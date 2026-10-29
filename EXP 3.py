from scipy.stats import binom
import matplotlib.pyplot as plt
n = int(input("Enter trials: "))
p = float(input("Enter probability: "))
x = range(n + 1)
y = binom.pmf(x, n, p)
print("Probabilities:", y)
plt.bar(x, y)
plt.xlabel("Successes")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.show()
