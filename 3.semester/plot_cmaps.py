import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

fig = plt.figure(facecolor='k')
ax = fig.add_subplot(facecolor='k')

x = np.linspace(0, 6*np.pi, 1000)
# 3 linje-eksempler
f = 3*np.exp(0.1*x)*np.sin(2*x)*np.cos(x - 1) + 2*x
g = 40*np.exp(-0.2*x)
h = 5*np.cos(x) - 2*x + 40

# Henter 3 eksempler på fargekart å gi til linjer
get_viridis = plt.get_cmap('viridis')
viridis = np.array(get_viridis(f / np.max(f)))

get_jet = plt.get_cmap('jet')
jet = np.array(get_jet(g / np.max(g)))

get_plasma = plt.get_cmap('plasma')
plasma = np.array(get_plasma(h / np.max(h)))

# Må plotte linjevis
for i in range(len(x)-1):
    line1, = ax.plot([x[i], x[i+1]], [f[i], f[i+1]], color=viridis[i], linewidth=3)
    line2, = ax.plot([x[i], x[i+1]], [g[i], g[i+1]], color=jet[i], linewidth=3)
    line3, = ax.plot([x[i], x[i+1]], [h[i], h[i+1]], color=plasma[i], linewidth=3)

plt.show()
