import requests

url='https://api.jikan.moe/v4/top/anime'
data=requests.get(url)

if data.status_code == 200:
    data = data.json()
    for e in data['data']:
        print(e['title'])