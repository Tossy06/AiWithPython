import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from mpl_toolkits.mplot3d import Axes3D

api_key = '49e2bf11151133ab3c0d1e702a7d59e5'
city = 'Bogotá'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

# List for save data
data_list = []

# Extrae los datos del pronóstico
for forecast in data['list']:
    temp = forecast['main']['temp']
    humidity = forecast['main']['humidity']
    wind_speed = forecast['wind']['speed']
    pressure = forecast['main']['pressure']
    
    # Agrega los datos a la lista
    data_list.append({
        'temp': temp,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'pressure': pressure
    })

# Crate data frame with data
df = pd.DataFrame(data_list)
#show data frame
x = df[['temp', 'humidity', 'wind_speed']]
y = df['pressure']

#Create model and trainig
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)

#Prediction and calculate error
y_pred = model.predict(x_test)
print(f'The pressure prediction is: {y_pred}')
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f'Error percentage: {mape:.2f}%')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_test['temp'], x_test['humidity'], y_test, color='r', label='Actual')
ax.scatter(x_test['temp'], x_test['humidity'], y_pred, color='b', label='Predicted')
ax.set_xlabel('Temperature')
ax.set_ylabel('Humidity')
ax.set_zlabel('Pressure')
plt.legend()
plt.show()