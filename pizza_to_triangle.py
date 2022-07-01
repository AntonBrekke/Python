import numpy as np
import matplotlib.pyplot as plt


r = 1
theta = np.linspace(0, 2*np.pi)

# Plot circle
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y, label='Rund pizza')


# Plot triangle with equal area as circle
# Plot with G = 2*pi*r

G = 2*np.pi*r

plt.plot([3, G+3],[-1/2,-1/2], 'r', label='Trekant pizza')
plt.plot([3, G/2 + 3],[-1/2,r-1/2], 'r')
plt.plot([G/2 + 3, G+3],[r-1/2,-1/2], 'r')

plt.axis('equal')
plt.legend()
plt.show()
