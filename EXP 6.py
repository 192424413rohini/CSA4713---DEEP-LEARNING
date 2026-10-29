import matplotlib.pyplot as plt
x, lr = 5, 0.1
gd = x - lr * 2*x
sgd = x - lr * 2*x
momentum = x - lr * 2*x
adam = x - lr
v = [gd, sgd, momentum, adam]
print("GD, SGD, Momentum, Adam:", v)
plt.bar(["GD", "SGD", "Momentum", "Adam"], v)
plt.ylabel("Updated Value")
plt.show()
