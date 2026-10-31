import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 0])
w = np.array([0.5, 0.5])
y = np.dot(x, w) + 0.2
print("Output:", y)
plt.bar(["X1", "X2"], x)
plt.title("Perceptron Input")
plt.show()
