import json

from pprint import pprint

with open('example.json') as json_file:
    json_data = json.load(json_file)

# pprint(json_data)

pencils = json_data['pencils']

for pencil in pencils:

    dollar_plurality = 'dollars' if not int(pencil['price']) == 1 else 'dollar'
    print('This is a ' + pencil['color'] + ' pencil that costs ' + pencil['price'] + ' ' + dollar_plurality + '.')
