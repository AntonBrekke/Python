import numpy as np
import matplotlib.pyplot as plt

plt.axis([-2,2,-20,20])

x = np.linspace(-2,2,100)

lines = plt.plot(x,x)
plt.title("y = x")
plt.pause(0.5)

for k in range(2,21):
    lines[0].set_ydata(x**k)
    plt.title(f"y = x^{k}")
    plt.draw()
    plt.pause(0.5)
