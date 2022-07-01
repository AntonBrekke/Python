import numpy as np
import matplotlib.pyplot as plt

a = 1
I = np.linspace(-5, 5)
J = np.linspace(0, 5)

x, z = np.meshgrid(I, J, indexing='xy')

vx = a*np.sqrt(z)
vz = np.zeros_like(vx)

plt.quiver(x[::2, ::2], z[::2, ::2], vx[::2, ::2], vz[::2, ::2], np.sqrt(vx**2 + vz**2)[::2, ::2], cmap='jet')
# plt.streamplot(x, z, vx, vz, color=np.sqrt(vx**2 + vz**2), cmap='jet')
# Alternativt 
C = np.linspace(0, 5, 5)
x = np.linspace(-5, 5, 300)
for C in C:
    z = (3*C/(2*a))**(2/3)
    plt.plot(x, np.broadcast_to(z, np.shape(x)), 'b--')
plt.show()
