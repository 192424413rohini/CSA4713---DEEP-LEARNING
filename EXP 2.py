import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'X': [2, 4, 6, 8],
    'Y': [1, 3, 5, 7]
})
print("Dataset:")
print(data)
cov = data.cov()
print("\nCovariance Matrix:")
print(cov)
values, vectors = np.linalg.eig(cov)
print("\nEigenvalues:")
print(values)
print("\nEigenvectors:")
print(vectors)
plt.scatter(data['X'], data['Y'])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Covariance Data Visualization")
plt.show()
