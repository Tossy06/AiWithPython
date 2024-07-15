import quandl
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
import datetime as dt

quandl.ApiConfig.api_key = 'YYhdhKLv8nrUA498h7CP'

data = quandl.get("WIKI/GOOGL")
print(data)
data = data[['Adj. Close']]
data.dropna(inplace = True)

x = np.array(data.index.factorize()[0]).reshape(-1, 1)
y = data['Adj. Close'].values

#Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

#Train model

model = LinearRegression()
model.fit(x_train, y_train)

#Predic for especific date into database
def predict_adj_date(modell, date):
    Reference_date = data.index.min()
    index_date= (date - Reference_date).days
    prediction = modell.predict(np.array([[index_date]]))
    return prediction[0]

date_prediction = dt.datetime(2004, 8, 19)
value_prediction = predict_adj_date(model, date_prediction)
print(f'Prediction for the date {date_prediction.strftime("%Y-%m-%d")} is: {value_prediction}')

#Make predictions
y_pred = model.predict(x_test)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f'Error percentrage: {mape:.2f}%')

#Equqtion
intercept = model.intercept_
pendiente = model.coef_[0]

print(f'The equation is: y = {pendiente}(x) + {intercept}')


#Show data
plt.scatter(x_train, y_train, label = "Training Data", color ='b', alpha=.7)
plt.scatter(x_test, y_test, label = "Test Data", color = 'r', alpha= .7)
plt.xlabel('Date')
plt.ylabel('Adj. Close')

#Graph straight line
plt.plot(x, model.predict(x), color = 'g', label = 'Regression line')
plt.legend()
plt.show()

