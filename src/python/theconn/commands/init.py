"""Initialize The Conn framework in a project."""

from datetime import datetime
from pathlib import Path

from ..github import download_framework_files
from ..version import save_version_info


def run(target_path: Path, branch: str) -> None:
    """Initialize The Conn framework.
    
    Args:
        target_path: Target project directory
        branch: GitHub branch to use
    
    Raises:
        ValueError: If .the_conn already exists
    """
    the_conn_dir = target_path / ".the_conn"
    
    # Check if already initialized
    if the_conn_dir.exists():
        raise ValueError(
            f"The Conn framework is already initialized in {target_path}\n"
            "Use 'theconn update' to update the framework."
        )
    
    # Create .the_conn directory
    the_conn_dir.mkdir(parents=True, exist_ok=True)
    
    # Download framework files
    version_info = download_framework_files(the_conn_dir, branch, update_mode=False)
    version_info["installed_at"] = datetime.now().isoformat()
    
    # Save version info
    save_version_info(the_conn_dir, version_info)
