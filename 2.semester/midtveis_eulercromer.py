import numpy as np
import matplotlib.pyplot as plt

N = 1000
T = 10

r_0 = (0,50)
v_0 = (0,0)
m = 5
g = 9.81
D = 2
Q = 2.2
w = 2


i = np.array([1,0])
j = np.array([0,1])
G = -m*g*j
W = w*i

t = np.linspace(0, T, N+1)
r = np.zeros([N+1,2])
v = np.zeros([N+1,2])
a = np.zeros([N+1,2])

def acceleration(y,v):
    F_d = -D*abs(v-W)*(v-W)
    F_w = Q*abs(W)*W
    acc = (F_d + F_w + G)/m
    return acc

# Setter initialbetingelser
r[0,:] = r_0
v[0,:] = v_0
a[0,:] = acceleration(r[0,:], v[0,:])
# Bruker Euler-Cromer
for n in range(N):
    dt = t[n+1] - t[n]
    v[n+1] = v[n,:] + dt*a[n,:]
    r[n+1] = r[n,:] + dt*v[n+1,:]
    a[n+1] = acceleration(r[n+1,:], v[n+1,:])
    if r[n+1, 1] < 0:
        break

plt.plot(r[:,0], r[:,1])
plt.show()
