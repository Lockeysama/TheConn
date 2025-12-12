"""Version management for The Conn framework."""

import json
from pathlib import Path
from typing import Any


VERSION_FILE = ".version"


def save_version_info(the_conn_dir: Path, version_info: dict[str, Any]) -> None:
    """Save version information.
    
    Args:
        the_conn_dir: The .the_conn directory
        version_info: Version information dict
    """
    version_file = the_conn_dir / VERSION_FILE
    with version_file.open("w", encoding="utf-8") as f:
        json.dump(version_info, f, indent=2, ensure_ascii=False)


def load_version_info(the_conn_dir: Path) -> dict[str, Any]:
    """Load version information.
    
    Args:
        the_conn_dir: The .the_conn directory
    
    Returns:
        Version information dict, or empty dict if not found
    """
    version_file = the_conn_dir / VERSION_FILE
    if not version_file.exists():
        return {}
    
    with version_file.open("r", encoding="utf-8") as f:
        return json.load(f)
