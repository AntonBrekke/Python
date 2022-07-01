import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-3, 3, 41)
x, y = np.meshgrid(I, I, indexing='xy')
# Strømningslinjer / hastighetsfelt

u = x*y
v = y

# Med streamplot regner den ut Potensialfunksjonen ut på egenhånd
fig, ax = plt.subplots(1,1)
strm = ax.streamplot(x, y, u, v, color = np.sqrt(u**2+v**2), cmap='jet')
ax.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])
fig.colorbar(strm.lines)
plt.show()


plt.contour(x, y, (np.log(abs(x))-y), 50, cmap='jet')
plt.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])
plt.plot(x, np.zeros_like(y), 'k.')
plt.xlabel('x'); plt.ylabel('y')
plt.title(r'$ln|x|-y=C$', weight='bold')
plt.savefig('oppgave_2_b.png')
plt.show()
