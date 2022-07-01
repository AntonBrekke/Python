import numpy as np
import matplotlib.pyplot as plt

def efield(r, qi, ri):
    # 1 / 4*pi*epsilon_0 = 1
    Ri = r - ri
    Rinorm = np.linalg.norm(Ri)
    return qi*Ri/Rinorm**3


q1 = 1.0
r1 = np.array([0,0])
q2 = 1.0
r2 = np.array([1,0])
r = np.array([2,0])

N = 20
L = 2
I = np.linspace(-L, L, N)
rx, ry = np.meshgrid(I, I, indexing='xy')

Ex = np.zeros([N, N], float)
Ey = np.zeros([N, N], float)
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], ry.flat[i]])
    Ex.flat[i], Ey.flat[i] = efield(r, q1, r1) + efield(r, q2, r2)

plt.quiver(rx, ry, Ex, Ey)
plt.axis('equal')
plt.show()

d = 1
x = np.linspace(d, 100, 1000)
E = 1 / (x-d/2)**2 - 1 / (x+d/2)**2
plt.plot(x, E)
plt.show()
plt.loglog(x, E)
plt.show()

logx = np.log10(x)
logE = np.log10(E)
j = np.where(logx>0.25)
plt.plot(logx[j], logE[j])
plt.show()
pol = np.polyfit(logx[j], logE[j], 1)
logfit = np.poly1d(pol)
plt.plot(logx, logE, '.r', logx, logfit(logx), ':b')
plt.show()
print(pol)
