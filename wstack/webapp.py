from .wsgi import load_app
"""
The WebApp loads modules and metadata from an app JSON
"""

class WebApp(object):

    def __init__(self, app_json):
        self.wsgi_app = load_app(app_json['module'])
        self.path = app_json['path']

    def handle_request(self, environ, start_response):
        return self.wsgi_app(environ, start_response)