import numpy as np
import matplotlib.pyplot as plt
from numba import njit

@njit
def solvepoissonvonneumann(b, niter):
    # b: Matrise med randverdier, NaN hvor vi skal finne V
    # niter: antall iterasjoner
    # V: returnerer potensialet
    # Tar hensyn til Von Neumann - betingelser
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
                ncount = 0
                Vsum = 0
                if np.isnan(b[ix, iy]):
                    if ix > 0:
                        Vsum += V[ix-1, iy]
                        ncount += 1
                    if ix < Lx-1:
                        Vsum += V[ix+1, iy]
                        ncount += 1
                    if iy > 0:
                        Vsum += V[ix, iy-1]
                        ncount += 1
                    if iy < Ly-1:
                        Vsum += V[ix, iy+1]
                        ncount += 1
                    Vnew[ix, iy] = Vsum / ncount
        V, Vnew = Vnew, V
    return V

# Må definere grenseverdier
L = 50
b = np.zeros((L,L))

a = L*0.3
cx = L/2
cy = L/2

for ix in range(L):
    for iy in range(L):
        dx = ix - cx
        dy = iy - cy
        d = np.sqrt(dx**2 + dy**2)
        if d < a:
            b[ix, iy] = np.float('nan')

b[int(0.65*L), int(0.6*L)] = 1.0

imb = plt.imshow(b)
plt.colorbar(imb)
plt.show()

V = solvepoissonvonneumann(b, 2000)
plt.contourf(V)
plt.axis('equal')
plt.show()

Ey, Ex = np.gradient(-V)
x = np.linspace(0, L-1, L)
y = np.linspace(0, L-1, L)
rx, ry = np.meshgrid(x, y, indexing='xy')
plt.quiver(rx, ry, Ex, Ey)
plt.axis('equal')
plt.show()

plt.streamplot(x, y, Ex, Ey)
plt.show()
