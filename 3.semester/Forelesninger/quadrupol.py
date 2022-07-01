import numpy as np
import matplotlib.pyplot as plt

def efieldlist(r, Q, R):
    E = np.zeros(np.shape(r))
    for i in range(len(R)):
        Ri = r - R[i]
        Rinorm = np.linalg.norm(Ri)
        E += Q[i]*Ri/Rinorm**3
    return E

R = []
Q = []
a = 1.0
r1 = np.array([a,a])
Q1 = 1.0
R.append(r1)
Q.append(Q1)

r2 = np.array([a,-a])
Q2 = -1.0
R.append(r2)
Q.append(Q2)

r3 = np.array([-a,a])
Q3 = -1.0
R.append(r3)
Q.append(Q3)

r4 = np.array([-a,-a])
Q4 = 1.0
R.append(r4)
Q.append(Q4)

L = 5
NL = 20
x = np.linspace(-L, L, NL)
y = np.linspace(-L, L, NL)
rx, ry = np.meshgrid(x, y, indexing='xy')
