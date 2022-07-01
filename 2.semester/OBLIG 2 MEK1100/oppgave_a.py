import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
# Dette virker med versjon 7 MAT-filer
data = sio.loadmat('data.mat')
x = data.get('x')
y = data.get('y')
u = data.get('u')
v = data.get('v')
xit = data.get('xit')
yit = data.get('yit')

print(f'shape x = {np.shape(x)}')
print(f'shape y = {np.shape(y)}')
print(f'shape u = {np.shape(u)}')
print(f'shape v = {np.shape(v)}')
print(f'shape xit = {np.shape(xit)}')
print(f'shape yit = {np.shape(yit)}')

print(f'intersections in grid : {len(x[0])*len(y[:,0])}')

print(f'all dx = 0.5 : {np.all(np.diff(x, axis=1)==0.5)}')
print(f'all dy = 0.5 : {np.all(np.diff(y, axis=0)==0.5)}')


# Kjøretest fra terminal:
"""
shape x = (201, 194)
shape y = (201, 194)
shape u = (201, 194)
shape v = (201, 194)
shape xit = (1, 194)
shape yit = (1, 194)
intersections in grid : 38994
all dx = 0.5 : True
all dy = 0.5 : True
first and last y-values :
 -50.0 -50.0
50.0 50.0
"""
