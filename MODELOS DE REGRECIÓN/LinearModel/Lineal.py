import matplotlib.pyplot as plt
import numpy as np

x = [173, 171, 189, 181]
y = [81, 72, 96, 94]

x_ones = np.c_[np.ones(4), x]
print(x_ones)

theta = np.linalg.inv(x_ones.T.dot(x_ones)).dot(x_ones.T).dot(y)
print(theta)

plt.scatter(x, y, s =40, c = '#06d6a0')
x_lim = [170, 190]
x_lim_ones = np.c_[np.ones(2), x_lim]
y_lim = x_lim_ones.dot(theta)
plt.plot(x_lim, y_lim, 'r')

whigth_david = theta[0] + theta[1] * 179
print(whigth_david)
plt.show()
