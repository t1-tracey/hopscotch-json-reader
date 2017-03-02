import urllib.request as urllib_request
import os
import json
from lxml import html

def read_url(url_string):

    '''
    Takes a Hopscotch project URL (may need to have .html at the end, but unconfirmed) and writes its data into a .json file
    '''

    url_obj = urllib_request.urlopen(url_string).read()
    page = html.fromstring(url_obj)

    for div in page.xpath('//div'):

        # Get the JSON from the 'data' attribute of the <div> tag
        # This is made on the assumption that there is only one <div> tag that has a 'data' attribute where Hopscotch stores the JSON data
        div_data = div.get('data')

        if div_data:
            print('Project JSON was found.')

            # Convert the string containing the data from the <div> tag into a Python object
            project_data = json.loads(div_data)

            write_json_file(project_data)

def write_json_file(data):

    '''
    Takes a Python object and writes it into a .json file
    '''

    project_id = data['uuid']
    file_path_data = os.path.join('project_data', str(project_id) + '.json')

    with open(file_path_data, 'w') as project_file:
        json.dump(data, project_file, ensure_ascii=False, indent=4, sort_keys=True)
        print('Writing the JSON to a file.')

read_url('https://c.gethopscotch.com/p/ykcmajup8.html')
