import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(0, 2*np.pi, 800)
theta, phi = np.meshgrid(I, I, indexing='ij')

r = 1
R = 3

# Parameteriserer torus
x = (r*np.cos(theta) + R)*np.cos(phi)
y = (r*np.cos(theta) + R)*np.sin(phi)
z = r*np.sin(theta)
# Lager figur
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d", title="Torus")
ax.plot_surface(x, y, z, cmap='hsv_r')
ax.set_zlim(-R, R)  # Setter grensene på z-aksen så figuren dimensjoneres riktig
plt.show()
