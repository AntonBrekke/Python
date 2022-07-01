import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(1, 2, 30)
J = np.linspace(-1,1, 30)
x, y = np.meshgrid(I, J, indexing='xy')

T0 = 2

grad_Tx = -T0*y
grad_Ty = -T0*x

plt.quiver(x[::2, ::2], y[::2, ::2], grad_Tx[::2, ::2], grad_Ty[::2, ::2])

T = T0*(2 - x*y)
plt.contour(x, y, T, 20, cmap='jet')

x = np.linspace(1, 2, 600)
h = 1/x
plt.plot(x, h, 'r', x, -h, 'r', linewidth=10)

plt.show()
