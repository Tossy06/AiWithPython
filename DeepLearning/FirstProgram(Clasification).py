import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(f"x_train: {x_train.shape}, y_train: {y_train.shape}")
print(f"x_test: {x_test.shape}, y_test: {y_test.shape}")

x_train, x_test = x_train / 255.0, x_test / 255.0

#Build model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape = (28,28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
])
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()


print("Comezando el entrenamiento...")
history = model.fit(x_train, y_train, epochs = 15, validation_split = 0.2)
print("Modelo entrenado")
#show graphics
plt.xlabel("·Epoca")
plt.ylabel("Magnitud de  pèrdida")
plt.plot(history.history["loss"])
plt.show()

predictions = model.predict(x_test)

def predict_and_show_images(images, true_labels):
    predictions = model.predict(images)
    predicted_labels = np.argmax(predictions, axis=1)

    plt.figure(figsize=(5, 5))
    for i in range(len(images)):
        plt.subplot(2, 5, i + 1)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.title(f'Pred: {predicted_labels[i]}\nTrue: {true_labels[i]}',
                  color='green' if predicted_labels[i] == true_labels[i] else 'red')
        plt.axis('off')
    plt.show()

# Mostrar 10 imágenes de prueba con las predicciones
predict_and_show_images(x_test[:10], y_test[:10])