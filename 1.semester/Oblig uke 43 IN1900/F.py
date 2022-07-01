# Exercise 8.3 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

class F:
    def __init__(self, n, m):   # Setter opp konstruktør med argumenter n og m
        self.n = n
        self.m = m

    def __call__(self, x):
        k = np.sin(self.n*x)*np.cos(self.m*x)   # Regner ut med formel gitt i oppgave
        return k

# Class usage:
u = F(1,50)      # Lager objekt med verdi 1 og 1
v = F(1,30)      # Lager objekt med verdi 2 og 3
x_values = np.linspace(0,2*np.pi,1000)      # Array med x verdier

plt.plot(u(x_values),v(x_values))       # Samme som u.__call__(x_values), v.__call__(x_values)
plt.xlabel('u(x)')
plt.ylabel('v(x)')
plt.show()

# Kjøretest fra temrinal:
"""
PS C:\Desktop\Python\Oblig uke 43 IN1900> python .\F.py
PS C:\Desktop\Python\Oblig uke 43 IN1900>
"""
