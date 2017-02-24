import urllib.request as urllib_request

from lxml import html

url_string = 'https://c.gethopscotch.com/p/ykcmajup8.html'
url_obj = urllib_request.urlopen(url_string).read()
page = html.fromstring(url_obj)

for div in page.xpath('//div'):

    div_data = div.get('data')
    if div_data:
        print(div_data)

        #TODO: write div_data as a .json file
