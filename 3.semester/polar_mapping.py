import numpy as np
import matplotlib.pyplot as plt


l = 0.8
x = np.linspace(0.01, 2*np.pi, 400)
y = l*np.ones_like(x)

x1 = np.linspace(0, 2*np.pi*l, 400)
y1 = (l - 0.8)*np.ones_like(x1)

fig = plt.figure()
ax1 = fig.add_subplot(212)
ax1.grid(True)
ax2 = fig.add_subplot(211, projection='polar')

r = np.sqrt(x**2 + y**2)
theta = np.arctan(y/x)

x_polar = r*np.cos(theta)
y_polar = r*np.sin(theta)

ax1.plot(x, y, 'tomato')
ax1.plot(x1, y1, 'royalblue')
ax1.plot(l*np.cos(x), l*np.sin(x) + 2*l, 'royalblue')
ax2.plot(x, y/l, 'k', alpha=0.75)
ax2.plot(x_polar, y_polar, 'royalblue')
ax2.set_rlim([0,2])
ax2.set_rticks([1.0, 2.0])
ax2.set_yticklabels(['1.0', '2.0'])
points = np.linspace(0, 2*np.pi, 8)
points1 = np.linspace(0, 2*np.pi*l, 8)
colors = {0:'yellow', 1:'red', 2:'navy', 3:'limegreen', 4:'gold', 5:'brown',
          6:'lime', 7:'cyan', 8:'magenta', 9:'green', 10:'royalblue', 11:'crimson',
          12:'maroon', 13:'purple'}
ax1.axis('equal')
for key, p in enumerate(points):
    # for l in points:
    ax1.scatter(p, l, color=colors[key])
    ax1.scatter(-l*np.cos(p + np.pi/2), -l*np.sin(p + np.pi/2) + 2*l, color=colors[key])
    ax2.scatter(p, l, color=colors[key])
for key, p in enumerate(points1):
    ax1.scatter(p, (l - 0.8), color=colors[key])
fig.tight_layout()
plt.show()
