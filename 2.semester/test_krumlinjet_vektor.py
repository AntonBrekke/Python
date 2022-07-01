import numpy as np
import matplotlib.pyplot as plt

R = 1
w = 1
v0 = 0.1

I = np.linspace(-R, R, 40)
x, y = np.meshgrid(I, I, indexing='ij')

vx = -w*y - v0/np.sqrt(x**2 + y**2)
vy = w*x + v0/np.sqrt(x**2 + y**2)

plt.quiver(x[::2, ::2], y[::2, ::2], vx[::2, ::2], vy[::2, ::2])

r = np.linspace(0, R, 500)[:,None]  # Får numpy til å broadcaste
C = np.linspace(-2, 2, 5)[None,:] # Linspace for 5 ulike konstanter C
theta = -w/v0*r + C         # Fra strømlinjene v x dr = 0 eller dr x v = 0

x = r*np.cos(theta)
y = r*np.sin(theta)
t = np.linspace(0, 2*np.pi, 100)

plt.plot(x, y)
plt.plot(R*np.cos(t), R*np.sin(t), 'k')
plt.axis('equal')
plt.legend([f'C={c}' for c in C[0]], loc='upper right')

# plt.show()
plt.clf()

I = np.linspace(-R, R, 40)
x, y = np.meshgrid(I, I, indexing='ij')

vx = x
vy = -y
plt.quiver(x[::2, ::2], y[::2, ::2], vx[::2, ::2], vy[::2, ::2], np.sqrt(vx**2 + vy**2)[::2, ::2], cmap='jet')
x = np.linspace(-R, R, 300)[:,None]
C = np.linspace(-R, R, 11)[None,:]
plt.plot(x, C/x,'r')
plt.plot(x, np.sqrt(x**2 + C), 'g--', x, -np.sqrt(x**2 + C), 'g--')
plt.plot([0,0], [0,0], 'ko', markersize=10)
plt.axis('equal')
plt.xlim([-R, R])
plt.ylim([-R, R])
plt.show()
