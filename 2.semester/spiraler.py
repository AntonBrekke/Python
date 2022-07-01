import numpy as np
import matplotlib.pyplot as plt

# Fra MEK eksamen 2019
w = 1         # Vinkelfart på karusellen (konstant hele tiden)
v0 = 0.1      # Fart i negativ radiell retning
R = 1         # Radius

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
plt.show()
