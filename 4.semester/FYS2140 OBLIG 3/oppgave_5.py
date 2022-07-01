import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# a, b, c)

# Bruker naturlige enheter
"""
Alle disse utledet i notat
kravet er at c = 1 og h = 1 skal være dimensjonsløse, og m_e = 1 kg
h : [kg*m^2/s^2 = kg] siden c : [m/s = [-]] -> m = s
E = sqrt(m^2c^4 + p^2c^2) = sqrt(m^2 + p^2) : [p = kg = E]
h: J*s = J*m = kg*m^2/s^2 * m = kg * m = [-] -> m = 1/kg = 1/E -> t = 1/kg = 1/E
etc. kan man gjøre for å utlede, bruker dette til å finne enheter
på andre ting nedover her
m = 1/E
t = 1/E
kg = E
J = E
p = E
F = E^2
"""
hbar = 1 # [-]
c = 1   # [-]
m = 1   # elektronmassen, [kg = E]
A = m       # [kg = E]

k1 = 0.7    # Gitt i oppgaven
k2 = 0.6

def omega(k):
    return c*np.sqrt(k**2 + (m*c/hbar)**2)  # [E]

def y(x,t,k):
    return A*np.sin(k*x - omega(k)*t)   # [E]

t = 0
x = np.linspace(-50, 50, 1000)
y1 = y(x, t, k1)
y2 = y(x, t, k2)
y_sum = y1 + y2

# Finner også fase- og gruppehastighet for summen
v_f1 = omega(k1) / k1
v_g1 = c**2 * k1 / omega(k1)
v_f2 = omega(k2) / k2
v_g2 = c**2 * k2 / omega(k2)
v_f = (omega(k1) + omega(k2)) / (k1 + k2)
v_g = (omega(k1) - omega(k2)) / (k1 - k2)
print(f'v_f1 = {v_f1}, v_f2 = {v_f2}\nv_g1 = {v_g1}, v_g2 = {v_g2}')
print(f'v_f = {v_f}, v_g = {v_g}')


plt.plot(x, y1, 'r--', label=r'$\psi_1$')
plt.plot(x, y2, 'b--', label=r'$\psi_2$')
plt.plot(x, y_sum, 'k', linewidth=2, label=r'$\psi = \psi_1 + \psi_2$')
plt.title(f't = {t}s', weight='bold', fontsize=20)
plt.xlabel('x [m]', weight='bold')
plt.ylabel('y(x,t) [E]', weight='bold')
plt.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot()

t = np.linspace(0, 100, 500)
maxx = 30
maxy = 1.7

def animate_a(frame):
    y1 = y(x, t[frame], k1)
    y2 = y(x, t[frame], k2)
    y_sum = y1 + y2
    p0, = ax.plot(x, y_sum, 'r')
    ax.set_xlabel('x [m]', weight='bold')
    ax.set_ylabel('y(x,t) [E]', weight='bold')
    timelabel = ax.text(maxx, maxy, f't={t[frame]:.1f}s', fontsize=16)
    return p0, timelabel,

ani = FuncAnimation(fig, func=animate_a, frames=len(t), interval=10, blit=True)
plt.show()


X = np.linspace(-50, 50, 1000)
T = np.linspace(0, 1, 1000)

x, t = np.meshgrid(X, T, indexing='ij')

y1 = y(x, t, k1)
y2 = y(x, t, k2)
y_sum = y1 + y2


fig = plt.figure()
gs = fig.add_gridspec(2,2)
ax1 = fig.add_subplot(gs[0,0], projection='3d')
ax2 = fig.add_subplot(gs[1,0], projection='3d')
ax3 = fig.add_subplot(gs[:,1], projection='3d')
ax1.set_xlabel('x', weight='bold'); ax1.set_ylabel('t', weight='bold')
ax2.set_xlabel('x', weight='bold'); ax2.set_ylabel('t', weight='bold')
ax3.set_xlabel('x', weight='bold'); ax3.set_ylabel('t', weight='bold')

ax1.plot_surface(x, t, y1, cmap='jet')
ax2.plot_surface(x, t, y2, cmap='jet')
ax3.plot_surface(x, t, y_sum, cmap='jet')

fig.tight_layout()
plt.show()


a = 100
def A(k):
    return a / (k**2 + a**2)

t = 0
k = np.linspace(-5, 5, 1000)[None,:]
x = np.linspace(-50, 50, 1000)[:,None]

def y_new(x, t, k):
    return A(k)*np.cos(k*x - omega(k)*t)

fig = plt.figure()
fig.suptitle(f't = {t}s', weight='bold', fontsize=20)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
y_sum = np.sum(y_new(x, t, k), axis=1)
ax1.plot(x, y_sum[:,None], 'r')
ax2.plot(x, y_new(x, t, k))
ax1.set_xlabel('x [m]', weight='bold')
ax2.set_xlabel('x [m]', weight='bold')
ax1.set_ylabel(r'y(x,t)$_{sum}$ [E]', weight='bold')
ax2.set_ylabel(r'y(x,t)$_k$ [E]', weight='bold')
ax1.set_title(r'$\sum_k$y(t,x)$_k$', weight='bold')
ax2.set_title(r'k$\in$[-5, 5; 1000]', weight='bold')
fig.tight_layout()
plt.show()

fig = plt.figure()
ax = fig.add_subplot()

t = np.linspace(0, 100, 500)
maxx = 30
maxy = 9

def update(frame):
    y_sum = np.sum(y_new(x, t[frame], k), axis=1)
    p0, = ax.plot(x, y_sum[:,None], 'r')
    ax.set_xlabel('x [m]', weight='bold')
    ax.set_ylabel('y(x,t) [E]', weight='bold')
    timelabel = ax.text(maxx, maxy, f't={t[frame]:.1f}s', fontsize=16, backgroundcolor='w')
    return p0, timelabel

ani = FuncAnimation(fig, func=update, frames=len(t), interval=10, blit=True)
plt.show()
