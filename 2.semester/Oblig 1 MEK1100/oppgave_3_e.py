import numpy as np
import matplotlib.pyplot as plt

"""
Sammenlikner potensialet cos(x)cos(y)
med annen ordens Taylor-approksimasjon rundt punktet
(0,0)
"""

I = np.linspace(-np.pi/2, np.pi/2, 101)
x, y = np.meshgrid(I, I, indexing='xy')

N = 30

z = np.cos(x)*np.cos(y)
T2 = 1- 0.5*x**2 - 0.5*y**2
fig, ax = plt.subplots(1,2, sharey=True)
ax[0].contour(x, y, z, N); ax[0].axis('equal')
ax[0].set_xlabel('x'); ax[0].set_ylabel('y')
ax[0].set_title(r'$\psi = cos(x)cos(y) = C$')
ax[1].contour(x, y, T2, N); ax[1].axis('equal')
ax[1].set_xlabel('x'); ax[1].set_ylabel('y')
ax[1].set_title(r'$T_2 = 1-\frac{1}{2}x^2 - \frac{1}{2}y^2 = C$')
# plt.savefig('oppgave_3_e_contour.png')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(x, y, np.cos(x)*np.cos(y), rstride=1, cstride=1, cmap=plt.cm.jet, linewidth=0, antialiased=False)
surf = ax.plot_wireframe(x, y, z, color='k', label=r'$\psi = cos(x)cos(y)$')
surf2 = ax.plot_surface(x, y, T2, rstride=1, cstride=1, cmap=plt.cm.jet, linewidth=0, antialiased=False)
ax.set_title(r'Taylor approximation: $1 - \frac{1}{2}x^2 - \frac{1}{2}y^2\;,\;(a,b)=(0,0)$')
ax.set_xlabel('x'); ax.set_ylabel('y')
cbar_ax = fig.add_axes([0.1, 0.2, 0.025, 0.6])
cbar = fig.colorbar(surf2, cax=cbar_ax)
cbar.set_label('Second degree Taylor approximation')
ax.grid(True)
ax.legend()

# plt.savefig('oppgave_3_e_3Dplot.png')
plt.show()
