from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

N = 100

# Forskjellige thetaverdier for ulike baner
theta0 = np.linspace(0, 2*np.pi, N)
theta1 = np.linspace(np.pi/2, 5*np.pi/2, N)
theta2 = np.linspace(-np.pi/4, 7*np.pi/4, N)
theta3 = np.linspace(-np.pi/5, 8*np.pi/3, N)
theta4 = np.linspace(-np.pi/8, 2*np.pi, N)
theta5 = np.linspace(3*np.pi/4, 7*np.pi/4, N)
theta6 = np.linspace(-np.pi/2, np.pi/4, N)

data0 = np.zeros((3, N))
data1 = np.zeros((3, N))
data2 = np.zeros((3, N))
data3 = np.zeros((3, N))
data4 = np.zeros((3, N))
data5 = np.zeros((3, N))
data6 = np.zeros((3, N))

r0 = 1
r1 = 2
r2 = 3
r3 = 4
r4 = 5
r5 = 6
r6 = 7


ax.plot(0, 0, 0, color='yellow', marker='o', markersize=10)     # Stjerna
# Baner
line0, = ax.plot(r0*np.cos(theta0), r0*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)
line1, = ax.plot(r1*np.cos(theta0), r1*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)
line2, = ax.plot(r2*np.cos(theta0), r2*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)
line3, = ax.plot(r3*np.cos(theta0), r3*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)
line4, = ax.plot(r4*np.cos(theta0), r4*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)
line5, = ax.plot(r5*np.cos(theta0), r5*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)
line6, = ax.plot(r6*np.cos(theta0), r6*np.sin(theta0), np.zeros_like(theta0), color='k', linewidth=0.8)

# Setter dataverdier samtidig som jeg animerer
def update(frame):
    data0[:,frame] = r0*np.cos(theta0[frame]), r0*np.sin(theta0[frame]), 0
    data1[:,frame] = r1*np.cos(theta1[frame]), r1*np.sin(theta1[frame]), 0
    data2[:,frame] = r2*np.cos(theta2[frame]), r2*np.sin(theta2[frame]), 0
    data3[:,frame] = r3*np.cos(theta3[frame]), r3*np.sin(theta3[frame]), 0
    data4[:,frame] = r4*np.cos(theta4[frame]), r4*np.sin(theta4[frame]), 0
    data5[:,frame] = r5*np.cos(theta5[frame]), r5*np.sin(theta5[frame]), 0
    data6[:,frame] = r6*np.cos(theta6[frame]), r6*np.sin(theta6[frame]), 0
    p0, = ax.plot3D(data0[0, frame], data0[1, frame], data0[2, frame], color='blue', marker='o')
    p1, = ax.plot3D(data1[0, frame], data1[1, frame], data1[2, frame], color='green', marker='o')
    p2, = ax.plot3D(data2[0, frame], data2[1, frame], data2[2, frame], color='orange', marker='o')
    p3, = ax.plot3D(data3[0, frame], data3[1, frame], data3[2, frame], color='purple', marker='o')
    p4, = ax.plot3D(data4[0, frame], data4[1, frame], data4[2, frame], color='cyan', marker='o')
    p5, = ax.plot3D(data5[0, frame], data5[1, frame], data5[2, frame], color='gold', marker='o')
    p6, = ax.plot3D(data6[0, frame], data6[1, frame], data6[2, frame], color='maroon', marker='o')
    # ax.axis('off')
    return p0, p1, p2, p3, p4, p5, p6

# Setting the axes properties
ax.set_xlim3d([-5, 5])
ax.set_xlabel('X')

ax.set_ylim3d([-5, 5])
ax.set_ylabel('Y')

# ax.set_zlim3d([-5, 5])
ax.set_zlabel('Z')

ani = FuncAnimation(fig, func=update, frames=N, interval=10, blit=True)
#ani.save('matplot003.gif', writer='imagemagick')
plt.show()
