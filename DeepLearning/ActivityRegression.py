import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
# Generar los valores de x de 0 a 99
x = np.arange(100)
# Calcular los valores de y = e^x
y = np.exp(x)
x_train, y_train, x_test, y_test = train_test_split(x, y, test_size =0.2, random_state= 42)

model = tf.keras.Sequential([
    
])

