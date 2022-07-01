import numpy as np
import matplotlib.pyplot as plt
from numba import njit

@njit
def solvepoisson(Vb, nrep):
    V = np.copy(Vb)
    for i in range(len(V.flat)):
        if (np.isnan(Vb.flat[i])):
            V.flat[i] = 0
    Vnew = np.copy(V)
    Lx = Vb.shape[0]
    Ly = Vb.shape[1]
    for n in range(nrep):
        for ix in range(Lx):
            for iy in range(Ly):
                pot = 0
                if np.isnan(Vb[ix,iy]):
                    ix1 = ix + 1
                    if (ix1 > Lx-1):
                        ix1 = 0
                    pot = pot + V[ix1, iy]
                    ix1 = ix - 1
                    if (ix1 < 0):
                        ix1 = Lx - 1
                    pot = pot + V[ix1, iy]
                    iy1 = iy + 1
                    if (iy1 > Ly-1):
                        iy1 = 0
                    pot = pot + V[ix, iy1]
                    iy1 = iy - 1
                    if (iy1 < 0):
                        iy1 = Ly - 1
                    pot = pot + V[ix, iy1]
                    Vnew[ix, iy] = pot/4
                else:
                    Vnew[ix, iy] = V[ix, iy]
        V, Vnew = Vnew, V
    return V

Lx = 50
Ly = 50
Vb = np.zeros((Lx, Ly))
c = np.copy(Vb)
Vb[:] = np.float('nan')
# Toppen
Vb[:, Ly-1] = 0
# Bunnen
Vb[:, 0] = 1

zeroneighbor = np.copy(Vb)
zeroneighbor[:] = 0
zeroneighbor[:, -20] = np.float('nan')

nrep = 500
zexp = 0.25
ymin = Ly - 1
ns = 0

# Dynamic visualization
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

np.random.seed(10)
while (ymin > 0):
    V = solvepoisson(Vb, nrep)
    prob = V**zexp
    prob = prob*np.random.uniform(0, 1, (Lx, Ly))
    prob = prob*np.isnan(zeroneighbor)
    [ix, iy] = np.unravel_index(np.argmax(prob, axis=None), prob.shape)
    Vb[ix, iy] = 0
    if (ix > 0):
        zeroneighbor[ix-1, iy]=np.float('nan')
    if (ix < Lx-1):
        zeroneighbor[ix+1, iy]=np.float('nan')
    if (iy > 0):
        zeroneighbor[ix, iy-1]=np.float('nan')
    if (iy < Ly-1):
        zeroneighbor[ix, iy-1]=np.float('nan')
    ns = ns + 1
    c[ix, iy] = ns
    if (iy < ymin):
        ymin = iy
    # Visualize result
    # ax1.cla()
    # ax2.cla()
    ax1.contourf(c.T, cmap='viridis')
    ax2.contourf(V.T, levels=10, cmap='viridis')
    plt.pause(0.01)
plt.show()
