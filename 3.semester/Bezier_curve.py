import numpy as np
import matplotlib.pyplot as plt

"""
Plotter cubic Bezier-kurver
"""

fig = plt.figure()
gs = fig.add_gridspec(3, 2)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[1,0])
ax3 = fig.add_subplot(gs[2,0])
ax4 = fig.add_subplot(gs[:,1])

A = np.array([[0, 0]])
B = np.array([[0, 2]])
C = np.array([[-2, 1]])
D = np.array([[1, 0]])

t = np.linspace(0, 1, 300)[:,None]

r1 = (1-t)*A + t*B
r2 = (1-t)*B + t*C
r3 = (1-t)*C + t*D

r4 = (1-t)*r1 + t*r2
r5 = (1-t)*r2 + t*r3

r6 = (1-t)*r4 + t*r5

ax1.plot(r1[:,0], r1[:,1])
ax1.plot(r2[:,0], r2[:,1])
ax1.plot(r3[:,0], r3[:,1])
ax1.plot(A[0,0], A[0,1], 'ko'); ax1.text(A[0,0], A[0,1], s='A')
ax1.plot(B[0,0], B[0,1], 'ko'); ax1.text(B[0,0], B[0,1], s='B')
ax1.plot(C[0,0], C[0,1], 'ko'); ax1.text(C[0,0], C[0,1], s='C')
ax1.plot(D[0,0], D[0,1], 'ko'); ax1.text(D[0,0], D[0,1], s='D')


ax2.plot(r4[:,0], r4[:,1])
ax2.plot(r5[:,0], r5[:,1])

ax3.plot(r6[:,0], r6[:,1])

ax4.plot(r1[:,0], r1[:,1])
ax4.plot(r2[:,0], r2[:,1])
ax4.plot(r3[:,0], r3[:,1])
ax4.plot(r4[:,0], r4[:,1])
ax4.plot(r5[:,0], r5[:,1])
ax4.plot(r6[:,0], r6[:,1])

fig.tight_layout()
plt.show()
