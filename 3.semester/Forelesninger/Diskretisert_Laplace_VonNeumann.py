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
    Ly = b.shape[1]
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
L = 100
L14 = int(L/4)
L34 = int(3*L/4)
b = np.zeros((L,L))
b[:] = np.float('nan')
b[int(L/4),L14:L34] = -1.0
b[int(3*L/4),L14:L34] = 1.0       # Kan også bruke L-1 istedet for -1 på indeks


V = solvepoissonvonneumann(b, 2000)

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
plt.quiver(rx[::2, ::2], ry[::2, ::2], Ex[::2, ::2], Ey[::2, ::2])
plt.colorbar(plot)
stream = plt.streamplot(rx, ry, Ex, Ey, color=field_strength, cmap='plasma_r')
plt.colorbar(stream.lines)
# plt.axis('equal')
plt.show()
