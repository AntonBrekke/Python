import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-np.pi, np.pi, 50)
x, y = np.meshgrid(I, I, indexing='xy')

U = np.sin(y)   # x = 0, (sin(y), 0)
V = -np.sin(x)  # y = 0, (0, -sin(x))

"""
fig, ax = plt.subplots(1,2)
ax[0].quiver(np.zeros_like(x)[::2, ::2], y[::2, ::2], U[::2, ::2], np.zeros_like(V)[::2, ::2], angles='xy', scale_units='xy', scale=1)
ax[0].set_xlim(np.min(U)*1.3, np.max(U)*1.3)
ax[1].quiver(x[::2, ::2], np.zeros_like(y)[::2, ::2], np.zeros_like(U)[::2, ::2], V[::2, ::2], angles='xy', scale_units='xy', scale=1)
ax[1].set_ylim(np.min(V)*1.3, np.max(V)*1.3)
ax[0].set_xlabel('x'); ax[1].set_xlabel('x')
ax[0].set_ylabel('y'); ax[1].set_ylabel('y')
ax[0].set_title(r'$\vec{v}$ along the y-axis'), ax[1].set_title(r'$\vec{v}$ along the x-axis')
# plt.savefig('oppgave_3_b.png')
plt.show()
"""

QV1 = plt.quiver(np.zeros_like(x)[::2, ::2], y[::2, ::2], U[::2, ::2], np.zeros_like(V)[::2, ::2], angles='xy', scale_units='xy', scale=1, color='royalblue')
QV2 = plt.quiver(x[::2, ::2], np.zeros_like(y)[::2, ::2], np.zeros_like(U)[::2, ::2], V[::2, ::2], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiverkey(QV1, 3.5, 2.5, 1, label='x=0, (sin(y), 0)', coordinates='data', angle = 0)
plt.quiverkey(QV2, 3.5, 1.2, 1, label='y=0, (0, -sin(x))', coordinates='data', angle = 90, labelsep=0.3)
plt.plot([0,0],[np.min(y),np.max(y)], 'k'); plt.plot([np.min(x),np.max(x)],[0,0], 'k')
plt.xlabel('x', weight='bold'); plt.ylabel('y', weight='bold')
plt.axis('equal')
plt.title(r'$\vec{v}=(cos(x)sin(y), -sin(x)cos(y))$ along the x and y axis', weight='bold')
# plt.savefig('oppgave_3_b.png')
plt.show()
