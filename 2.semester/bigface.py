import numpy as np
import matplotlib.pyplot as plt

class Friend:
    def __init__(self, S, R, col, name):
        self.R = R; self.S = S; self.col = col
        self.name = name

    def kule(self, S, R):
        I = np.linspace(0, 2*np.pi)
        J = np.linspace(0, np.pi)
        theta, phi = np.meshgrid(I, J, indexing='ij')
        a, b, c = S

        x = a + R*np.cos(theta)*np.sin(phi)
        y = b + R*np.sin(theta)*np.sin(phi)
        z = c + R*np.cos(phi)

        return x, y, z

    def summon_friend(self):
        a, b, c = self.S
        R = self.R
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        # Hode
        ax.plot_surface(*self.kule([a,b,c], R), color=self.col)
        # Øyer
        ax.plot_surface(*self.kule([0.8+a, -2+b, 2+c], 0.5), color='w')
        ax.plot_surface(*self.kule([2+a, -1+b, 2+c], 0.5), color='w')
        ax.plot_surface(*self.kule([2.1+a, -1.1+b, 2.2+c], 0.3), color='k')
        ax.plot_surface(*self.kule([0.9+a, -2.1+b, 2.2+c], 0.3), color='k')
        ax.text(a,b, c+4, self.name, size=10, weight='bold')
        ax.set_xticklabels([]); ax.set_yticklabels([]); ax.set_zticklabels([])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Karl = Friend([0,0,0], 3, 'yellow', 'Karl')
Karl.summon_friend()

Sigrid = Friend([-5,-5,0], 3, 'red', 'Sigrid')
Sigrid.summon_friend()

Jonathan = Friend([5,-5,0], 2, 'lightblue', 'Jonathan')
Jonathan.summon_friend()

plt.show()
