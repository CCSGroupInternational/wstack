from .wsgi import wsgi_server, routing_wsgi_app, add_route
from .webapp import WebApp


def run(webstack_data):

    for app_data in webstack_data.get('apps'):
        webapp = WebApp(app_data)
        add_route(webapp, webapp.path)
    wsgi_server(routing_wsgi_app)
