import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-1,1,20)
xi, yi = np.meshgrid(I, I, indexing='ij')
plt.quiver(xi, yi, -yi, xi) # Vektorfelt
plt.contour(xi,yi,xi**2 + yi**2, 8) # Strømlinjer
plt.axis('equal')
# plt.show()
plt.clf()


import sympy as sp
from sympy.vector import CoordSys3D

x, y = sp.symbols('x, y', real=True)
omega = sp.Symbol('omega', real=True)
N = CoordSys3D('N')
u = -N.y*omega*N.i + N.x*omega*N.j
r = N.x*N.i + N.y*N.j
# print(r.cross(u))
w = omega*N.k
# print(w.cross(r))

# Tre virvler

beta = (sp.exp(-((x-3*sp.pi/4)**2 + (y-sp.pi/2)**2))
+sp.exp(-((x-3*sp.pi/4)**2+(y-3*sp.pi/2)**2))
-sp.exp(-((x-3*sp.pi/2)**2+(y-3*sp.pi/2)**2))/2)

I = np.linspace(0, 2*np.pi, 100)
xi, yi = np.meshgrid(I, I, indexing='ij')
betai = sp.lambdify((x,y), beta)(xi, yi)
plt.contourf(xi, yi, betai, 100)
# plt.show()
plt.clf()

z = (-0.4, -0.2, -0.05, -0.01, 0, 0.01, 0.05, 0.2, 0.4, 0.8)
CS = plt.contour(xi, yi, betai, z)
plt.clabel(CS, inline=1, fontsize=8, fmt='%1.3f', colors='k')
# plt.show()
plt.clf()

dbeta_x = beta.diff(x, 1)   # Sympy modul partiellderivasjon
dbeta_y = beta.diff(y, 1)
u = dbeta_x*N.j - dbeta_y*N.i
# print(u)
# Må evaluere Sympy funksjonen u på meshet mitt og plotte med quiver
dbx = sp.lambdify((x,y), dbeta_x)(xi,yi)
dby = sp.lambdify((x,y), dbeta_y)(xi, yi)
CS = plt.contour(xi, yi, betai, 15)
plt.quiver(xi[::4, ::4], yi[::4, ::4], dby[::4, ::4], -dbx[::4, ::4])
plt.axis('equal')
plt.show()
plt.clf()
