import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
gs = fig.add_gridspec(3,2)
ax1 = fig.add_subplot(gs[0, 1], projection='3d', title=r'3D plot of $\vec{r}(t)$')
ax2 = fig.add_subplot(gs[1, 1], projection='3d')
ax3 = fig.add_subplot(gs[0::, 0], projection='3d')
ax4 = fig.add_subplot(gs[2, 1], projection='polar')

plt.show()
