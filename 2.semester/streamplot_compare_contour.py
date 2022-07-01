import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-3, 3, 40)
x, y = np.meshgrid(I, I, indexing='xy')
# Strømningslinjer / hastighetsfelt
u = -y
v = x

# Med streamplot regner den ut Potensialfunksjonen ut på egenhånd
fig, ax = plt.subplots(1,2)
strm = ax[1].streamplot(x, y, u, v, color = np.sqrt(u**2+v**2), cmap='jet')
ax[1].quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])
fig.colorbar(strm.lines)

# For å lage konturplott må du lage prikk-produkt likningen f.eks (-y, x)dot(a,b) = 0 for å finne gradientfeltet til Potensialfunksjonen,
# og så finne Potensialfunksjonen fra gradientfeltet
"""
(-y, x)dot(a, b) = -ay + bx = 0
a = x , b = y en løsning
grad,psi = (x, y) -> psi = 0.5*x**2 + 0.5*y**2 + C
"""
ax[0].contour(x, y, 0.5*x**2 + 0.5*y**2, 20, cmap='jet')       # Potensialfunksjonen til
ax[0].quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])

"""
fig, ax = plt.subplots(1,1)
strm = ax.streamplot(x, y, u, v, color = np.sqrt(u**2+v**2), cmap='jet')
ax.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])
cbaxes = fig.add_axes([0.87, 0.11, 0.03, 0.77])        # Posisjoner fargebar
fig.colorbar(strm.lines, cax = cbaxes)
ax.axis('equal')
"""
plt.show()
