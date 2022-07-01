import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd

lab = vd.polarisasjon()
lab.find_refraction_n2(thetab=55.6, n1=1, angle='degree')
lab.d_lambda_half()

p1 = np.loadtxt('polarisering1.dat')
p2 = np.loadtxt('polarisering2.dat')
p3 = np.loadtxt('polarisering3.dat')

fig, (ax1, ax2, ax3) = plt.subplots(3,1)

ax1.plot(p1[:, 0], p1[:, 1], 'r')
ax2.plot(p2[:, 0], p2[:, 1], 'b')
ax3.plot(p3[:, 0], p3[:, 1], 'k')

fig.tight_layout()
plt.show()
