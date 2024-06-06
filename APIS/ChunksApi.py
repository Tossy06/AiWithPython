#Dowloading image
import requests
import json

url= 'https://i.pinimg.com/564x/34/9e/2a/349e2a4d065dcc55a417ac6f0528a5cf.jpg'
response = requests.get(url, stream=True) #Make reuest whithout downloading the content


if response.status_code == 200:
    with open('img.jpg','wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
response.close()