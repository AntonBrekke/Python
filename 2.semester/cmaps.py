import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap

viridis = cm.get_cmap('viridis', 12)
print(viridis)
print(viridis(0.56))

I = np.linspace(0,1)
x,y = np.meshgrid(I, I, indexing='xy')
L = np.cos(x) + np.sin(y)

top = cm.get_cmap('twilight', 256)
bottom = cm.get_cmap('YlOrRd', 256)

newcolors = np.vstack((top(np.linspace(0, 1, 256)),
                       bottom(np.linspace(0, 1, 256))))
newcmp = ListedColormap(newcolors, name='OrangeBlue')

fig = plt.figure()
ax = fig.add_subplot(111)
plot = ax.contourf(x,y,L,200, cmap=newcmp)
fig.colorbar(plot, ax=ax)
plt.show()
