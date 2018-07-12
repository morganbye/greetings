import requests
import simplejson as json
import os
from pprint import pprint

username = 'test_user'

# local server
URL = 'http://0.0.0.0:6543/'

# production server
#URL = 'https://test.com/'

# Create session object, which can be used for all requests.
request_handle = requests.Session()

# Set up appropriate headers.
headers = {'Content-Type': 'application/json',
           'Accept': 'application/json'}

# Send the POST request, with your username & password, converted to json.
response = request_handle.post(os.path.join(URL, 'users'),
                               data=username,
                               headers=headers)

if response.status_code != requests.codes.ok:
    # User `requests` built-in raise error
    response.raise_for_status()

# Add the authentication token to the headers.
token = response.json()
headers['X-Messaging-Token'] = token

# Make api request
response = request_handle.get(os.path.join(URL, 'users'),
                              headers=headers)

if response.status_code != requests.codes.ok:
    response.raise_for_status()

pprint(response.json(), indent=1)

# Delete session
request_handle.delete(os.path.join(URL, 'users'),
                      headers=headers)
