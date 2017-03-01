import urllib.request as urllib_request
import os
import json

from lxml import html


def read_url(url_string):

    url_obj = urllib_request.urlopen(url_string).read()
    page = html.fromstring(url_obj)

    for div in page.xpath('//div'):

        div_data = div.get('data')
        if div_data:

            print('Project JSON was found.')

            project_data = div_data
            write_json_file(project_data)

def write_json_file(data):

    project_id = 621 #div_data['user_id']
    file_path_project_data = os.path.join('project_data', str(project_id) + '.json')

    with open(file_path_project_data, 'w') as project_data_file:
        json.dump(json.loads(data), project_data_file, ensure_ascii=False, indent=4, sort_keys=True)
        print('Attempting to write the JSON to a file')

    '''
    # Clear encapsulating ""
    with open(file_path_project_data) as project:

        for line in project:

            # Clear backslashes
            line = line.replace('\\', '')

        project = project[1:-1]
    '''

read_url('https://c.gethopscotch.com/p/ykcmajup8.html')
