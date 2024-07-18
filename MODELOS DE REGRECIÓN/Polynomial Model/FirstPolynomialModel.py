import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

m = 100
x = 6 * np.random.rand(m, 1) - 3
y = 2 + x + 0.5 * x**2 + np.random.rand (m, 1)

poly_features = PolynomialFeatures(degree=2, include_bias = False)
x_poly = poly_features.fit_transform(x)

lin_reg = LinearRegression()
lin_reg.fit(x_poly, y)

x_plot = np.linspace(-3, 3, m).reshape(m, 1)
x_plot_poly = poly_features.transform(x_plot)
y_plot = lin_reg.predict(x_plot_poly)

plt.scatter(x, y, color = 'r', alpha = .7, s = 10)
plt.plot(x_plot, y_plot, 'g')
plt.show()