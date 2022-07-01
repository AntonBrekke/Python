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
            V.flat[i] = 0
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


X = 80
Y = 80
V0 = np.zeros((X, Y))
V0[:] = np.nan

disp_x = 0
disp_y = 0
Cx = int(X/2)
Cy = int(Y/2)

V0[Cx - disp_x, Cy - disp_y] = 0

r = 35

# Lager sirkulært potensiale i grid
for ix in range(X):
    for iy in range(Y):
        dx = ix - Cx
        dy = iy - Cy
        d = np.sqrt(dx**2 + dy**2)
        if d < r and d >= r-1:
            V0[ix, iy] = -10
            if iy >= Cy and ix >= Cx - 25 and ix <= Cx - 22:
                V0[ix, iy] = -2e3
            # if iy >= Cy and ix <= Cx - 22 and ix >= Cx - 25:
            #     V0[ix, iy] = -2e3


fig, ax = plt.subplots()
init = ax.imshow(V0.T, cmap='plasma_r')
ax.invert_yaxis()
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(init)
plt.show()
V = solvepoissonvonneumann(V0, 2000)
Ey, Ex = np.gradient(-V.T)
plt.quiver(Ex[::2,::2], Ey[::2,::2])
plt.axis('equal')
plt.show()

theta = np.linspace(0, 2*np.pi, 200)
globe = (r*np.cos(theta) + Cx, r*np.sin(theta) + Cy)

def get_plasma_strike(V0, animate=True):
    # fig = plt.figure(figsize=(10, 5))
    # ax1 = fig.add_subplot(1,2,1)
    # ax2 = fig.add_subplot(1,2,2)

    zeroneighbor = np.copy(V0)
    zeroneighbor[:] = 0
    zeroneighbor[Cx+1 - disp_x, Cy-1 - disp_y:Cy+1 - disp_y] = np.nan
    zeroneighbor[Cx-1 - disp_x, Cy-1 - disp_y:Cy+1 - disp_y] = np.nan
    zeroneighbor[Cx-1 - disp_x:Cx+1 - disp_x, Cy+1 - disp_y] = np.nan
    zeroneighbor[Cx-1 - disp_x:Cx+1 - disp_x, Cy-1 - disp_y] = np.nan

    c = np.copy(V0)
    c[:] = 0
    # c[Cx, Cy] = 1

    zexp = 5
    ns = 0

    nrep = 500

    x = np.linspace(X/2 - Cx, X/2 + Cx, X)
    y = np.linspace(Y/2 - Cy, Y/2 + Cy, Y)
    rx, ry = np.meshgrid(x, y, indexing='xy')

    rl = 0
    np.random.seed(150)
    while rl < r:
        V = solvepoissonvonneumann(V0, nrep)
        Ey, Ex = np.gradient(-V.T)
        norm = np.sqrt(Ex**2 + Ey**2)
        Ex, Ey = (Ex, Ey) / norm
        # Ex = Ex / np.linalg.norm(Ex, axis=0)
        # Ey = Ey / np.linalg.norm(Ey, axis=0)
        prob = abs(V**zexp)
        prob = prob*np.random.uniform(0, 1, (X,Y))
        prob = prob*np.isnan(zeroneighbor)
        # print(np.unravel_index(np.argmax(prob,  axis=None), prob.shape))
        [ix, iy] = np.unravel_index(np.argmax(prob, axis=None), prob.shape)
        # print(ix, iy)
        V0[ix, iy] = 0
        ir = np.sqrt((ix - Cx)**2 + (iy - Cy)**2)
        # print(ir)
        if ix > 0:
            zeroneighbor[ix-1, iy] = np.nan
            zeroneighbor[ix+1, iy] = np.nan
        if ix < X-1:
            zeroneighbor[ix-1, iy] = np.nan
            zeroneighbor[ix+1, iy] = np.nan
        if iy > 0:
            zeroneighbor[ix, iy-1] = np.nan
            zeroneighbor[ix, iy+1] = np.nan
        if iy < Y-1:
            zeroneighbor[ix, iy-1] = np.nan
            zeroneighbor[ix, iy+1] = np.nan
        ns = ns + 1
        c[ix, iy] = ns
        if ir > rl:
            rl = ir
        # Visualize result
        if animate==True:
            ax1.cla()
            ax2.cla()
            ax1.set_xlabel('x'); ax2.set_xlabel('x')
            ax1.set_ylabel('y'); ax2.set_ylabel('y')
            ax1.imshow(c.T, cmap='plasma')
            ax1.invert_yaxis()
            cont = ax2.contourf(rx, ry, V.T, levels=10, cmap='plasma_r')
            if ns == 1 or rl >= r:
                if rl >= r:
                    cbar.remove()
                cbaxes = fig.add_axes([0.92, 0.11, 0.02, 0.77])
                cbar = fig.colorbar(cont, cax=cbaxes)
            ax2.quiver(rx[::2, ::2], ry[::2, ::2], Ex[::2, ::2], Ey[::2, ::2], scale=r)
            ax1.plot(*globe, 'k')
            ax2.plot(*globe, 'k')
            plt.pause(0.01)
    return c, V
# plt.show()

fig = plt.figure()
ax = fig.add_subplot()
V = V0
for i in range(10):
    c, V = get_plasma_strike(V, animate=False)
    where = np.where(c==0)
    c[where] = np.nan
    ax.plot(*globe, 'k')
    ax.imshow(c.T, cmap='plasma')
    ax.invert_yaxis()
plt.show()
