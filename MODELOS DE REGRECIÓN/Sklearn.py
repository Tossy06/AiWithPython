from pydataset import data
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

pima = data('Pima.tr')

pima.plot(kind= 'scatter', x = 'skin', y = 'bmi')
plt.legend()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(pima.skin, pima.bmi )
plt.scatter(x_train, y_train, label = 'Training Data', color = 'r', alpha= .7 )
plt.scatter(x_test, y_test, label = 'Test Data', color = 'g', alpha= .7)
plt.legend()
plt.show()
#Create linear model and train it

LR = LinearRegression()
LR.fit(x_train.values.reshape(-1,1), y_train.values)

prediction = LR.predict(x_test.values.reshape(-1,1))
plt.plot(x_test, prediction, label = 'Label Regression', color = 'b' )
plt.scatter(x_test, y_test, label = 'Actual Test Data', color = 'g', alpha= .7)
plt.legend()
plt.show()
prediction2= LR.predict(np.array([[50]]))[0]
print(prediction2)
score = LR.score(x_test.values.reshape(-1, 1), y_test.values)
print(score)
