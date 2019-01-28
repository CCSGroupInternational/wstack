from .wsgi import load_app
from .cli.options import verboseprint
"""
The WebApp loads modules and metadata from an app JSON
"""

class WebApp(object):

    def __init__(self, app_json):
        app_module_name = app_json['module']
        print(verboseprint, print)
        verboseprint('Loading WSGI app', app_module_name)
        self.wsgi_app = load_app(app_module_name)
        self.path = app_json['path']

    def handle_request(self, environ, start_response):
        return self.wsgi_app(environ, start_response)