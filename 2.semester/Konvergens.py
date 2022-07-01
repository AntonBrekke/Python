import numpy as np
import matplotlib.pyplot as plt

def G(x,y):
    G1 = 1/x - 3/4*(y-1)
    G2 = x + 0.99*(y-1)
    return G1, G2

N = 100
x0 = (10,5)
a = np.zeros([N+1, 2])
a[0] = x0
for n in range(1, N+1):
    a[n] = G(a[n-1,0], a[n-1,1])

plt.plot(a[:,0], a[:,1])
I = np.linspace(-10,10, 40)
x,y = np.meshgrid(I, I, indexing='xy')
plt.quiver(x[::2,::2], y[::2,::2], (G(x,y)[0])[::2,::2], (G(x,y)[1])[::2,::2])
plt.show()
