"""
Main CLI logic for Eilam-CLI.
Handles argument parsing and user interaction using Click.
"""

import click
from .config import SUPPORTED_EDITORS, validate_editor
from .docker_ops import ContainerManager


@click.command()
@click.option('--image', required=True, help='Docker image to use (e.g., python, node, openjdk)')
@click.option('--version', required=True, help='Version of the image (e.g., 3.10, 18, 17)')
@click.option('--path', required=True, type=click.Path(exists=True, file_okay=False), help='Path to mount into the container')
@click.option('--editor', type=click.Choice(SUPPORTED_EDITORS), default='vim', show_default=True, help='Editor to use inside the container')
def cli(image, version, path, editor):
    """
    Main CLI entry point. Validates arguments and launches the container manager.

    Args:
        image (str): The base Docker image (e.g., 'python', 'node', 'openjdk').
        version (str): The version tag for the image (e.g., '3.10', '18', '17').
        path (str): Local path to mount into the container.
        editor (str): Editor to install and use inside the container.
    """
    try:
        validate_editor(editor)
        manager = ContainerManager()
        manager.run_container(image, version, path, editor)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == '__main__':
    cli()
