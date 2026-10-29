import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
X = [[1], [2], [3], [4], [5]]
y = [1, 4, 9, 16, 25]
m = DecisionTreeRegressor(max_depth=1)
m.fit(X, y)
p = m.predict(X)
print("Predicted:", p)
plt.plot(y, 'o-', label="Actual")
plt.plot(p, 's--', label="Predicted")
plt.legend()
plt.show()
