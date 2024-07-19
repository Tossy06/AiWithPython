import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error

x = np.array([1,2,3,4,5]).reshape(-1, 1) #independent variables
y = np. array ([2, 4, 6, 8, 10]) #dependent variable

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

#Create model and train it
model = LinearRegression()
model.fit(x_train, y_train)

#Select a number for prediction
prediction = model.predict(np.array([[8]]))[0]
print("The prediction for x = 6 is: ", prediction)

#Calculate error
y_pred = model.predict(x_test)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f'Error percentrage: {mape:.2f}%')

#Equation
intercept = model.intercept_
pendeinte = model.coef_[0]
print(f'The ecuation is: y = {pendeinte}(x) + {intercept}')

#Show data
plt.scatter(x_train, y_train, label = "Training Data", color = 'r', alpha= .7)
plt.scatter(x_test, y_test, label = 'Test Data', color = 'g', alpha = .7)

#Graph straight line
plt.plot(x, model.predict(x), color = 'b', label = 'Regression Line')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

