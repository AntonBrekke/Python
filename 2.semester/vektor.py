import numpy as np
import matplotlib.pyplot as plt


g = 9.81
m = 10
v0 = 0
r0 = 0
dt = 0.1
n = 100

t = np.zeros(n)
r = np.zeros([n,2])
v = np.zeros([n,2])
a = np.zeros([n,2])

r[0,:] = r0
t[0] = 0
v[0,:] = v0
a[0,:] = 0

i = 0
while r[i,1] >= 0 and i<n:
    Fnet = -m*g*np.array([0,1])
    a[i,:] = Fnet/m
    v[i+1,:] = v[i,:] + a[i,:]*dt
    r[i+1,:] = r[i,:] + v[i+1,:]*dt
    t[i+1] = t[i] + dt
    i += 1
