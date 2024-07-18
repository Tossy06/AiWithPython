import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([3, 6, 8, 11, 15, 18])

transformer = PolynomialFeatures(degree = 2, include_bias = False) 
x_poly = transformer.fit_transform(x[:, np.newaxis])

#Train model
model = LinearRegression()
model.fit(x_poly, y)

x_new = np.array([7, 8])
x_new_poly = transformer.transform(x_new[:, np.newaxis])
y_pred = model.predict(x_new_poly)

x_fit = np.linspace(1, 8, 100)
x_fit_poly = transformer.transform(x_fit[:, np.newaxis])
y_fit = model.predict(x_fit_poly)


plt.scatter(x, y, label='Datos de muestra')
plt.plot(x_fit, y_fit, label='Regresión Polinomial', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()