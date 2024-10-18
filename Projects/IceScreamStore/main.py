import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

datos_ventas = pd.read_csv(r'C:\Users\user.USER-PC\Documents\AiWithPython\Projects\IceScreamStore\datos_de_ventas.csv')
#print (datos_ventas)

x_train =np.array(datos_ventas['Temperature'])
y_train = np.array(datos_ventas['Revenue'])

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

epochs_history = model.fit(x_train, y_train, epochs=1000)

plt.plot(epochs_history.history['loss'])
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train Loss'])
plt.show()

def revenue_predict(temperature):
    temperature_array = np.array([temperature])
    prediction = model.predict([temperature_array])
    return prediction[0][0]
print(f'Revenue prediction for 5°C: {revenue_predict(5)}')