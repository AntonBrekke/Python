import numpy as np
import matplotlib.pyplot as plt

# Elektrisk dipol
def epotlist(r, Q, R):
    """
    Regner i enheter 1/(4*pi*epsilon_0)
    (eller antar at den er 1)
    """
    V = 0
    for i in range(len(R)):
        Ri = r - R[i]
        Qi = Q[i]
        Rinorm = np.linalg.norm(Ri)
        V += Qi/Rinorm

    return V

R = []
Q = []
r1 = np.array([1,0])
Q1 = 1
R.append(r1)
Q.append(Q1)
r2 = np.array([-1,0])
Q2 = -1
R.append(r2)
Q.append(Q2)

Lx = 3
Ly = 3
N = 21
x = np.linspace(-Lx, Lx, N)
y = np.linspace(-Ly, Ly, N)
rx, ry = np.meshgrid(x, y, indexing='xy')
V = np.zeros((N,N), float)
# Finne verdier for elektrisk potensial på grid
for i in range(np.size(rx)):
    r = np.array([rx.flat[i], ry.flat[i]])
    V.flat[i] = epotlist(r, Q, R)

plt.imshow(V)
plt.colorbar()
plt.show()

plt.contourf(rx, ry, V, levels=20)
plt.colorbar()
plt.show()

# Finner elektrisk felt
Ex = np.gradient(V, axis=1)
Ey = np.gradient(V, axis=0)
Ex, Ey = -Ex, -Ey
plt.contourf(rx, ry, V, levels=20)
plt.quiver(rx, ry, Ex, Ey)
plt.show()
