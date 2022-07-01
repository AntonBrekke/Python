import numpy as np
import matplotlib.pyplot as plt

m = 70
d = 50
h = 100
k = 40
D = 0.8
g = 9.81
time = 60
dt = 0.001

n = int(time/dt)

t = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)

x[0] = h
t[0] = 0
v[0] = 0

for i in range(n-1):
    if x[i] <= h-d:
        Fk = k*(h-d-x[i])
    else:
        Fk = 0
    Fd = -D*v[i]*abs(v[i])
    Fg = -m*g
    a[i] = (Fk + Fd + Fg)
    v[i+1] = v[i] + dt*a[i]
    x[i+1] = x[i] + dt*v[i+1]
    t[i+1] = t[i] + dt

fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
ax1.plot(t,x)
ax2.plot(t,v)
plt.show()
