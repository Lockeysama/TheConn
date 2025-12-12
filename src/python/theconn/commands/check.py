"""Check for framework updates."""

from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from ..github import GitHubClient
from ..version import load_version_info

console = Console()


def run(target_path: Path) -> None:
    """Check for framework updates.
    
    Args:
        target_path: Target project directory
    
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
    current_branch = current_version.get("branch", "unknown")
    current_commit = current_version.get("commit", "unknown")
    
    # Get latest commit from GitHub
    console.print(f"🔍 Checking for updates on branch '[cyan]{current_branch}[/cyan]'...")
    
    try:
        client = GitHubClient()
        latest_commit = client.get_branch_commit(current_branch)
        
        # Create comparison table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Version", style="cyan")
        table.add_column("Commit SHA", style="yellow")
        table.add_column("Status", style="green")
        
        table.add_row(
            "Current",
            current_commit[:7] if current_commit != "unknown" else current_commit,
            "✓ Installed"
        )
        table.add_row(
            "Latest",
            latest_commit[:7],
            "✓ Available"
        )
        
        console.print(table)
        
        # Check if update is available
        if current_commit == latest_commit:
            console.print(
                Panel(
                    "[green]✅ You are using the latest version![/green]",
                    border_style="green",
                )
            )
        else:
            console.print(
                Panel(
                    "[yellow]⚠️  A new version is available![/yellow]\n\n"
                    "Run '[cyan]theconn update[/cyan]' to update to the latest version.",
                    border_style="yellow",
                )
            )
    except Exception as e:
        console.print(f"[red]❌ Error checking for updates:[/red] {e}")
        raise
