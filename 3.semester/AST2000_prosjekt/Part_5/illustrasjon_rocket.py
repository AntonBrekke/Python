import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(-0.1, 1, 200)
xh1 = x[:151]
xh2 = x[150:]

traj_plan = 0.25*x**2
traj_dev = 0.2*x**2
traj_cor1 = 0.2*xh1**2
traj_cor2 = 0.53*(xh2 - xh1[-1]) + traj_cor1[-1]

fig = plt.figure()
plt.axis('off')
plt.plot(x, traj_plan, 'royalblue', linestyle='--', label='Planned trajectory')
plt.plot(x, traj_dev, 'orange', linestyle='--', label='Deviated (real) trajectory')
plt.plot(xh1, traj_cor1, 'r', label='Corrected trajectory')
plt.plot(xh2, traj_cor2, 'r')
# plt.show()

rocket_plan, = plt.plot([],[], 'royalblue', marker='o')
rocket_dev, = plt.plot([], [], 'orange', marker='o')
rocket_cor, = plt.plot([], [], 'red', marker='o')

def update(index):
    if index == 0:          # Skal bare hjelpe meg med å få tid til å ta opptak av animasjon
        input('Play:')
    rocket_plan.set_data(x[index], traj_plan[index])
    rocket_dev.set_data(x[index], traj_dev[index])
    if index <= 150 and index >= 150:
        arrow = plt.arrow(xh1[-1], traj_cor1[-1], -0.1, 0.04, head_width=0.003)
        text = plt.text(xh1[-1] - 0.06, traj_cor1[-1] + 0.03, r'$\Delta v$', fontsize=16)
    if index < 150:
        rocket_cor.set_data(xh1[index], traj_cor1[index])
    else:
        rocket_cor.set_data(xh2[index - 150], traj_cor2[index - 150])

    return rocket_plan, rocket_dev, rocket_cor

ani = FuncAnimation(fig, update, frames=[i for i in range(0, len(x), 2)], interval=1)
plt.legend()
plt.show()
