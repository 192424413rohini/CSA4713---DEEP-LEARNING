import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
m = models.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(8, activation='relu',
    kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid')
])
m.compile(optimizer='adam', loss='binary_crossentropy')
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 1, 1, 0])
m.fit(X, y, epochs=5, verbose=0)
print("Training Completed")
