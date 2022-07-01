import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


func = input('Input a function: ')
n = int(input('Input number of sum: '))
funclabel = func.replace('**', '^').replace('np.', '').replace('*', '')
funclabel = f'${funclabel}$'        # Formatterer penere

X = np.linspace(-4, 4, 1000)
dX = X[1] - X[0]
N = np.arange(1, n+1, 1)

n, x = np.meshgrid(N, X, indexing='ij')     # Vi gjør det på denne måten denne gangen vi ;) 

f = eval(func)
f1 = eval(func.replace('exp', '~').replace('x', 'X').replace('~', 'exp'))

a0 = 1 / np.pi * np.sum(f, axis=1)*dX               # Regner ut Fourier-koeffisienter med wack integral
an = 1 / np.pi * np.sum(f * np.cos(n*x), axis=1)*dX
bn = 1 / np.pi * np.sum(f * np.sin(n*x), axis=1)*dX

an = an[:, None]        # Må ha ekstra akser på disse for broadcasting heheh
bn = bn[:, None]        # Må ha ekstra akser på disse for broadcasting heheh

g = an * np.cos(n*x) + bn * np.sin(n*x)
fig = plt.figure()
ax = fig.add_subplot()
functext = ax.set_title(f'f(x)={funclabel}', fontsize=16, weight='bold', ha='center')

pmax = np.max(f1)       # Standard hvor-skal-jeg-plassere-teksten-generelt-tingtang
pmin = np.min(f1)       # Standard hvor-skal-jeg-plassere-teksten-generelt-tingtang

# Bitch ass funksjon som animerer shit, yeeee haw
def update(frame):
    h = a0[frame]/2 + np.sum(g[0:frame+1, :], axis=0)
    line, = ax.plot(X, h, 'r')      # Fourier-crap
    line2, = ax.plot(X, f1, 'k')    # tha real func
    text = ax.text(4, pmin, f'n={N[frame]}', fontsize=16, weight='bold', ha='right')    # ha gir referansepunkt til teksten (ha='center' er nice å vite om ;) )
    return line, line2, text,

ani = FuncAnimation(fig, update, frames=len(N), interval=50, blit=True, repeat=False)
plt.show()
