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

L = 100
b = np.zeros((L,L))
b[:] = np.float('nan')

x0 = int(0.25*L)
x1 = int(0.75*L)
y0 = int(0.25*L)
y1 = int(0.30*L)

for ix in range(x0, x1):
    for iy in range(y0, y1):
        b[ix, iy] = 0.5

x0 = int(0.25*L)
x1 = int(0.75*L)
y0 = int(0.70*L)
y1 = int(0.75*L)

for ix in range(x0, x1):
    for iy in range(y0, y1):
        b[ix, iy] = -0.5

V = solvepoissonvonneumann(b, 10000)

plt.contourf(V)
plt.show()

Ey, Ex = np.gradient(-V)
x = np.linspace(0, L-1, L)
y = np.linspace(0, L-1, L)
rx, ry = np.meshgrid(x, y, indexing='xy')
plt.streamplot(rx, ry, Ex, Ey)
plt.show()

# Capacitnace-part missed, check lecture notes
