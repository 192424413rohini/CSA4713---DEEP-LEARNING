import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 0])
w = np.array([0.5, 0.5])
y = np.dot(x, w)
error = 1 - y
w = w + 0.1 * error * x
print("Output:", y)
print("Updated Weights:", w)
plt.bar(["W1", "W2"], w)
plt.title("Updated Weights")
plt.show()
