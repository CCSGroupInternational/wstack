# Adapted from:
#
#   https://wsgi.readthedocs.io/en/latest/specifications/simple_authentication.html

from importlib import import_module
from os import getenv

class Middleware(object):

    def __init__(self, next_wsgi_app):
        self.next_wsgi_app = next_wsgi_app
        self.auth_module = import_module(getenv('AUTH_MODULE'))
        self.realm = getenv('AUTH_REALM')

    def __call__(self, environ, start_response):
        def repl_start_response(status, headers, exc_info=None):
            if status.startswith('401'):
                remove_header(headers, 'WWW-Authenticate')
                headers.append(('WWW-Authenticate', 'Basic realm="%s"' % self.realm))
            return start_response(status, headers)
        auth = environ.get('HTTP_AUTHORIZATION')
        if auth:
            scheme, data = auth.split(None, 1)
            assert scheme.lower() == 'basic'
            username, password = data.decode('base64').split(':', 1)
            if self.user_database.get(username) != password:
                return self.bad_auth(environ, start_response)
            environ['REMOTE_USER'] = username
            del environ['HTTP_AUTHORIZATION']
        return self.app(environ, repl_start_response)

    def bad_auth(self, environ, start_response):
        body = 'Please authenticate'
        headers = [
            ('content-type', 'text/plain'),
            ('content-length', str(len(body))),
            ('WWW-Authenticate', 'Basic realm="%s"' % self.realm)]
        start_response('401 Unauthorized', headers)
        return [body]

def remove_header(headers, name):
    for header in headers:
        if header[0].lower() == name.lower():
            headers.remove(header)
            break