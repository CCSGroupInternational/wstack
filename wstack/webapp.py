from .wsgi import load_app
"""
The WebApp loads modules and metadata from an app JSON
"""

class WebApp(object):

    def __init__(self, app_json):
        
        # Load the WSGI application module
        app_module_name = app_json['module']
        self.wsgi_app = load_app(app_module_name)
        self.path = app_json['path']

        pre_filter_module_list = []
        for filter_module_name in app_json.get('pre-filters', []):
            filter_module = load_app(filter_module_name, is_middleware=True)
            pre_filter_module_list.append(filter_module)
        
        pre_filter_mdw = []
        for i, module in enumerate(pre_filter_module_list):
            pre_filter_mdw = module(pre_filter_module_list[i]+1)


    def handle_request(self, environ, start_response):
        return self.wsgi_app(environ, start_response)