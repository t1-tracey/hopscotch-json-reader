import json
import os

from pprint import pprint


def open_json_file(filepath):

    with open(filepath, 'r') as json_file:
        project_data = json.load(json_file)

    #TODO: what if filepath does not exist?

    return project_data

project = open_json_file(os.path.join('project_data', '621.json'))
print(project['abilities'][2]['blocks'][0]['description'])
