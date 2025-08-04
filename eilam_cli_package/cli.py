import click
from .config import SUPPORTED_LANGUAGES, SUPPORTED_EDITORS, validate_language, validate_editor
from .docker_ops import ContainerManager

@click.command()
@click.option('--language', required=True, type=click.Choice(SUPPORTED_LANGUAGES.keys()), help='Programming language (e.g., python)')
@click.option('--version', required=True, help='Version of the language (e.g., 3.10)')
@click.option('--path', required=True, type=click.Path(exists=True, file_okay=False), help='Path to mount into the container')
@click.option('--editor', type=click.Choice(SUPPORTED_EDITORS), default='vim', show_default=True, help='Editor to use inside the container')
def cli(language, version, path, editor):
    try:
        validate_language(language, version)
        validate_editor(editor)
        manager = ContainerManager()
        manager.run_container(language, version, path, editor)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == '__main__':
    cli()
