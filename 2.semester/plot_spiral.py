import numpy as np
import matplotlib.pyplot as plt

# Plotter spiral i kartesiske koordinater

w = 1
v0 = 0.1
# Broadcaster
r = np.linspace(0, 1, 100)[:,None]
theta = -w/v0*r + np.linspace(-2, 2, 5)[None,:]
# I kartesiske x, y koordinater
plt.plot(r*np.cos(theta), r*np.sin(theta))
plt.axis('equal')
plt.show()
# I r, theta koordinater
for w in range(0, 5):
    plt.plot(r, -w/v0*r)
plt.show()
