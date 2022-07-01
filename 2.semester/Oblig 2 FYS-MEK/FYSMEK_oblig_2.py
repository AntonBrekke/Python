import numpy as np
import matplotlib.pyplot as plt

k = 200
g = 9.81
m = 0.1
L_0 = 1
theta = np.pi/6


i = np.array([1,0])
j = np.array([0,1])

T = 10
N = 500

t = np.linspace(0, T, N+1)
a = np.zeros([N+1, 2])
v = np.zeros([N+1, 2])
r = np.zeros([N+1, 2])

v0 =[0,0]; r0 = L_0*np.sin(theta)*i - L_0*np.cos(theta)*j
r[0,:] = r0
R = np.linalg.norm(r[0])
re0 = r[0,:] / R
a[0,:] = -g*j - k*(np.linalg.norm(r0) - L_0)*re0/m
v[0,:] = v0

for n in range(N):
    dt = t[n+1] - t[n]
    v[n+1,:] = v[n,:] + dt*a[n,:]
    r[n+1,:] = r[n,:] + dt*v[n+1,:]
    R = np.linalg.norm(r[n+1,:])
    re = r[n+1,:] / R
    a[n+1,:] = -g*j - k*(R - L_0)*re/m

fig, ax = plt.subplots(3,1)
ax[0].plot(t, a)
ax[0].set_xlim([0, 10])
ax[1].plot(t, v)
ax[1].set_xlim(0, 10)
ax[2].plot(r[:,0], r[:,1])
plt.show()
