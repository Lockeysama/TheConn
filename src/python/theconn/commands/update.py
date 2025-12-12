"""Update The Conn framework files."""

from datetime import datetime
from pathlib import Path
from typing import Optional

from rich.console import Console

from ..github import download_framework_files
from ..version import load_version_info, save_version_info

console = Console()


def run(target_path: Path, branch: Optional[str] = None) -> None:
    """Update The Conn framework.
    
    Args:
        target_path: Target project directory
        branch: GitHub branch to use (if None, use current branch)
    
    Raises:
        ValueError: If .the_conn doesn't exist
    """
    the_conn_dir = target_path / ".the_conn"
    
    # Check if initialized
    if not the_conn_dir.exists():
        raise ValueError(
            f"The Conn framework is not initialized in {target_path}\n"
            "Use 'theconn init' to initialize the framework."
        )
    
    # Load current version info
    current_version = load_version_info(the_conn_dir)
    
    # Use current branch if not specified
    if branch is None:
        branch = current_version.get("branch", "main")
        console.print(f"ℹ️  Using current branch: [cyan]{branch}[/cyan]")
    
    # Download framework files (update mode preserves user data)
    version_info = download_framework_files(the_conn_dir, branch, update_mode=True)
    version_info["installed_at"] = current_version.get("installed_at")
    version_info["updated_at"] = datetime.now().isoformat()
    
    # Save version info
    save_version_info(the_conn_dir, version_info)
