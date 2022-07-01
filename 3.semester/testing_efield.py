import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

epsilon_0 = sc.epsilon_0

def efield(r, qi, ri):
    Ri = r - ri
    Rinorm = np.linalg.norm(Ri)
    return qi/(4*np.pi*epsilon_0) * Ri/Rinorm**3


a = 1.0
N = 20
Q = 1.0e-8
L = 1.5
NL = 9

x = np.linspace(-L, L, NL)
y = np.linspace(-L, L, NL)
z = np.linspace(-L, L, NL)

rx, ry, rz = np.meshgrid(x, y, z, indexing='ij')

Ex = np.zeros((NL, NL, NL), float)
Ey = np.zeros((NL, NL, NL), float)
Ez = np.zeros((NL, NL, NL), float)
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], ry.flat[i], rz.flat[i]])
    for j in range(N):
        theta = 2*np.pi / N*j
        r1 = np.array([a*np.cos(theta), a*np.sin(theta), -a/2])
        dq1 = Q/N
        dE1 = efield(r, dq1, r1)
        r2 = np.array([a*np.cos(theta), a*np.sin(theta), a/2])
        dq2 = -Q/N
        dE2 = efield(r, dq2, r2)
        Ex.flat[i] += dE1[0] + dE2[0]
        Ey.flat[i] += dE1[1] + dE2[1]
        Ez.flat[i] += dE1[2] + dE2[2]
"""
# Sjekk med kode fra forelesning om dette stemmer med NL = 40
# og kun legge sammen dE1[0]
C = int(np.ceil((NL - 1)/2))    # Velger indeksen som gir oss planene gjennom origo
plt.quiver(rx[:,C], rz[C], Ex[:,C], Ez[C])
plt.show()
plt.quiver(ry[C], rz[C], Ey[C], Ez[C])
plt.show()
plt.quiver(rx[:,C], ry[C].T, Ex[:,C], Ey[C].T)
plt.show()
"""
# Ser riktig ut
# Videre til å plotte i 3D:
"""
# Må gjøre dette for å få laget med cmap på 3D-quiver
k = np.sqrt(Ex**2 + Ey**2 + Ez**2)
# Flatten and normalize
c = np.ravel(k) / np.ptp(k)     # Ravel flater ned dimensjonene til en array
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))        # Gjentar c 2 ganger og konkatenerer så lista ikke går tom for verdier
c = plt.cm.jet(c)

# print(np.ptp(c) == np.max(c) - np.min(c))     # Returnerer True, ptp - peak to peak

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
len = 1 / (1.5*np.max(np.sqrt(Ex**2 + Ey**2 + Ez**2)))
quiver_3d = ax.quiver(rx, ry, rz, Ex, Ey, Ez, colors=c, cmap='jet', length=len, arrow_length_ratio=0.5)
cbar = fig.colorbar(quiver_3d, ax=ax)
# Få på plass riktige verdier på cbar
rnd = lambda t: round(t, 3)
N = 10
cbar.set_ticks(np.linspace(0, 1, N))
cbar.set_ticklabels([*map(rnd, np.linspace(np.min(k), np.max(k), N))])
plt.show()
"""
