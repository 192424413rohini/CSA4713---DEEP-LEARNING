import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
p = [0.5, 0.5]
q = [0.9, 0.1]
e = entropy(p)
c = -np.sum(np.array(p)*np.log(q))
k = entropy(p, q)
print("Entropy:", round(e, 4))
print("Cross Entropy:", round(c, 4))
print("KL Divergence:", round(k, 4))
plt.bar(["Entropy", "Cross", "KL"], [e, c, k])
plt.show()
