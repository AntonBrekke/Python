"""
Vi har følgende system:
x'(t) = y(t)
y'(t) = -x(t)

Vi vil finne løsning for t i [0, 6] når x(0) =1, y(0) = 0.
Hvis y(t) antas kjent kan vi finne x(t) med ForwardEuler
og vice-versa.

x'(t) = y(t), x(0) = 0
y'(t) = -x(t), y(0) = 1
"""
# Bruk:
from ODESolver import *
import numpy as np

def f(u,t):
    return np.array([u[1], -u[0]])

metode = ForwardEuler(f)
metode.set_initial_condition(U0 = [0, 1])
timepoints = np.linspace(0, 6, 400)
u, t = metode.solve(timepoints)

import matplotlib.pyplot as plt

plt.plot(u[:,0], u[:,1])  # Todimensjonale arrays, y(t) mot x(t)
plt.title("Faseportrett")
plt.show()
