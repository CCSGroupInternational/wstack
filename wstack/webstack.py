from .wsgi import load_app, set_routing, wsgi_server, routing_wsgi_app

def run(webstack_data):
    routing_dict = {}
    for app in webstack_data.get('apps'):
        wsgi_app = load_app(app['module'])
        app_route = app['path']
        routing_dict[app_route] = wsgi_app
    set_routing(routing_dict)
    wsgi_server(routing_wsgi_app)

