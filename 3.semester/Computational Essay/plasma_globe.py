import numpy as np
import matplotlib.pyplot as plt
from numba import njit

@njit
def solvepoissonvonneumann3d(b, niter):
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
    Lz = b.shape[2]
    for n in range(niter):
        for ix in range(Lx):
            for iy in range(Ly):
                for iz in range(Lz):
                    ncount = 0
                    Vsum = 0
                    if np.isnan(b[ix, iy, iz]):
                        if ix > 0:
                            Vsum += V[ix-1, iy, iz]
                            ncount += 1
                        if ix < Lx-1:
                            Vsum += V[ix+1, iy, iz]
                            ncount += 1
                        if iy > 0:
                            Vsum += V[ix, iy-1, iz]
                            ncount += 1
                        if iy < Ly-1:
                            Vsum += V[ix, iy+1, iz]
                            ncount += 1
                        if iz > 0:
                            Vsum += V[ix, iy, iz-1]
                            ncount += 1
                        if iz < Lz - 1:
                            Vsum += V[ix, iy, iz+1]
                            ncount += 1
                        Vnew[ix, iy, iz] = Vsum / ncount
        V, Vnew = Vnew, V
    return V

def make_sphere_fig():
    # Making the figure
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(projection='3d', facecolor='w')
    # ax.grid(False)
    ax.xaxis.pane.fill = False; ax.set_xticklabels([])
    ax.yaxis.pane.fill = False; ax.set_yticklabels([])
    ax.zaxis.pane.fill = False; ax.set_zticklabels([])
    # Making the sphere
    I = np.linspace(0, 2*np.pi, 100)
    J = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(I, J, indexing='xy')
    px = r*np.cos(theta)*np.sin(phi) + Cx
    py = r*np.sin(theta)*np.sin(phi) + Cy
    pz = r*np.cos(phi) + Cz
    ax.plot_surface(px, py, pz, color='blue', alpha=0.08)
    ax.plot(Cx, Cy, Cz, color='k', marker='o')
    globe = (px, py, pz)
    return fig, ax

X = 80
Y = 80
Z = 80
disp_x = 0
disp_y = 0
disp_z = 0
V0 = np.zeros((X, Y, Z))
V0[:] = np.nan

r = 35
Cx = int(X/2)
Cy = int(Y/2)
Cz = int(Z/2)

V0[Cx - disp_x, Cy - disp_y, Cz - disp_z] = 0


fig, ax = make_sphere_fig()
# Setting the initial potential for a sphere
for ix in range(X):
    for iy in range(Y):
        for iz in range(Z):
            dx = ix - Cx
            dy = iy - Cy
            dz = iz - Cz
            d = np.sqrt(dx**2 + dy**2 + dz**2)
            if d < r and d >= r-3:
                # plt.plot(ix, iy, iz, marker='o')
                V0[ix, iy, iz] = -10
                if ix >= Cx - 25 and ix <= Cx - 22 and iy >= Cy-1 and iy <= Cy+1 and iz >= Cz:
                    V0[ix, iy, iz] = -2e3
                    ax.plot(ix, iy, iz, marker='o', color='red', alpha=0.3)     # plotting where I increase the potential


# Making a grid for later
x = np.linspace(X/2 - Cx, X/2 + Cx, X)
y = np.linspace(Y/2 - Cy, Y/2 + Cy, Y)
rx, ry = np.meshgrid(x, y, indexing='xy')

def get_plasma_strike_3d(animate=True):

    zeroneighbor = np.copy(V0)
    zeroneighbor[:] = 0
    zeroneighbor[Cx+1 - disp_x, Cy-1 - disp_y:Cy+1 - disp_y, Cz-1 - disp_z:Cz+1 - disp_z] = np.nan
    zeroneighbor[Cx-1 - disp_x, Cy-1 - disp_y:Cy+1 - disp_y, Cz-1 - disp_z:Cz+1 - disp_z] = np.nan
    zeroneighbor[Cx-1 - disp_x:Cx+1 - disp_x, Cy+1 - disp_y, Cz-1 - disp_z:Cz+1 - disp_z] = np.nan
    zeroneighbor[Cx-1 - disp_x:Cx+1 - disp_x, Cy-1 - disp_y, Cz-1 - disp_z:Cz+1 - disp_z] = np.nan
    zeroneighbor[Cx-1 - disp_x:Cx+1 - disp_x, Cy-1 - disp_y:Cy+1 - disp_y, Cz+1 - disp_z] = np.nan
    zeroneighbor[Cx-1 - disp_x:Cx+1 - disp_x, Cy-1 - disp_y:Cy+1 - disp_y, Cz-1 - disp_z] = np.nan

    c = np.copy(V0)
    c[:] = 0

    zexp = 5
    ns = 0
    cmap = plt.get_cmap('plasma')

    nrep = 500

    rl = 0
    np.random.seed(150)
    ix_old, iy_old, iz_old = (Cx,Cy,Cz)
    while rl < r-2:
        V = solvepoissonvonneumann3d(V0, nrep)
        prob = abs(V**zexp)
        prob = prob*np.random.uniform(0, 1, (X,Y,Z))
        prob = prob*np.isnan(zeroneighbor)
        # print(np.unravel_index(np.argmax(prob,  axis=None), prob.shape))
        [ix, iy, iz] = np.unravel_index(np.argmax(prob, axis=None), prob.shape)
        print(ix, iy, iz)
        V0[ix, iy, iz] = 0
        ir = np.sqrt((ix - Cx)**2 + (iy - Cy)**2 + (iz - Cz)**2)
        # print(ir)
        if ix > 0:
            zeroneighbor[ix-1, iy, iz] = np.nan
            zeroneighbor[ix+1, iy, iz] = np.nan
        if ix < X-1:
            zeroneighbor[ix-1, iy, iz] = np.nan
            zeroneighbor[ix+1, iy, iz] = np.nan
        if iy > 0:
            zeroneighbor[ix, iy-1, iz] = np.nan
            zeroneighbor[ix, iy+1, iz] = np.nan
        if iy < Y-1:
            zeroneighbor[ix, iy-1, iz] = np.nan
            zeroneighbor[ix, iy+1, iz] = np.nan
        if iz > 0:
            zeroneighbor[ix, iy, iz-1] = np.nan
            zeroneighbor[ix, iy, iz+1] = np.nan
        if iz < Z-1:
            zeroneighbor[ix, iy, iz-1] = np.nan
            zeroneighbor[ix, iy, iz+1] = np.nan
        ns = ns + 1
        c[ix, iy, iz] = ns
        if ir > rl:
            rl = ir
        if animate==True:
            # Visualize result
            ax.set_xlim(X/2 - Cx, X/2 + Cx); ax.set_xlabel('x')
            ax.set_ylim(Y/2 - Cy, Y/2 + Cy); ax.set_ylabel('y')
            ax.set_zlim(Z/2 - Cz, Z/2 + Cz); ax.set_zlabel('z')

            ax.plot([ix_old, ix], [iy_old, iy], [iz_old, iz], color=cmap(c[ix, iy, iz]/r), linewidth=2)
            plt.pause(0.01)
            ix_old, iy_old, iz_old = ix, iy, iz
    return V
V = get_plasma_strike_3d(animate=True)
# np.save('3dpot.npy', V)
# plt.show()

# V = np.load('3dpot.npy')
import plotly.graph_objects as go

x = np.linspace(X/2 - Cx, X/2 + Cx, X)
y = np.linspace(Y/2 - Cy, Y/2 + Cy, Y)
z = np.linspace(Z/2 - Cz, Z/2 + Cz, Z)
rx, ry, rz = np.meshgrid(x, y, z, indexing='xy')

# fig = go.Figure(data=go.Volume(
#     x = rx.flatten(),
#     y = ry.flatten(),
#     z = rz.flatten(),
#     value = V0.flatten(),
#     opacity = 0.5,
#     surface_count = 20, # number of isosurface
#     colorscale='plasma'
# ))
# fig.show()
