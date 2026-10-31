from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
filters = [8, 16]
params = []
for f in filters:
    m = models.Sequential([
        layers.Input(shape=(28,28,1)),
        layers.Conv2D(f, (3,3), activation='relu'),
        layers.Flatten(),
        layers.Dense(10, activation='softmax')
    ])
    params.append(m.count_params())
    print("Filters:", f, "Parameters:", m.count_params())
plt.bar(filters, params)
plt.xlabel("Filters")
plt.ylabel("Parameters")
plt.title("CNN Comparison")
plt.show()
