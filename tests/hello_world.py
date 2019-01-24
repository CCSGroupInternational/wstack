# https://www.python.org/dev/peps/pep-3333/

HELLO_WORLD = b"Hello world!\n"


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [HELLO_WORLD]


application = simple_app
