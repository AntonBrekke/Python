import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-3, 3, 101)

x, y = np.meshgrid(I, I, indexing='xy')

stream = np.log(x**2 + y**2)

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.contour(x, y, stream, 30)
ax2.contour(x, y, 0.5*stream, 30)
plt.show()
