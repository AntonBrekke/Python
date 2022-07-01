import numpy as np
import matplotlib.pyplot as plt

# Ringladning
def epotlist(r, Q, R):
    V = 0
    for i in range(len(R)):
        Ri = r - R[i]
        Qi = Q[i]
        Rinorm = np.linalg.norm(Ri)
        V += Qi / Rinorm

    return V

# Lage ring
Q = []
R = []
M = 100
a = 2
q = 1
deltatheta = 2*np.pi/M
for i in range(M):
    thetai = i*deltatheta
    xi = a*np.cos(thetai)
    yi = a*np.sin(thetai)
    ri = np.array([xi, yi, 0])
    R.append(ri)
    Qi = q / M
    Q.append(Qi)

Lx = 5
Lz = 5
N = 30
x = np.linspace(-Lx, Lx, N)
z = np.linspace(-Lz, Lz, N)
rx, rz = np.meshgrid(x, z, indexing='ij')

V = np.zeros((N, N), float)
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], 0, rz.flat[i]])
    V.flat[i] = epotlist(r, Q, R)

plt.contourf(rx, rz, V)
plt.colorbar()
plt.show()

Ex, Ez = np.gradient(-V)
plt.contourf(rx, rz, V)
plt.quiver(rx, rz, Ex, Ez)
plt.show()
