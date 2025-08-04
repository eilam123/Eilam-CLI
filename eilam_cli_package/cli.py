import click
from .utils import LANGUAGE_IMAGES, EDITORS
from .container import ContainerManager

@click.command()
@click.option('--language', required=True, type=click.Choice(LANGUAGE_IMAGES.keys()), help='Programming language (e.g., python, node, java)')
@click.option('--version', required=True, help='Version of the language (e.g., 3.10, 18, 17)')
@click.option('--path', required=True, type=click.Path(exists=True, file_okay=False), help='Path to mount into the container')
@click.option('--editor', type=click.Choice(EDITORS), default='vim', show_default=True, help='Editor to use inside the container')
def cli(language, version, path, editor):
    image = f"{LANGUAGE_IMAGES[language]}:{version}"
    manager = ContainerManager()
    try:
        manager.run_container(image, path, editor)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == '__main__':
    cli()
