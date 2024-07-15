import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error

x = np.array([
    1500, 1800, 2400, 3000, 1200, 2000, 2200, 1600, 2800, 2500,
    2100, 1900, 2300, 2700, 3100, 1300, 1400, 2600, 1700, 2900,
    2000, 1500, 2200, 1800, 2300, 2400, 2500, 2600, 2700, 2800
]).reshape(-1, 1)

y = np.array([
    300000, 350000, 450000, 600000, 200000, 400000, 420000, 320000, 550000, 470000,
    380000, 360000, 440000, 530000, 610000, 220000, 250000, 500000, 340000, 570000,
    410000, 310000, 430000, 370000, 450000, 460000, 480000, 490000, 510000, 520000
])

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state= 42)

#Create model
model = LinearRegression()
model.fit(x_train, y_train)

#Select a number for prediction
prediction = model.predict(np.array([[2500]]))[0]
print("The prediction for x = 2500 is: ", prediction)

#Calculate error
y_pred = model.predict(x_test)
mape = mean_absolute_percentage_error(y_test, y_pred) *100
print(f'Error percentrage: {mape:.2f}%')

#Show data

plt.scatter(x_train, y_train, label = 'Training Data', color = 'y', alpha= .7)
plt.scatter(x_test, y_test, label = 'Test Data', color = 'r', alpha= .7,)
plt.plot(x, model.predict(x), color = 'm', label = 'Regression Line')
plt.legend()
plt.grid()
plt.xlabel('Size')
plt.ylabel('Price')
plt.show()
