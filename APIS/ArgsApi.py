import requests
import json
url='https://httpbin.org/get'
args = { 'name': 'David', 'curse': 'ApiPython'}
response = requests.get(url, params= args)

if response.status_code == 200:
    content = response.json()
    print(content)
    #Get a especific value from json
    '''
    origin = content['origin']
    print('This is the origin:', origin)
    '''
    content2 = json.loads(response.text)
    origin = content2['origin']
    print('This is the origin:', origin)
    