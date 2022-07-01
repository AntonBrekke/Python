import numpy as np
import matplotlib.pyplot as plt


C = np.linspace(-2, 2, 5)[None,:]
x = np.linspace(-5, 5, 300)[:,None]

y_phi = np.sqrt(C + x**2)
y_psi = C/x

plt.plot(x, y_phi, 'g--', x, -y_phi, 'g--')
plt.plot(x, y_psi, 'r')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.text(4,3.2, 'y_psi', color='r', weight='bold')
plt.text(4,2.8, 'y_phi', color='g', weight='bold')
plt.show()
