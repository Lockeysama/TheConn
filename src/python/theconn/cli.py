"""The Conn CLI - Command line interface for The Conn framework."""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel

from .commands import check, init, uninstall, update

console = Console()


@click.group()
@click.version_option(version="0.1.4", prog_name="theconn")
def main():
    """The Conn - AI-powered development framework.
    
    Easily integrate The Conn framework into your projects.
    """
    pass


@main.command()
@click.option(
    "--branch",
    default="main",
    help="GitHub branch to use (default: main)",
    show_default=True,
)
@click.option(
    "--path",
    type=click.Path(),
    default=".",
    help="Target directory (default: current directory)",
    show_default=True,
)
def init_cmd(branch: str, path: str):
    """Initialize The Conn framework in a project."""
    target_path = Path(path).resolve()
    
    try:
        init.run(target_path, branch)
        console.print(
            Panel(
                f"✅ [green]Successfully initialized The Conn framework![/green]\n\n"
                f"📁 Location: {target_path / '.the_conn'}\n"
                f"🌿 Branch: {branch}\n\n"
                f"📖 Next steps:\n"
                f"   1. Read .the_conn/GUIDE.md for usage instructions\n"
                f"   2. Add '.the_conn/ai_workspace/' to your .gitignore",
                title="🎉 Installation Complete",
                border_style="green",
            )
        )
    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {e}", style="bold red")
        sys.exit(1)


@main.command()
@click.option(
    "--branch",
    default=None,
    help="GitHub branch to use (default: same as installed version)",
)
@click.option(
    "--path",
    type=click.Path(exists=True),
    default=".",
    help="Target directory (default: current directory)",
    show_default=True,
)
def update_cmd(branch: Optional[str], path: str):
    """Update The Conn framework files."""
    target_path = Path(path).resolve()
    
    try:
        update.run(target_path, branch)
        console.print(
            Panel(
                f"✅ [green]Successfully updated The Conn framework![/green]\n\n"
                f"📁 Location: {target_path / '.the_conn'}\n\n"
                f"ℹ️  Your data (epics/, context/, ai_workspace/) has been preserved.",
                title="🎉 Update Complete",
                border_style="green",
            )
        )
    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {e}", style="bold red")
        sys.exit(1)


@main.command()
@click.option(
    "--path",
    type=click.Path(exists=True),
    default=".",
    help="Target directory (default: current directory)",
    show_default=True,
)
@click.confirmation_option(prompt="Are you sure you want to uninstall The Conn framework?")
def uninstall_cmd(path: str):
    """Uninstall The Conn framework (keeps user data)."""
    target_path = Path(path).resolve()
    
    try:
        uninstall.run(target_path)
        console.print(
            Panel(
                "✅ [green]Successfully uninstalled The Conn framework![/green]\n\n"
                "ℹ️  Your data (epics/, context/, ai_workspace/) has been preserved.\n"
                "   To completely remove, delete the .the_conn directory manually.",
                title="🗑️  Uninstall Complete",
                border_style="yellow",
            )
        )
    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {e}", style="bold red")
        sys.exit(1)


@main.command()
@click.option(
    "--path",
    type=click.Path(exists=True),
    default=".",
    help="Target directory (default: current directory)",
    show_default=True,
)
def check_cmd(path: str):
    """Check for updates."""
    target_path = Path(path).resolve()
    
    try:
        check.run(target_path)
    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {e}", style="bold red")
        sys.exit(1)


if __name__ == "__main__":
    main()
