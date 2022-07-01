import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x', real=True)
y = sp.Symbol('y', real=True)



a = 2
b = -2
c = 3

A = np.array([[c,-a],[-a,-b]])
xy_vert = np.array([[x],[y]])
xy_horz = np.array([[x,y]])

function = np.dot(xy_horz, A).dot(xy_vert)
print(f'{function}\n\n{np.linalg.det(A)}')
