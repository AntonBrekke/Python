import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from matplotlib.animation import FuncAnimation
from scipy.io import wavfile
from IPython.display import Audio
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

"""
Gode verdier for gitar-streng:
l = 2e-6
gamma = 8e-5
h = 0.005 (høy amplitude)
Simuler over 5 sekunder
"""
# Konstanter og variabler
Nx = 100
Nt = 1e6
L = 0.65
dx = L / Nx
dt = 5e-6
f = 130.81         # C3
# f = 146.83         # D3
v = 2*L*f       # v = 1 / (2*L) * np.sqrt(T / mu)
l = 2e-6        # m^2
gamma = 8e-5
x = np.linspace(0, L, Nx)
h = 1e-2           # m
print(f'Simulating for {Nt * dt} seconds')
print(f'Courant-betingelsen: dt < {dx / v}')

guitar_img = plt.imread('guitar.png')
image_box_guitar = OffsetImage(guitar_img, zoom=0.7)
guitar = AnnotationBbox(image_box_guitar, (L/2 - 0.02, -5e-3), frameon=False, zorder=0)

# Hvor man plukker gitarstrengen, initialbetingelse
x0 = 0.15
pluck_index = int(x0 / dx)
print(pluck_index)
y1 = np.linspace(0, h, pluck_index)
y2 = np.linspace(h, 0, Nx - pluck_index)
y0 = np.concatenate((y1, y2))
plt.plot(x, y0)
plt.show()

sol = np.zeros((int(Nt), Nx))
t0 = 0.5
t0_index = int(t0 / dt)
print(t0_index)
sol[0:t0_index+1] = y0

# Regner ut (diskretisert bølgelikning med demping og alt)
@njit
def compute_d(d, times, length, dt, dx, l, gamma):
    for i in range(t0_index, times-1):
        for j in range(2, length-2):
            outer_factor = (1/(v**2 * dt**2) + gamma/(2*dt))**(-1)
            p1 = 1 / dx**2 * (d[i, j+1] - 2*d[i, j] + d[i, j-1])
            p2 = 1 / (v**2 * dt**2) * (2*d[i, j] - d[i-1, j])
            p3 = gamma / (2*dt) * d[i-1, j]
            p4 = -l**2 / dx**4 * (d[i, j+2] - 4*d[i, j+1] + 6*d[i, j] - 4*d[i, j-1] + d[i, j-2])
            d[i+1, j] = outer_factor * (p1 + p2 + p3 + p4)
    return d


sol = compute_d(sol, Nt, Nx, dt, dx, l, gamma)

print(f'1/dt (fps): {1/dt}')

def update_guitar(frame):
    draw, = ax.plot(x, sol[frame*10 + t0_index], color='yellow', linewidth=2)
    ax.add_artist(guitar)
    return draw,

def update(frame):
    draw, = ax.plot(x, sol[frame*10 + t0_index], color='r')
    return draw,

def anim_guitar():
    global fig; global ax
    fig = plt.figure(figsize=(12, 6), facecolor=[0.12, 0.12, 0.12])
    ax = fig.add_subplot()
    ax.set_xlim(-0.3, 1.1*L)
    ax.set_ylim(-0.2, 0.2)
    ax.axis('off')
    ani = FuncAnimation(fig, update_guitar, frames=int(Nt/10), interval=20, blit=True)
    plt.show()

def anim():
    global fig; global ax
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(0, L)
    ax.set_ylim(-1.1*h, 1.1*h)
    ani = FuncAnimation(fig, update, frames=int(Nt/10), interval=20, blit=True)
    plt.show()

anim()
anim_guitar()

# Finner koeffisientene A_n som er i signalene
def get_integral(m):
    sin_arr = np.sin(m*np.pi*x/L)
    return np.array([np.sum(sin_arr*s, axis=0) for s in sol])       # Egentlig et integral, så må ha med dx. Men da blir lyden lav, og tenker at amplituden er prop. med integralet og ignorerer dx.

harmonics = [get_integral(m) for m in range(10)]

tot = np.sum(harmonics, axis=0)

wavfile.write('ex_guitar.wav', int(1/dt), tot.astype(np.float32))
Audio('ex_guitar.wav')
