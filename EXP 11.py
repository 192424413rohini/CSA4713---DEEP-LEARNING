import tensorflow as tf
from tensorflow.keras import layers, models
m = models.Sequential([
    layers.Input(shape=(28,28,1)),
    layers.Conv2D(8, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(10, activation='softmax')
])
m.compile(optimizer='adam',
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])
print("CNN Model Created")
