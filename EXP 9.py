import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
X = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 1, 1, 0]
m = MLPClassifier(hidden_layer_sizes=(4,),
                  max_iter=5000, random_state=1)
m.fit(X, y)
p = m.predict(X)
print("Prediction:", p)
plt.plot(y, 'o-', label="Actual")
plt.plot(p, 's--', label="Predicted")
plt.legend()
plt.show()
