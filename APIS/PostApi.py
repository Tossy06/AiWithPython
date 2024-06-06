import requests
import json
url='https://httpbin.org/post'
payload = { 'name': 'David', 'curse': 'ApiPython'}
response = requests.post(url, data = json.dumps(payload))

if response.status_code == 200:
    content = response.json()
    print(content)
    
    