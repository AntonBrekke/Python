import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 100
v0 = 1
time = 2
n = 101

v = np.zeros(n)
x = np.zeros(n)
 for i in range(0, n-1):
     F = -k*x[i]
     v[i+1] = v[i] + a*dt
     x[i+1] = x[i] + v[i+1]*dt
     t[i+1] = t[i] + dt
