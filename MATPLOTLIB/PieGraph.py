import matplotlib.pyplot as plt

jugar = [7,2,3,8,10]
estudiar = [15,20,30,4,9]
dormir = [2,1,3,0,4]

divisiones = [5, 50, 45]
colores = ['red', 'orange', 'purple']
actividades =['jugar', 'estudiar', 'dormir']

plt.pie(divisiones, labels = actividades, colors=colores, autopct='%1.1f%%', startangle = 45, shadow = True, explode= (0.1,0,0))
plt.show()
