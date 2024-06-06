import requests
import json
url='https://httpbin.org/post'
payload = { 'name': 'David', 'curse': 'ApiPython'}
headers = {'Conten-type': 'aplication/json'}
response = requests.post(url, data = json.dumps(payload), headers=headers)

if response.status_code == 200:
    headers_response = response.headers
    print(headers_response)
    server = headers_response['Server']
    print("This is the server: ", server)
    
    