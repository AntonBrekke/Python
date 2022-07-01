import numpy as np
import matplotlib.pyplot as plt
from math import *
import sys
n = True
while n:
    eq = input('Put scalar field equation of 2 variables in Python numpy syntax here:')
    if eq =='':
        sys.exit()
    else:
        n = False
n = True
while n:
    N = input('Type N numbers of level curves:')
    if N =='':
        sys.exit()
    else:
        N = int(float(N))
        n = False
n = True
while n:
    a = input("Input min value here:")
    b = input("Input max value here:")
    if a == '' or b == '':
        sys.exit()
    else:
        a = float(a); b = float(b)
        n = False

equation = f"""
def eq(x,y):
    return {eq}
"""

exec(equation)

I = np.linspace(a, b, 101)
x, y = np.meshgrid(I, I, indexing='ij')

plt.contour(x, y, eq(x,y), N)
plt.axis('equal')
plt.show()
