import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


fig = plt.figure()
ax = fig.add_subplot()

planet_img = plt.imread('planet_3.png')
image_box_planet = OffsetImage(planet_img, zoom=0.08)

N = 150
M = 600

x1 = np.linspace(0.8, 0, N)
x2 = np.linspace(0, 0.8, N)
traj1 = np.sqrt(x1)
traj2 = -np.sqrt(x2)

ax.plot(x1, traj1, x2, traj2, color='royalblue', linestyle='--')

a = 0.5
b = 0.49
c = np.sqrt(a**2 - b**2)
center = 0.5
theta = np.linspace(np.pi, 3*np.pi, M)
ellipse = (a*np.cos(theta) + center, b*np.sin(theta))

ax.plot(*ellipse, 'r', alpha=0.8)
ax.plot(c + center, 0, color='r', marker='o', markersize=20)
planet = AnnotationBbox(image_box_planet, (c + center, 0), frameon=False)
ax.add_artist(planet)

rocket_traj, = ax.plot([], [], color='royalblue', marker='o')
rocket_maneuver, = ax.plot([], [], color='r', marker='o')

def update(index):
    if index == 0: input()

    if index < N:
        rocket_traj.set_data(x1[index], traj1[index])
        rocket_maneuver.set_data(x1[index], traj1[index])
    elif index >= N:
        if index == N:
            ax.arrow(0, 0, 0.2, 0.3, head_width=0.02)
            ax.text(0.1, 0, r'$\Delta v$')
            plt.pause(1)
        rocket_maneuver.set_data(ellipse[0][index - N], ellipse[1][index - N])
        if index < 2*N:
            rocket_traj.set_data(x2[index - N], traj2[index - N])
        else:
            rocket_traj.set_data([], [])


    return rocket_traj, rocket_maneuver

ax.axis('off')
ax.axis('equal')
ani = FuncAnimation(fig, update, frames=M + N, interval=1)
plt.show()
