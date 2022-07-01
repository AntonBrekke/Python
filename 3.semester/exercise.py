import numpy as np
import matplotlib.pyplot as plt

def efield(r, q):
    if r <= a: return q*r*(1/a**3 - 1/b**3)
    if r > a and r <= b: return q*(1/a**3 - r/b**3)
    else: return 0

N = 30
L = 30
q = 10
a = 10
b = 20

I = np.linspace(-L, L, N)
rx, rz = np.meshgrid(I, I, indexing='ij')

Ex = np.zeros((N,N))
Ez = np.zeros((N,N))

for i in range(len(rx.flat)):
    r = np.sqrt(rx.flat[i]**2 + rz.flat[i]**2)
    Ex.flat[i] = efield(r, q) * rx.flat[i] / r     # rx.flat[i] / r = cos(theta)
    Ez.flat[i] = efield(r, q) * rz.flat[i] / r     # rz.flat[i] / r = sin(theta)

Ex, Ez = (Ex, Ez) / np.sqrt(Ex**2 + Ez**2)      # normaliserer 
plt.quiver(rx, rz, Ex, Ez)
plt.axis('equal')
plt.show()
