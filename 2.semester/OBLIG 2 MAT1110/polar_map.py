import numpy as np
import matplotlib.pyplot as plt

# setting the radius
a = 1
radius = a/2

# creating an array containing the
# radian values
rads1 = np.arange(-np.pi/4, np.pi/4, 0.0001)
rads2 = np.arange(3*np.pi/4, 5*np.pi/4, 0.0001)
# plotting the lemniscate
r1 = np.sqrt(a*np.cos(2*rads1))
r2 = np.sqrt(a*np.cos(2*rads2))

# Plotting r on theta
rp = r1
rn = -r1
plt.plot(rads1, rp, 'r', label=r'$r=\sqrt{cos(2\theta)},\,\theta\in\left[-\frac{\pi}{4},\,\frac{\pi}{4}\right]$')
plt.plot(rads1, rn, 'b', label=r'$r=-\sqrt{cos(2\theta)},\,\theta\in\left[-\frac{\pi}{4},\,\frac{\pi}{4}\right]$')
rp = r2
rn = -r2
plt.plot(rads2, rp, 'tab:orange', label=r'$r=\sqrt{cos(2\theta)},\,\theta\in\left[\frac{3\pi}{4},\,\frac{5\pi}{4}\right]$')
plt.plot(rads2, rn, 'g', label=r'$r=-\sqrt{cos(2\theta)},\,\theta\in\left[\frac{3\pi}{4},\,\frac{5\pi}{4}\right]$')
plt.plot([np.min(rads1)-1, np.max(rads2)+1],[0,0],'k')

plt.plot([0,0],[-a-1,a+1], 'k--')

plt.xlabel(r'$\theta$', fontsize=15, fontweight='bold', rotation=0)
plt.ylabel('r', fontsize=15, fontweight='bold', rotation=0)

ticks = [-np.pi/4*(1-k) for k in range(7)]
ticks_text = [r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$']
for i in range(len(ticks)):
    plt.plot([ticks[i], ticks[i]], [0,0], 'yellow', marker='o', markersize=6)
    plt.text(ticks[i]+0.1, -0.3, ticks_text[i])
plt.ylim([-2,3])
plt.legend(prop={'size':10}, mode='expand', ncol=2)
plt.show()


# setting the axes projection as polar
fig, axes = plt.subplots(1,2,subplot_kw={'projection': 'polar'})
# Changing tickmarks
xT = plt.xticks()[0]
xL = [r'$0,\,2\pi$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$' ,\
    r'$\pi$', r'$\frac{5\pi}{4}$', r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
plt.setp(axes, xticks=xT, xticklabels=xL)
axes[0].set_title(r'$r=\pm\sqrt{cos(2\theta)},\,\theta\in\left[-\frac{\pi}{4},\,\frac{\pi}{4}\right]$')
axes[0].plot(rads1, r1, 'r')
axes[0].plot(rads2, r2, 'b')
axes[0].set_rlabel_position(75)

axes[1].set_title(r'$r=\pm\sqrt{cos(2\theta)},\,\theta\in\left[\frac{3\pi}{4},\,\frac{5\pi}{4}\right]$')
axes[1].plot(rads1, r1, 'green')
axes[1].plot(rads2, r2, 'tab:orange')
axes[1].set_rlabel_position(75)

# display the Polar plot in ranbows! :D
# axes[0].scatter(rads1, r1, c=rads1, s=2*np.pi*radius**2, cmap='hsv', alpha=0.75)
# axes[0].scatter(rads2, r2, c=rads1, s=2*np.pi*radius**2, cmap='hsv', alpha=0.75)
fig.tight_layout()
plt.show()
