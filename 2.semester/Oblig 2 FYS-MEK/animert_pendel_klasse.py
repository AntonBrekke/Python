import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import collections  as mc
from decimal import Decimal, getcontext

getcontext().prec = 10

class Pendulum:
    def __init__(self, g, k, L_0, r_start, m, T, N):
        self.g = g
        self.k = k
        self.L_0 = L_0
        self.r_start = r_start
        self.m = m

        self.N = N
        self.T = T

        self.a = np.zeros([N+1, 2])
        self.v = np.zeros([N+1, 2])
        self.r = np.zeros([N+1, 2])
        self.t = np.linspace(0, T, N+1)

        self.i = np.array([1,0])
        self.j = np.array([0,1])

    def set_initial_condition(self, v0, theta):
        self.r0 = self.r_start*np.sin(theta)*self.i - self.r_start*np.cos(theta)*self.j
        self.v0 = v0
        R0 = np.linalg.norm(self.r0)
        re0 = self.r0 / R0
        self.a0 = -self.g*self.j - self.k*(R0 - self.L_0)*re0/self.m

    def solve(self):
        t = self.t; a = self.a; v = self.v; r = self.r
        a[0] = self.a0
        v[0] = self.v0
        r[0] = self.r0
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1,:] = v[n,:] + dt*a[n,:]
            r[n+1,:] = r[n,:] + dt*v[n+1,:]
            R = np.linalg.norm(r[n+1,:])
            re = r[n+1,:] / R
            a[n+1,:] = -self.g*self.j - self.k*(R - self.L_0)*re/self.m
        return self.a, self.v, self.r, self.t

"""
I oblig:
k = 1
v0 = [-2, 2]
r0 = [1, np.pi/6]

Morsomme verdier:
k = 2
v0 = [-1, 2]
r0 = [0.3, np.pi]
"""

# Henter inn parametere fra terminal via. input og formatterer
k_in = input('Bestem fjærkonstant:')
v0_in = input('Sett initialhastighet [vx, vy]: ')
r0_in = input('Sett initialposisjon (theta [rad]), [r, theta]: ')
if k_in == '': k = 2; k_in = f'{k}'
elif float(k_in) <= 0: raise ValueError('Choose k bigger than 0')
else: k = float(k_in)
if v0_in == '': v0 = [-1, 2]; v0_in = f'{v0}'
else: v0 = [eval(i) for i in v0_in.strip('[]').replace(' ', '').split(',')]
if r0_in == '':
    r0 = [0.3, np.pi]
    const = Decimal(f'{r0[1] / np.pi}')
    a, b = const.as_integer_ratio()
    print(a, b)
    if a == 1 and b!= 1:
        r0_in = f'[{r0[0]}, ' + r'$\frac{\pi}{' + f'{b}' + r'}$]'
    elif a == 0:
        r0_in = f'[{r0[0]}, 0]'
    elif b == 1 and a != 1:
        r0_in = f'[{r0[0]}, {a}' + r'$\pi$]'
    elif a == 1 and b == 1:
        r0_in = f'[{r0[0]}, ' + r'$\pi$]'
    else:
        r0_in = f'[{r0[0]}, ' + r'$\frac{' + f'{a}' + r'\pi}{' + f'{b}' + r'}$]'

else:
    r0 = [eval(i) for i in r0_in.strip('[]').replace(' ', '').split(',')]
    const = Decimal(f'{r0[1] / np.pi}')     # Finner koeffisient foran pi
    a, b = const.as_integer_ratio()     # Regner ut som ratio mellom heltall
    print(a, b)
    exp10_a = 0
    exp10_b = 0
    while a >= 10:       # Skriver den ned på exp. form
        a *= 1/10
        exp10_a += 1
    while b >= 10:
        b *= 1/10
        exp10_b += 1
    a, b = round(a, 2), round(b, 2)
    print(exp10_a, exp10_b)
    if exp10_a > exp10_b:       # Deler bort forholdet mellom eksponent
        a *= 10**exp10_a / 10**exp10_b
    elif exp10_a < exp10_b:
        b *= 10**exp10_b / 10**exp10_a
    print(a, b)
    if '.' in f'{a}':           # Gjør om floats til int om de egt er int, f.eks 5.0 -> 5, 6.0000 -> 6, men 5.5 != 5
        split_list_a = np.array([i for i in f'{a}'.split('.')[1]])
    else:
        split_list_a = np.array([i for i in f'{a}'])
    if '.' in f'{b}':
        split_list_b = np.array([j for j in f'{b}'.split('.')[1]])
    else:
        split_list_b = np.array([j for j in f'{b}'])
    print(split_list_a, split_list_b)
    if np.all(split_list_a == '0'): a = int(a)
    if np.all(split_list_b == '0'): b = int(b)
    print(a, b)
    if a == 1 and b == 1:
        r0_in = f'[{r0[0]}, ' + r'$\pi$]'
    elif a == 1:
        r0_in = f'[{r0[0]}, ' + r'$\frac{\pi}{' + f'{b}' + r'}$]'
    elif a == 0:
        r0_in = f'[{r0[0]}, 0]'
    elif b == 1:
        r0_in = f'[{r0[0]}, {a}' + r'$\pi$]'
    else:
        # print('yo')
        r0_in = f'[{r0[0]}, ' + r'$\frac{' + f'{a}' + r'\pi}{' + f'{b}' + r'}$]'

r_start, theta = r0

method = Pendulum(g=9.81, k=k, L_0=1, r_start=r_start, m=0.1, T=30, N=2000)
method.set_initial_condition(v0=v0, theta=theta)
a, v, r, t = method.solve()
"""
class matplotlib.animation.FuncAnimation(fig, func,
    frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=True, **kwargs)
"""
fig = plt.figure(facecolor='k', figsize=(10, 6))
ax = fig.add_subplot(facecolor='k')
ax.spines['bottom'].set_color('w')      # Setter aksen hvit
ax.spines['left'].set_color('w')
ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
ax.tick_params(axis='y', colors='w')

plt.suptitle("Pendulum", fontweight='bold')
ax.set_xlabel('x [m]', weight='bold', fontsize=12)
ax.set_ylabel('y [m]', weight='bold', fontsize=12)

if np.max(r[:,1]) < 0:
    ymax = 0
else:
    ymax = np.max(r[:,1])*1.1

ymin = np.min(r[:,1])*1.1
xmin = np.min(r[:,0])*1.1

xmax = np.max(r[:,0])*1.1

# Henter cmap som skal plotte linje i ulike farger
get_cmap = plt.get_cmap('jet')
colors = np.array(get_cmap(abs(r[:,1]) / np.max(abs(r[:,1]))))      # Farger etter høyde y rundt nullpunktet, normaliserer maximum

# Lager en kolleksjon med alle linjestykkene som skal plottes
lines = np.zeros([len(r[:,0]), 2, 2])
for n in range(len(lines)-1):
    lines[n, 0, :] = [r[n, 0], r[n,1]]
    lines[n, 1, :] = [r[n+1, 0], r[n+1, 1]]

lc = mc.LineCollection(lines, colors=colors)

# Init-func som kalles på første frame
def init():
    ax.clear()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_xlabel('x [m]', weight='bold', color='w', fontsize=14)
    ax.set_ylabel('y [m]', weight='bold', color='w', fontsize=14)
    ax.set_title(f'k={k}N/m, v0 = {v0_in}, r0 = {r0_in}', color='w', fontsize=14, weight='bold')
    return ()       # Må returnere en iterabel med blit=True

# Update-funksjonen skal tegne og animere selve plottet
def update(frame):
    lc = mc.LineCollection(lines[0:frame, :, :], colors=colors, linewidths=2)
    ax.add_collection(lc)
    line, = ax.plot([0, r[frame,0]], [0, r[frame,1]], color='w', label=f'k={k}N/m')
    ln_ball, = ax.plot(r[frame, 0], r[frame, 1], color='red', marker='o', markersize='22')  # Trenger ikke datalister for ballen siden jeg ikke lagrer posisjonen
    timelabel = ax.text(xmax/2, ymin+0.3, f't={method.t[frame]:.2f}s', color='w', fontsize=14, weight='bold')
    return lc, line, ln_ball, timelabel        # Må returnere alle biter som skal animeres, må også være iterable om blit=True

ani = FuncAnimation(fig, update, init_func=init, frames=[i for i in range(0, method.N, 1)],
                    interval=2, blit=True, repeat=True)

# writer = PillowWriter(fps=25)
# ani.save("pendulum_klasse.gif", writer=writer)
plt.show()
