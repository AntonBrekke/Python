import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(1, 25, 800)*1.5e11
t = np.linspace(0, 20*365*24*60*60, 800)

r, t = np.meshgrid(r, )
A = 1.28857e-24*r**2

plt.plot(r, A)
plt.show()
