import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR


api_key = '49e2bf11151133ab3c0d1e702a7d59e5'
city = 'Bogotá'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()
print(data)
data_list = []

for find in data['list']:
    temp = find['main']['temp']
    wind_speed = find['wind']['speed']
    
    data_list.append({
        'temp' : temp,
        'speed': wind_speed
    })
    
df = pd.DataFrame(data_list)
x = df['temp'].values.reshape(-1, 1)
y = df['speed'].values.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

#I define the algorithm
svr = SVR(kernel ='linear', C = 1.0, epsilon = 0.2)
svr.fit(x_train, y_train)

#Prediction
y_pred = svr.predict(x_test)

#Show graph
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color = 'r')
plt.show()