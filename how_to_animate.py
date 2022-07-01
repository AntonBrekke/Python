import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
"""
class matplotlib.animation.FuncAnimation(fig, func,
    frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=True, **kwargs)
"""
"""
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r')

def init():
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 4*np.pi, 400), interval=10,
                    init_func=init, blit=True)

plt.show()

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'b')

def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-100, 100)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(frame**3 - 2*frame**2 + 3*frame - 5)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(-10, 10, 400), interval=10,
                    init_func=init, blit=True)

plt.show()
"""

"""
x = np.arange(-3, 3, 0.01)
j = 1
y = np.sin( np.pi*x*j ) / ( np.pi*x*j )
fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
#plot a line along points x,y
line, = ax.plot(x, y)
line2, = ax2.plot(x, y)
#update data
j_array = np.linspace(1,5,600)
for j in j_array:
    y1 = np.sin( np.pi*x*j ) / ( np.pi*x*j )
    y2 = y = np.log( np.pi*x*j ) / ( np.pi*x*j )
    #update the line with the new data
    line.set_ydata(y1)
    line2.set_ydata(y2)
    plt.draw()
    plt.pause(0.001)
"""

# Animering i subplots:
x = np.arange(-3, 3, 0.01)
a = 1
y1_start = np.sin(np.pi*x*a ) / ( np.pi*x*a )       # y1_start og y2_start må ikke være funksjonen som plottes, kan være f.eks bare x, for å få en linje som kan oppdateres
y2_start = np.sin(np.pi*a*x)**(np.cos(a**a*np.pi*x))
f, (ax1, ax2) = plt.subplots(1, 2, sharex = True, sharey = False)
line1, = ax1.plot(x, y1_start)
line2, = ax2.plot(x, y2_start, 'orange')
ax1.axis([-2, 2, -0.5, 1.5])
ax2.axis([-2, 2, -1, 5])
ax1.set_title(r'$f(x) = \frac{sin(a\pi x)}{a\pi x}$,')
ax2.set_title(r'$f(x) = sin(a\pi x)^{cos(a^a\pi x)}$,')
#update data
a_array = np.linspace(0.1,4,200)
for a in a_array:
    y1 = np.sin(np.pi*x*a ) / ( np.pi*x*a )
    y2 = np.sin(np.pi*a*x)**(np.cos(a**a*np.pi*x))
    #update the line with the new data
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    plt.draw()
    plt.pause(0.001)
