import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

Nx = 100
Ny = 100
Nt = 5e4

Lx = 5
Ly = 5
time = 10
dx = Lx / Nx
dy = Ly / Ny
dt = time / Nt

T1 = 295     # K
T0 = 400      # K
a = 1
# kappa = 10

X = np.linspace(-Lx, Lx, Nx)
Y = np.linspace(-Ly, Ly, Ny)
T = np.linspace(0, 10, int(Nt))

x, y = np.meshgrid(X, Y, indexing='ij')

sol = np.zeros((int(Nt), Nx, Ny))
sol[0:1] = T0*np.exp(-a*(x**2 + y**2))

# Plotter initialbetingelse
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, sol[0] + T1, cmap='hot')
plt.show()

@njit
def solve_heateq(solve_array, Nx, Ny, Nt, dx, dy, dt):
    T = solve_array.copy()
    kappa = 1
    for i in range(0, int(Nt)-1):
        for j in range(1, Nx-1):
            for k in range(1, Ny-1):
                x_part = (T[i,j+1,k] - 2*T[i,j,k] + T[i,j-1,k]) / dx**2
                y_part = (T[i,j,k+1] - 2*T[i,j,k] + T[i,j,k-1]) / dy**2
                T[i+1,j,k] = T[i,j,k] + dt*kappa*(x_part + y_part)
    return T

T_sol = solve_heateq(sol, Nx, Ny, Nt, dx, dy, dt) + T1
print('k')

minz = np.min(T_sol)
maxz = np.max(T_sol)
maxx = np.max(x)
maxy = np.max(y)

C = (0.15, 0.15, 0.15)
fig = plt.figure(facecolor=C)
ax = fig.add_subplot(projection='3d')

theta = np.linspace(0, np.pi, 300)
phi = np.linspace(0, 2*np.pi, 300)
theta, phi = np.meshgrid(theta, phi, indexing='ij')
R = Lx

rx = R*np.sin(theta)*np.cos(phi)
ry = R*np.sin(theta)*np.sin(phi)
rz = np.cos(theta) * maxz / 2

def update(frame):
    ax.cla()
    # ax.axis('off')        # Skrur av alle akser
    ax.grid(color='w')      # Fjerner grid (trenger ikke hvis ax.axis('off') er på)
    ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
    ax.tick_params(axis='y', colors='w')    # Setter ticks hvit
    ax.tick_params(axis='z', colors='w')    # Setter ticks hvit
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.line.set_color('w')
    ax.yaxis.line.set_color('w')
    ax.zaxis.line.set_color('w')
    ax.set_zlim(minz, maxz)
    ax.set_facecolor(C)       # Setter farge rundt plott til svart
    plot = ax.plot_surface(x, y, T_sol[40*frame, :, :], cmap='hot')
    plot2 = ax.plot_surface(rx, ry, rz + T1, color='w', alpha=0.2)
    # timelabel = ax.text(0.8*maxx, 0.8*maxy, maxz, f't={t[frame]:.1f}', fontsize=16, color='w', weight='bold')

ani = FuncAnimation(fig, update, frames=int(Nt), interval=10, blit=False)

plt.show()
