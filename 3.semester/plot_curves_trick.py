import numpy as np
import matplotlib.pyplot as plt

v0 = 10
g = 9.81

"""
Om verdiene i en array er avhengig av verdiene i en annen array og du vil unngå looping
"""
theta = np.linspace(0, np.pi/2, 6)
# v0 = np.linspace(0, 10, 6)
# y = v0*np.sin(theta)*t - 0.5*g*t**2 = 0 => t = 2*v0*np.sin(theta) / g
t = np.linspace(0, 2*v0*np.sin(theta)/g, 200)   # Lager en array med en array
print(np.shape(t))

x = v0*np.cos(theta)*t
y = v0*np.sin(theta)*t - 0.5*g*t**2
plt.plot(x,y)
plt.legend(theta)
plt.show()

for th in theta:
    tt = np.linspace(0, 2*v0*np.sin(th)/g, 200)   # Lager en array med en array
    xth = v0*np.cos(th)*tt
    yth = v0*np.sin(th)*tt - 0.5*g*tt**2
    plt.plot(xth,yth)
    # plt.legend(theta)
plt.show()

print(np.shape(y))
print(np.shape(theta[None,:]))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, theta[None,:], y)
ax.set_xlabel('t')
ax.set_ylabel('theta')
plt.show()

for theta, v0 in zip(theta, v0):
    t = np.linspace(0, 2*v0*np.sin(theta)/g, 200)   # Lager en array med en array
    x = v0*np.cos(theta)*t
    y = v0*np.sin(theta)*t - 0.5*g*t**2
    plt.plot(x,y)
    # plt.legend(theta)
plt.show()
