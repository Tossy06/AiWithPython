import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


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
x_adr = df['speed'].values.reshape(-1, 1)
y_adr = df['temp'].values.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x_adr, y_adr, test_size= 0.2, random_state= 42)


adr = DecisionTreeRegressor(max_depth = 5)
adr.fit(x_train, y_train)

y_pred = adr.predict(x_test)

x_grid = np.arange(min(x_test), max(x_test), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x_test, y_test)
plt.plot(x_grid, adr.predict(x_grid), color ='r')
plt.show()