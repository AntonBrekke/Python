import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5, 5, 6)

x, y, z = np.meshgrid(I, I, I, indexing='ij')

u = 2*x
v = 2*y
w = 2*z


# Må gjøre dette for å få laget med cmap på 3D-quiver
k = np.sqrt(u**2 + v**2 + w**2)
# Flatten and normalize
c = np.ravel(k) / np.max(k)     # Ravel flater ned dimensjonene til en array
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))        # Gjentar c 2 ganger og konkatenerer så lista ikke går tom for verdier
c = plt.cm.gnuplot2(c)
# print(np.ptp(c) == np.max(c) - np.min(c))     # Returnerer True, ptp - peak to peak

fig = plt.figure(facecolor='k')
ax = fig.add_subplot(facecolor='k', projection='3d')

ax.set_axis_off()

len = 1 / (0.8*np.max(np.sqrt(u**2 + v**2 + w**2)))
# Kan normalisere med normalize=True eller dele på normen også for tydelig plott
quiver_3d = ax.quiver(x, y, z, u, v, w, colors=c, cmap='gnuplot2', arrow_length_ratio=0.5, normalize=True)   # cmap - argumentet er for cbar så den finner fargekartet
cbar = fig.colorbar(quiver_3d, ax=ax)
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='w')
# Få på plass riktige verdier på cbar
rnd = lambda t: round(t, 3)
N = 10
cbar.set_ticks(np.linspace(0, 1, N))
cbar.set_ticklabels([*map(rnd, np.linspace(np.min(k), np.max(k), N))])
cbax = cbar.ax
cbax.text(-1.5, 1.03, r'Speed$\left(\frac{m}{s}\right)$', color='w', rotation=1, fontsize=15)
# Alternativt
cbar.set_label(r'Speed$\left(\frac{m}{s}\right)$', color='w', fontsize=12)
plt.show()
