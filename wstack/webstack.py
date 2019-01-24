from .wsgi import load_app

def run(webstack_data):
    print(webstack_data)
    for app in webstack_data.get('apps'):
        wsgi_app = load_app(app['module'])

