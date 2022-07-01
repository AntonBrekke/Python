# Collect points on a function curve y = f(x):
def f(x):
    return x**3

n = 5       # Number of points
dx = 1.0/(n-1)      # x spacing in [0,1]

x = []
y = []

for i in range(n):
     x.append(i*dx)
     y.append(f(x))


# Turn list into Numerical Python (NumPy) arrays:
import numpy as np  # Module for arrays
x = np.array(xlist)
y = np.array(ylist)
