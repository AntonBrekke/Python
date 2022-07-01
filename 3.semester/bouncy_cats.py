import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from tqdm import trange

class Bouncy_cat():
    box_L = 20
    a = -9.81
    sim_time = 10       # s
    dt = 0.01
    N = int(sim_time / dt)

    background = plt.imread('cat_background.png')
    cat_1img = plt.imread('cat_1.png')
    cat_2img = plt.imread('cat_2.png')
    cat_3img = plt.imread('cat_3.png')
    img_background = OffsetImage(background, zoom=0.33)
    img_box_cat_1 = OffsetImage(cat_1img, zoom=0.15)
    img_box_cat_2 = OffsetImage(cat_2img, zoom=0.25)
    img_box_cat_3 = OffsetImage(cat_3img, zoom=0.08)
    def __init__(self):
        self.v0 = np.random.normal(0, 5, 2)
        self.r0 = np.random.uniform(0, Bouncy_cat.box_L*0.8, 2)
        self.N = Bouncy_cat.N
        self.r = np.zeros((self.N, 2))
        self.v = np.zeros((self.N, 2))
        self.annotation_array = np.empty((self.N), dtype=object)
        obj = np.random.randint(1,4)
        if obj == 1:
            self.cat_type = Bouncy_cat.img_box_cat_1
        elif obj == 2:
            self.cat_type = Bouncy_cat.img_box_cat_2
        elif obj == 3:
            self.cat_type = Bouncy_cat.img_box_cat_3

    def bounce_ball(self):
        v0 = self.v0
        r0 = self.r0
        v = self.v
        r = self.r
        a = np.array([0, Bouncy_cat.a])
        dt = Bouncy_cat.dt

        v[0] = v0
        r[0] = r0
        self.annotation_array[0] = AnnotationBbox(self.cat_type, (r0), frameon=False)
        for i in range(self.N-1):
            if r[i,0] <= 0 or r[i,0] >= Bouncy_cat.box_L:
                v[i,0] *= -1
            if r[i,1] <= 0:
                v[i,1] *= -1
            v[i+1] = v[i] + a*dt
            r[i+1] = r[i] + v[i]*dt
            self.annotation_array[i+1] = AnnotationBbox(self.cat_type, (r[i+1]), frameon=False)
        return r

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, Bouncy_cat.box_L)
ax.set_ylim(0, Bouncy_cat.box_L)

def num_balls(n):
    balls = np.zeros((n, Bouncy_cat.N, 2))
    cats = np.empty((n, Bouncy_cat.N), dtype=object)
    for i in trange(n, desc='Generating cats'):
        ball = Bouncy_cat()
        r = ball.bounce_ball()
        balls[i,:,:] = r
        cats[i,:] = ball.annotation_array
    return balls, cats

bcground_box = AnnotationBbox(Bouncy_cat.img_background, (Bouncy_cat.box_L/2, Bouncy_cat.box_L/2 + 1), frameon=False)
bcground = ax.add_artist(bcground_box)
n = 3
balls_array, cats_array = num_balls(n)
def update(frame):
    cats = np.empty((n), dtype=object)
    line, = ax.plot(balls_array[:,frame,0], balls_array[:,frame,1], color='k', marker='o', markersize=1, linewidth=0)
    for i in range(n):
        cats[i] = ax.add_artist(cats_array[i, frame])
    return line, *cats,

ani = FuncAnimation(fig, func=update, frames=[i for i in range(0, Bouncy_cat.N, 5)], interval=0, blit=True, repeat=True)
plt.show()
