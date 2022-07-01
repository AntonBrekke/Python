# Representing a function by a class
# Vanlig høydefunksjon:
def y(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2
"""
Funksjon med to parametere fungerer
normalt, men det finnes eksempler
der de ikke funker så bra. Dersom
man skal sende denne funksjonen
til en annen funksjon kan det
fort oppstå problemer ift. argumenter
og div. Da kan det være lønnsomt å
representere funksjonen med klasser
"""
# Eksempel hvor det går galt:

import numpy as np
import matplotlib.pyplot as plt
"""
def y(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2

def plot_function(f, start, stop):
    x = np.linspace(start, stop, 101)
    plt.plot(x, f(x))

def g(x):
    return x**2-4*x

plot_function(y,0,1)
plt.show()
"""
# Representing a function by a class:
class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

# Usage:
y = Y(v0 = 3)   # Create instance (object)
v = y.value(0.1)    # compute function value


# Fikset kode:
class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2

def plot_function(f,start,stop):
    x = np.linspace(start,stop,101)
    plt.plot(x, f(x))

y1 = Y(v0=3)
y2 = Y(v0=5)

plot_function(y1.value, 0, 1)
plot_function(y2.value, 0, 1)
plt.show()
