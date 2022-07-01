import numpy as np
import matplotlib.pyplot as plt
from numba import njit

# @njit(cache=True)
def bfield(r, rlist, dlist):
    B = np.array([0,0,0])
    for i in range(len(rlist)):
        ri = rlist[i]
        dli = dlist[i]
        R = r - ri
        Rnorm = np.linalg.norm(R)
        dB = np.cross(dli, R) / Rnorm**3
        B = B + dB

    return B

N = 100
a = 2
dl = 2*np.pi*a/N
rlist = []
dlist = []

# Setter opp listene
for i in range(N):
    thetai = i/N*2*np.pi
    ri = np.array([a*np.cos(thetai), a*np.sin(thetai), 0])
    rlist.append(ri)
    dli = np.array([-dl*np.sin(thetai), dl*np.cos(thetai), 0])
    dlist.append(dli)

for i in range(N):
    ri = rlist[i]
    plt.plot(ri[0], ri[1], 'ob')

plt.axis('equal')
plt.show()

L = 5
NL = 20

x = np.linspace(-L, L, NL)
z = np.linspace(-L, L, NL)

rx, rz = np.meshgrid(x, z, indexing='xy')

Bx = rx.copy()
Bz = rz.copy()

for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], 0, rz.flat[i]])
    Bx.flat[i], By, Bz.flat[i] = bfield(r, rlist, dlist)

plt.streamplot(x, z, Bx,Bz)
plt.show()


fig = plt.figure(figsize=(7,7))
Bmag = np.sqrt(Bx**2 + Bz**2)
uBx = Bx/Bmag
uBz = Bz/Bmag
Bcolor = np.log10(Bmag)
plt.quiver(rx, rz, uBx, uBz, Bcolor, cmap='jet')
plt.show()
