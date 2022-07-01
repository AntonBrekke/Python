import numpy as np
import matplotlib.pyplot as plt
import random

import numpy as np
import matplotlib.pyplot as plt

num = int(input('Input how many friends you want!: '))

class Friends:
    def __init__(self, S, R, number_of_friends):
        self.R = R; self.S = S
        self.number = number_of_friends

    def kule(self, S, R):
        I = np.linspace(0, 2*np.pi)
        J = np.linspace(0, np.pi)
        theta, phi = np.meshgrid(I, J, indexing='ij')
        a, b, c = S

        x = a + R*np.cos(theta)*np.sin(phi)
        y = b + R*np.sin(theta)*np.sin(phi)
        z = c + R*np.cos(phi)

        return x, y, z

    def random_color(self):
        color = [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)]
        return color

    def summon(self):
        a, b, c = self.S
        R = self.R
        fig = plt.figure()
        for n in range(1, 20):
            if n**2 >= self.number:
                k = n
                break
        for i in range(1, self.number+1):
            ax = fig.add_subplot(k,k,i, projection='3d')
            # Hode
            ax.plot_surface(*self.kule([a,b,c], R), color=self.random_color())
            # Øyer
            ax.plot_surface(*self.kule([0.8+a, -2+b, 2+c], 0.5), color='w')
            ax.plot_surface(*self.kule([2+a, -1+b, 2+c], 0.5), color='w')
            ax.plot_surface(*self.kule([2.1+a, -1.1+b, 2.2+c], 0.3), color='k')
            ax.plot_surface(*self.kule([0.9+a, -2.1+b, 2.2+c], 0.3), color='k')
            ax.set_xticklabels([]); ax.set_yticklabels([]); ax.set_zticklabels([])

Homies = Friends(S=[0,0,0], R=3, number_of_friends=num)
Homies.summon()
plt.show()
