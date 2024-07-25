import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype = float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype = float)

capa = tf.keras.layers.Dense(units =1, input_shape =[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

print("Comezando el entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs =1000, verbose = False)
print("Modelo entrenado")

plt.xlabel("·Epoca")
plt.ylabel("Magnitud de  pèrdida")
plt.plot(historial.history["loss"])
plt.show()

print("Hgamos una predicciòn")
resultado = modelo.predict(np.array([100.0]))
print('El resultado es:'+ str(resultado[0][0])+ 'F' )