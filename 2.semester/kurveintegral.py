import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.vector import CoordSys3D

ax = plt.axes(projection='3d')
ti = np.linspace(0, 1, 100)
ax.plot3D(ti, ti, 2*ti**1.5)
# plt.show()

t = sp.Symbol('t', real=True)
N = CoordSys3D('N')
r = t*N.i + t*N.j + 2*t**1.5*N.k        # Gir resultat med flyttall
# r = t*N.i + t*N.j + 2*t**sp.Rational(3,2)*N.k   #Alternativt, uttrykker med rotsymbolet

drdt = r.diff(t, 1)
# print(drdt)
a = sp.integrate(sp.sqrt(drdt.dot(drdt)), (t, 0, 1))
print(a)
