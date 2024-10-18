import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Data
temperature_data = pd.read_csv(r'C:\Users\user.USER-PC\Documents\AiWithPython\Projects\CtoF\celsius_a_fahrenheit.csv')
#sns.scatterplot(x=temperature_data['Celsius'], y=temperature_data['Fahrenheit'], color='green')
#plt.show()

x_train = np.array(temperature_data['Celsius']) 
y_train = np.array(temperature_data['Fahrenheit']) 

#Model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#Compile
model.compile(optimizer=tf.keras.optimizers.Adam(1.5), loss='mean_squared_error')

#Train
epochs_history = model.fit(x_train, y_train, epochs= 100)

epochs_history.history.keys()

#Loss graph
plt.plot(epochs_history.history['loss'])
plt.title('Model Loss Progress')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['Train Loss'])
plt.show()

model.get_weights()

#Predict
def celcius_to_fahrenheit(celsius):
    celsius_array = np.array([celsius])
    prediction = model.predict([celsius_array])
    return prediction[0][0]
print ('Predicting celsius to fahrenheit', celcius_to_fahrenheit(0))