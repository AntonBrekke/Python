import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import trange
from numba import njit

class Bouncy_ball():
    box_L = 10
    a = -9.81
    sim_time = 10       # s
    dt = 1e-3
    N = int(sim_time / dt)
    def __init__(self):
        self.v0 = np.random.normal(0, 5, 2)
        self.r0 = np.random.uniform(0.3, Bouncy_ball.box_L*0.8, 2)
        self.N = Bouncy_ball.N
        self.r = np.zeros((self.N, 2))
        self.v = np.zeros((self.N, 2))

    def bounce_ball(self):
        v0 = self.v0
        r0 = self.r0
        v = self.v
        r = self.r
        N = self.N
        L = Bouncy_ball.box_L
        a = np.array([0, Bouncy_ball.a])
        dt = Bouncy_ball.dt

        v[0] = v0
        r[0] = r0
        @njit(cache=True)
        def fast_loop(r, v):
            r = r.copy()
            v = v.copy()
            df = 0.9            # Damping factor
            for i in range(N-1):
                if r[i,0] <= 0 and r[i,0] >= v[i,0]*dt or r[i,0] >= L and r[i,0] <= L + v[i,0]*dt:
                    v[i,0] *= -1*df
                if r[i,1] <= 0 and r[i,1] >= v[i,1]*dt - 0.01:
                    v[i,1] *= -1*df
                v[i+1] = v[i] + a*dt
                r[i+1] = r[i] + v[i+1]*dt
            return r, v
        r, v = fast_loop(r, v)
        return r

fig = plt.figure()
ax = fig.add_subplot()
N = Bouncy_ball.N
dt = Bouncy_ball.dt
t = np.linspace(0, N*dt, N)
L = Bouncy_ball.box_L
ax.set_xlim(0, L)
ax.set_ylim(0, 2*L)
ax.set_xticks([])
ax.set_yticks([])

def num_balls(n):
    balls = np.zeros((n, Bouncy_ball.N, 2))
    for i in trange(n, desc='Creating balls'):
        ball = Bouncy_ball()
        r = ball.bounce_ball()
        balls[i,:,:] = r
    return balls

n = eval(input('\nNumber of balls: '))
balls_array = num_balls(n)

def update(frame):
    line, = ax.plot(balls_array[:,frame,0], balls_array[:,frame,1], color='r', marker='o', linewidth=0)
    timelabel = ax.text(L-2, 2*(L-1), f't={t[frame]:.1f}s', fontsize=16)
    return line, timelabel

ani = FuncAnimation(fig, func=update, frames=[i for i in range(0, Bouncy_ball.N, 10)], interval=1, blit=True, repeat=True)
plt.show()
