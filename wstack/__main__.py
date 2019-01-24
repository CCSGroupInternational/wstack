from .commands.appspec import run
from . import version
import click


@click.group()
@click.version_option(version=version)
def cli():
    pass


cli.add_command(run)

if __name__ == '__main__':
    cli()
