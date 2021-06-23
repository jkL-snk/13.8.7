import requests
import favicon
import sys, getopt

icons = favicon.get(sys.argv[1])
icon = icons[0]

response = requests.get(icon.url, stream=True)
with open('/app/python-favicon.{}'.format(icon.format), 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)


