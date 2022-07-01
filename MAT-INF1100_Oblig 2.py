import numpy as np
import matplotlib.pyplot as plt

N = 0
v0 = 0, t = 0
for i in range(N+1):
    v0 += v[i]
    t += t[i]

a = (v0 - v[0])/t
