import numpy as np
import matplotlib.pyplot as plt
from numba import njit

@njit
def solvepoisson(b, niter):
    # b: Matrise med randverdier, NaN hvor vi skal finne V
    # niter: antall iterasjoner
    # V: returnerer potensialet
    # Tar ikke hensyn til Von Neumann - betingelser
    V = b.copy()
    for i in range(len(V.flat)):
        if np.isnan(b.flat[i]):
            V.flat[i] = 0.0
    Vnew = V.copy()
    Lx = b.shape[0]
    Ly = b.shape[0]
    for n in range(niter):
        for ix in range(Lx):
            for iy in range(Ly):
                if np.isnan(b[ix, iy]):
                    Vnew[ix, iy] = 1/4*(V[ix + 1, iy] + V[ix - 1, iy] + V[ix, iy + 1] + V[ix, iy - 1])
        V, Vnew = Vnew, V
    return V

# Må definere grenseverdier
L = 40
b = np.zeros((L,L))
b[:] = np.float('nan')
b[0,:] = 0.0
b[-1,:] = 0.0       # Kan også bruke L-1 istedet for -1 på indeks
b[:,0] = 1.0
b[:,-1] = 0.0

V = solvepoisson(b, 2000)

plt.imshow(b)
plt.colorbar()
plt.show()
plt.contourf(V, 200)
plt.colorbar()
plt.show()

Ey, Ex = np.gradient(-V)
x = np.linspace(0, L-1, L)
y = np.linspace(0, L-1, L)
field_strength = np.sqrt(Ex**2 + Ey**2)

rx, ry = np.meshgrid(x,y, indexing='xy')
plot = plt.contourf(rx, ry, V, levels=200, cmap='plasma')
plt.quiver(rx, ry, Ex, Ey)
plt.colorbar(plot)
stream = plt.streamplot(rx, ry, Ex, Ey, color=field_strength, cmap='plasma_r')
plt.colorbar(stream.lines)
plt.axis('equal')
plt.show()
