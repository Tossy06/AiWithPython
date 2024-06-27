import matplotlib.pyplot as plt

x1 = [0.25, 1.25, 2.23, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]

x2 = [0.45, 2.25, 2.80, 3.75, 5.25]
y2= [15, 65, 75, 45, 23]

plt.scatter(x1, y1, label = 'Data1', color = "red")
plt.scatter(x2, y2, label = 'Data1', color = "orange")
plt.legend()
plt.grid()
plt.show()