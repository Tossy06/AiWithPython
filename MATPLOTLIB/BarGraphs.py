import matplotlib.pyplot as plt

x1= [0.22, 1.25, 2.25, 3.25, 4]
y1= [5, 10, 44, 23, 20]

#Graph creation
plt.bar(x1, y1, color = 'lightblue', width= 0.25, label = "Data1")

#Graph display
plt.legend()
plt.grid()
plt.show()