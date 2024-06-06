import requests

url='https://www.google.co.uk/'
response = requests.get(url)

if response.status_code == 200:
    content= response.content
    file = open('google.html', 'wb')
    file.write(content)
    file.close()