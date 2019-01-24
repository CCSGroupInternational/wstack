import json
from ..webstack import run as webstack_run

def process(json_file_list):
    for json_filename in json_file_list:
        with open(json_filename) as json_file:
            json_data = json.load(json_file)
            webstack_data = json_data.get('webstack', None)
            if webstack_data is not None:
                webstack_run(webstack_data)

