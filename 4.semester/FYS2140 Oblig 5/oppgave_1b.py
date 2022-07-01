import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.constants as sc
import time

a = 1e-9        # m
hbar = 6.582119569e-16   # eVs
m = 0.511e6 / sc.c**2      # 0.511MeV/c^2
n = 3
def Psi(x,t):
    return np.sqrt(2 / a) * np.sin(n*np.pi/a*x) * np.exp(-1j*(n**2*np.pi**2*hbar / (2*m*a**2))*t)

x = np.linspace(0, a, 1000)
t = np.linspace(9.5e-15, 10.5e-15, 1000)        # fs (1e-15s)

# Lager figur og plott til animasjon
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_xlabel('x [m]', weight='bold')
ax2.set_xlabel('x [m]', weight='bold')

# Animerer Psi over tid
M = 3
def update(frame):
    plot_prop, = ax1.plot(x, abs(Psi(x, t[frame])**2), 'k')
    plot_real, = ax2.plot(x, np.real(Psi(x, t[frame])), 'r')
    plot_imag, = ax2.plot(x, np.imag(Psi(x, t[frame])), 'b')
    ymin1, ymax1 = ax1.get_ylim()
    ymin2, ymax2 = ax2.get_ylim()
    timelabel1 = ax1.text(a*0.9, ymin1 + 0.05*ymax1, f't={t[frame]:.2e}s', weight='bold', fontsize=12)
    timelabel2 = ax2.text(a*0.9, ymin2 + 0.05*ymax2 * 2, f't={t[frame]:.2e}s', weight='bold', fontsize=12)
    ax1.legend([plot_prop], [r'$|\Psi|^2$'], loc='upper right'); ax2.legend([plot_real, plot_imag], [r'Re{$\Psi$}', r'Im{$\Psi$}'], loc='upper right')
    if t[frame] > 10e-15 and t[frame] < 10e-15 + M*(t[1] - t[0]): time.sleep(5)
    return plot_real, plot_imag, plot_prop, timelabel1, timelabel2


ani = FuncAnimation(fig, func=update, frames=[i for i in range(0, len(t), M)], interval=10, blit=True)
fig.tight_layout()
plt.show()
