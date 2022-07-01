import numpy as np
from numpy import linspace
n = 5       # Number of points
x = np.linspace(0, 1, n)    #n ponts in [0,1]
y = np.zeros(n)     # n zeros (float data type)
for i in range(n):
    y[i] = f(x[i])
print(y)


"""
Can work with entire arrays at once
instead of one element at a time
"""

from math import sin

for i in range(len(x)):
    y[i] = sin(x[i])
"""
Instead of looping every element, it is
much more efficient to run an array
"""
# More effecient code if x is array:
import numpy as np
y = np.sin(x)
"""
Vectorization gives shorter, much more readable
code, and faster code. Also closer to the mathematics.
"""

# A function f(x) written as a number x usually works for array x too:
from numpy import sin, exp, linspace

def f(x):
    return x**3 + sin(x)*exp(-3*x)

x = 1.2
y = f(x)

x = linspace(0, 3, 10001)
y = f(x)

# Very important application:
"""
vectorized code for computing points
along a curve.
Vectorization is basially something
you can make to replace loops to make
the code more effective.
"""

import numpy as np
n = 100
x = np.linspace(0, 4*pi, n+1)
y = 2.5 + x**2*np.exp(-0.5*x)*np.sin(x-p/3)
