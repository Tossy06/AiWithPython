import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

api_key = '49e2bf11151133ab3c0d1e702a7d59e5'
city = 'Bogotá'
lat = 4.7110
lon = -74.0721
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'

response = requests.get(url)
data = response.json()
print(data)
data_list = []

for climate in data['list']:
    humidity = climate['main']['humidity']
    temp = climate['main']['temp']
    
    data_list.append({
        'humidity' : humidity,
        'temp': temp
    })

df = pd.DataFrame(data_list)

x = df['humidity'].values.reshape(-1,1)
y = df['temp'].values.reshape(-1,1)

correlation = df['humidity'].corr(df['temp'])
print(f'The correlation is: {correlation}')


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)


model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(y_test)

print(f'Values prediction are: \n{y_pred}\n')
print(f'Real data is: \n{y_test}\n')

r2= model.score(x_test,y_test)
print(f'Determination Coefficient is: {r2}')


plt.scatter(x_train, y_train, label = "Training Data", color = 'r', alpha= .7)
plt.scatter(x_test, y_test, label = 'Test Data', color = 'm', alpha = .7)
plt.plot(x, model.predict(x), color='g', label = 'Regression line')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.legend()
plt.show()