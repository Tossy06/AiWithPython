import requests
import json

client_id = 'Ov23lifgN6LXHhnrh0Ke'
client_secret = '529a34fd427913c1164e61c30cc6c7cff278fdfc'
code ='dbd1cf1f601dd717a94a'
access_token =''
url='https://github.com/login/oauth/access_token'
payload = {'client' : client_id, 'client_secret' : client_secret, 'code' : code}
headers= {'Accept' : 'application/json'}
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    response_json = response.json()
    access_token = response_json['access_token']
    print(access_token)
else:
    print("NOP")
