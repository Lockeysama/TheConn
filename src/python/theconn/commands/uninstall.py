"""Uninstall The Conn framework."""

import shutil
from pathlib import Path

from rich.console import Console

console = Console()


def run(target_path: Path) -> None:
    """Uninstall The Conn framework (keeps user data).
    
    Args:
        target_path: Target project directory
    
    Raises:
        ValueError: If .the_conn doesn't exist
    """
    the_conn_dir = target_path / ".the_conn"
    
    # Check if initialized
    if not the_conn_dir.exists():
        raise ValueError(
            f"The Conn framework is not initialized in {target_path}"
        )
    
    # Remove framework files only
    framework_items = [
        "rules",
        "playbooks",
        "docs",
        ".version",
    ]
    
    for item in framework_items:
        item_path = the_conn_dir / item
        if item_path.exists():
            if item_path.is_dir():
                shutil.rmtree(item_path)
            else:
                item_path.unlink()
    
    # Check if .the_conn is now empty (only user data left)
    remaining_items = list(the_conn_dir.iterdir())
    if not remaining_items:
        # Remove empty directory
        the_conn_dir.rmdir()
        console.print("ℹ️  Removed empty .the_conn directory")
