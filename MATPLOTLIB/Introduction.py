import matplotlib.pyplot as plt
a = [1 , 2, 3, 4]
b = [1, 5, 10, 15]
#Graph creation
plt.plot(a, b, color ="blue", linewidth = 3, label = "linea")
plt.legend()
#Graph display
plt.grid()
plt.show()