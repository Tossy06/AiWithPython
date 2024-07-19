import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

api_key = '49e2bf11151133ab3c0d1e702a7d59e5'
city= 'Bogotá'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()

#Save adat
data_list = []

for i in data['list']:
    temp = i['main']['temp']
    wind_speed = i['wind']['speed']
    
    data_list.append({
        'temp': temp,
        'wind_speed': wind_speed
    })

df = pd.DataFrame(data_list)

x = df['temp'].values.reshape(-1,1)
y = df['wind_speed'].values.reshape(-1,1)

#Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)


#Transforn data
transformer = PolynomialFeatures(degree =2, include_bias = False)
x_poly_train = transformer.fit_transform(x_train)
x_poly_test = transformer.fit_transform(x_test)

#Create model and train this
model = LinearRegression()
model.fit(x_poly_train, y_train)

#Prediction and calculate error
y_pred = model.predict(x_poly_test)
print(f'The pressure prediction is: {y_pred}')
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f'Error percentage: {mape:.2f}%')

#Calculate the correlation between data
correlation = df['temp'].corr(df['wind_speed'])
print(f'The correlation between data is: {correlation}')

#Show graph

x_fit = np.linspace(x.min(), x.max(), 100).reshape(-1,1)
x_fit_poly = transformer.transform(x_fit)
y_fit = model.predict(x_fit_poly)

plt.scatter(x, y, color = 'm', label = 'Real data', alpha =.5)
plt.plot(x_fit, y_fit, label = 'Polynomial Regression', color = 'r')
plt.xlabel('Temperature')
plt.ylabel('Wind speed')
plt.title('Polynomial Regression')
plt.legend()
plt.show()

