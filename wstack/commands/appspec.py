"""
Load WSGI applications
"""
import click
from sys import stderr
from importlib import import_module
from traceback import format_exc
from ..wsgi import wsgi_server, wsgi_app, set_routing

WSGI_APPS_DICT = {}


def load_wsgi_app(appname):
    try:
        module = import_module(appname)
    except ModuleNotFoundError:
        print(format_exc(), file=stderr)
        exit(1)
    except ImportError as error:
        print('Error loading module', appname, file=stderr)
        print(format_exc(), error, file=stderr)
        exit(2)
    if not hasattr(module, 'application'):
        print("Module {} does not provide an application object !!!".format(module), file=stderr)
        exit(3)
    return module.application


def load_app_spec(ctx, param, value):
    for app_spec in value:
        appname = app_spec.split(':')[0]
        WSGI_APPS_DICT[appname] = load_wsgi_app(appname)


@click.command()
@click.option('--appspec', '-a', callback=load_app_spec, type=str, multiple=True)
def run(appspec):
    set_routing(WSGI_APPS_DICT)
    wsgi_server(wsgi_app)
