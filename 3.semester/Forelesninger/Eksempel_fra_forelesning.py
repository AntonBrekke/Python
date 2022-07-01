import numpy as np
import matplotlib.pyplot as plt

def epotlist(r, Q, R):
    """
    r er en posisjon i rommet
    Q er en liste med ladninger
    R er en liste med posisjoner for ladninger
    """
    V = 0
    for j in range(len(Q)):
        Qi = Q[j]
        Ri = R[j]
        Rnorm = np.linalg.norm(r - Ri)
        V += Qi / Rnorm
    return V

# ri = (a/2, -d/2 + d/(2N + id/N) Høyre
# ri = (-a/2, -d/2 + d/(2N + id/N) Venstre

Qlist = []
Rlist = []
N = 100
a = 1e-2
d = a
Q = 1
for i in range(N):
    # Høyre
    xi = a/2
    yi = -d/2 + d/(2*N) + i*d/N
    Qi = Q/N
    Qlist.append(Qi)
    Rlist.append(np.array([xi, yi, 0]))
for i in range(N):
    # Venstre
    xi = -a/2
    yi = -d/2 + d/(2*N) + i*d/N
    Qi = -Q/N
    Qlist.append(Qi)
    Rlist.append(np.array([xi, yi, 0]))

# Ide er xi, yi på et gitter finn V[xi, yi]
L = 5e-2
NL = 50
x = np.linspace(-L, L, NL)
y = np.linspace(-L, L, NL)

rx, ry = np.meshgrid(x, y, indexing='ij')
V = np.zeros((NL, NL))
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], ry.flat[i], 0])
    V.flat[i] = epotlist(r, Qlist, Rlist)

Ex, Ey = np.gradient(-V)
plt.contourf(rx, ry, V)
plt.quiver(rx, ry, Ex, Ey)
plt.show()

dx = 0.00001
x = np.linspace(a/2 + dx, 1000, 10000)
Vs = np.zeros(x.shape)
for i in range(len(x)):
    r = np.array([x[i], 0, 0])
    Vs[i] = epotlist(r, Qlist, Rlist)

plt.loglog(x, Vs)
plt.show()
# Eller
xlog = np.log10(x)
Vslog = np.log10(Vs)
plt.plot(xlog, Vslog)
plt.show()
p = np.polyfit(xlog, Vslog, 1)
print(p)
