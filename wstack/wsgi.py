from os import environ
from urllib.parse import urlparse
from wsgiref.util import setup_testing_defaults, request_uri
from wsgiref.simple_server import make_server
from importlib import import_module

# TODO: Analyze & improve the path routing performance

URI_ROUTING = {}

def load_app(appname):
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


def set_routing(wsgi_dict):
    """
    Build the http routing table from a "wsgi_dict" { 'uri_path' : wsgi_app }
    """
    for uri_path, wsgi_app in wsgi_dict.items():
        uri_path = uri_path.strip('/').replace('.', '/')
        URI_ROUTING[uri_path] = wsgi_app


def routing_wsgi_app(environ, start_response):
    setup_testing_defaults(environ)
    parsed_uri = urlparse(request_uri(environ, include_query=False))
    request_path = parsed_uri.path.strip('/')
    for uri_path, wsgi_app in URI_ROUTING.items():
        if request_path == uri_path:
            return wsgi_app(environ, start_response)

    status = '404 Not Found'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)
    return ["Not Found".encode('utf-8')]


def wsgi_server(wsgi_app):
    PORT = int(environ.get('PORT', 8000))
    with make_server('', PORT, wsgi_app) as httpd:
        print("Serving on port %d..." % PORT)
        httpd.serve_forever()
