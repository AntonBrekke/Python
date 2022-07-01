import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-3, 3, 40)
x, y = np.meshgrid(I, I, indexing='xy')

plt.quiver(x[::2, ::2], y[::2, ::2], x[::2, ::2], y[::2, ::2], np.sqrt(x**2 + y**2)[::2, ::2], cmap='jet')
plt.show()
