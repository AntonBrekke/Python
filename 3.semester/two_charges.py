import numpy as np
import matplotlib.pyplot as plt

def efield(r, ri, qi):
    Ri = r - ri
    Ri_norm = np.linalg.norm(Ri)
    return Ri*qi/Ri_norm**3
a = 1
q1 = 10
r1 = np.array([-a, 0])
q2 = 10
r2 = np.array([a, 0])

N = 40
I = np.linspace(-3, 3, N)
rx, ry = np.meshgrid(I, I, indexing='ij')
Ex = np.zeros((N,N))
Ey = np.zeros((N,N))

for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], ry.flat[i]])
    Ex.flat[i], Ey.flat[i] = efield(r, r1, q1) + efield(r, r2, q2)

norm = np.sqrt(Ex**2 + Ey**2)
Ex, Ey = (Ex, Ey) / norm
plt.quiver(rx[::2, ::2], ry[::2, ::2], Ex[::2, ::2], Ey[::2, ::2])
plt.show()
