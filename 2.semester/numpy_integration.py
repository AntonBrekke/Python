import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
x = np.arange(0, 2, dx)

f = x
# Denne er tydeligivis bittelitt mer presis enn trapesmetoden
int_f = np.sum(f, axis=0)*dx

func = lambda x: np.sin(x)

# Trapesmetoden
def int(f, a, b, N):
    x = np.linspace(a, b, N+1)
    dx = np.diff(x, axis=0)
    f = f(x)
    s = 0
    for i in range(0, len(f)-1):
        s += (f[i] + f[i+1])*dx[i] / 2
        plt.plot(x[i], s, 'ro', markersize=3)
    plt.show()
    return s

"""
Feilen i trapesmetoden kan uttrykkes som
E(dx) = (b-a)^3/(12n^2) * M
der n er antall steg, (a,b) er intervallet og M >= |f''(x)|
for alle x i intervallet (a,b).
F. eks blir feilen med trapesmetoden for sin(x) i intervallet (0, pi) med 500 steg ca.:
(pi - 0)^3/(12*(500^2))*1 = E(dx) = 1.033e-5
som stemmer godt (analytisk svar = 2, numerisk = 1.9999934202594032)
"""

# print(int_f)
def int_dx(f, a, b, dx):
    """
    Ulempen med denne er at jeg ikke får plottet den
    """
    x = np.arange(a, b, dx)
    f = f(x)
    s = np.sum(f, axis=0)*dx
    return s

# print(int_dx(func, a=1, b=4, dx=0.001))
#
# print(int(func, a=0, b=np.pi, N=1000))


x = np.linspace(0, 5, 501)[:,None]
y = np.linspace(0, 5, 501)[None,:]

def int_2D(f, t, axis):
    if axis == 'x':
        axis = 0
    elif axis == 'y':
        axis = 1
    else:
        raise IndexError("axis must be 'x' or 'y'")
    dt = np.sum(np.diff(t, axis=axis), axis=axis) / (np.size(t) - 1)
    int = np.sum(f, axis=axis)*dt
    return int

f = lambda x, y: x**2 - y**2

print(int_2D(f(x,y), x, axis='x'))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, f(x,y), cmap='jet')
plt.show()
