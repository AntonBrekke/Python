import numpy as np
import matplotlib.pyplot as plt

def efield(r, qi, ri):
    Ri = r - ri
    Rinorm = np.linalg.norm(Ri)
    return qi*Ri/Rinorm**3


a = 1.0
N = 20
Q = 1.0
L = 3.0
NL = 40

x = np.linspace(-L, L, NL)
z = np.linspace(-L, L, NL)

rx, rz = np.meshgrid(x, z, indexing='xy')

Ex = np.zeros((NL, NL), float)
Ez = np.zeros((NL, NL), float)
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], 0, rz.flat[i]])
    for j in range(N):
        theta = 2*np.pi / N*j
        rj = np.array([a*np.cos(theta), a*np.sin(theta), 0])
        R = r - rj
        dq = Q/N
        dE = efield(r, dq, rj)
        Ex.flat[i] += dE[0]
        Ez.flat[i] += dE[2]

plt.quiver(rx, rz, Ex, Ez)
plt.show()
