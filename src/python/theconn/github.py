"""GitHub integration for downloading framework files."""

import shutil
from pathlib import Path
from typing import Optional

import requests
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

GITHUB_REPO = "Lockeysama/TheConn"
GITHUB_API_BASE = "https://api.github.com"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com"


class GitHubClient:
    """Client for interacting with GitHub repository."""
    
    def __init__(self, repo: str = GITHUB_REPO):
        self.repo = repo
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
        })
    
    def get_branch_commit(self, branch: str) -> str:
        """Get the latest commit SHA for a branch."""
        url = f"{GITHUB_API_BASE}/repos/{self.repo}/branches/{branch}"
        response = self.session.get(url)
        
        if response.status_code == 404:
            raise ValueError(f"Branch '{branch}' not found in repository {self.repo}")
        
        response.raise_for_status()
        data = response.json()
        return data["commit"]["sha"]
    
    def get_default_branch(self) -> str:
        """Get the default branch of the repository."""
        url = f"{GITHUB_API_BASE}/repos/{self.repo}"
        response = self.session.get(url)
        response.raise_for_status()
        data = response.json()
        return data["default_branch"]
    
    def download_directory(
        self,
        branch: str,
        source_path: str,
        target_path: Path,
        exclude: Optional[list[str]] = None,
    ) -> None:
        """Download a directory from GitHub recursively.
        
        Args:
            branch: Branch name
            source_path: Path in repository
            target_path: Local target path
            exclude: List of paths to exclude (relative to source_path)
        """
        exclude = exclude or []
        url = f"{GITHUB_API_BASE}/repos/{self.repo}/contents/{source_path}?ref={branch}"
        
        response = self.session.get(url)
        response.raise_for_status()
        
        items = response.json()
        if not isinstance(items, list):
            # Single file
            items = [items]
        
        for item in items:
            item_name = item["name"]
            item_path = item["path"]
            
            # Check if excluded
            relative_path = item_path[len(source_path):].lstrip("/")
            if any(relative_path.startswith(ex) for ex in exclude):
                continue
            
            if item["type"] == "file":
                # Download file
                file_content = self.session.get(item["download_url"]).content
                target_file = target_path / relative_path
                target_file.parent.mkdir(parents=True, exist_ok=True)
                target_file.write_bytes(file_content)
            elif item["type"] == "dir":
                # Recurse into directory
                self.download_directory(branch, item_path, target_path, exclude)
    
    def download_file(self, branch: str, source_path: str, target_path: Path) -> None:
        """Download a single file from GitHub.
        
        Args:
            branch: Branch name
            source_path: Path in repository
            target_path: Local target path
        """
        url = f"{GITHUB_RAW_BASE}/{self.repo}/{branch}/{source_path}"
        response = self.session.get(url)
        
        if response.status_code == 404:
            raise ValueError(f"File '{source_path}' not found in branch '{branch}'")
        
        response.raise_for_status()
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(response.content)


def download_framework_files(
    target_dir: Path,
    branch: str = "main",
    update_mode: bool = False,
) -> dict:
    """Download The Conn framework files from GitHub.
    
    Args:
        target_dir: Target .the_conn directory
        branch: GitHub branch to use
        update_mode: If True, only update framework files (preserve user data)
    
    Returns:
        Version info dict
    """
    client = GitHubClient()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        # Get commit SHA
        task = progress.add_task(f"Fetching branch '{branch}' info...", total=None)
        commit_sha = client.get_branch_commit(branch)
        progress.update(task, description=f"✓ Branch: {branch} ({commit_sha[:7]})")
        
        # Download ai_prompts/
        progress.add_task("Downloading ai_prompts...", total=None)
        prompts_dir = target_dir / "ai_prompts"
        if prompts_dir.exists():
            shutil.rmtree(prompts_dir)
        client.download_directory(branch, ".the_conn/ai_prompts", target_dir, exclude=[])
        
        # Download GUIDE.md
        progress.add_task("Downloading GUIDE.md...", total=None)
        client.download_file(branch, ".the_conn/GUIDE.md", target_dir / "GUIDE.md")
        
        # Download README.md
        progress.add_task("Downloading README.md...", total=None)
        client.download_file(branch, ".the_conn/README.md", target_dir / "README.md")
        
        # Create directory structure (only in init mode)
        if not update_mode:
            progress.add_task("Creating directory structure...", total=None)
            (target_dir / "epics").mkdir(exist_ok=True)
            (target_dir / "context" / "global").mkdir(parents=True, exist_ok=True)
            (target_dir / "context" / "epics").mkdir(parents=True, exist_ok=True)
            (target_dir / "ai_workspace").mkdir(exist_ok=True)
    
    # Save version info
    version_info = {
        "branch": branch,
        "commit": commit_sha,
        "installed_at": None,  # Will be set by caller
    }
    
    return version_info
