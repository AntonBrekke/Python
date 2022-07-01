import numpy as np
import matplotlib.pyplot as plt

class Y:
    def __init__(self, v0):
        self._v0 = v0
        self._g = 9.81

    def __call__(self, t):
        return self._v0*t - 0.5*self._g*t**2

    def __str__(self):
        return f'v0*t - 0,5*g*t**2, v0 = {self._v0}'

    def __repr__(self):
        return f'Y(v0 = {self._v0}) '

y1 = Y(v0=5)
y2 = Y(v0=10)
y3 = eval(repr(y1))
print(y3)

t = np.linspace(0,2)

"""
plt.plot(t,y1(t))
plt.plot(t,y2(t))
plt.axis([0,5,0,10])
plt.show()
"""
