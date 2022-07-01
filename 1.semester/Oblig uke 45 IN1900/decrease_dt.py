# Exercise E.4 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

def f(x,t):         # diff, x' = cos(6t)/(1 + t + x)
    return np.cos(6*t)/(1 + t + x)

# Funksjon for ForwardEuler metoden:
def ForwardEuler(U0, T, N):
    x = [0]*(N+1)
    t = [0]*(N+1)
    dt = T/N
    x[0] = U0
    for k in range(N):
        t[k+1] = t[k] + dt
        x[k+1] = x[k] + dt*f(x[k], t[k])
    return x, t

n_list = [20, 30, 35, 40, 50, 100, 1000, 10000]     # Vet oppgaven sier {}, men det er tullete 

# Plotter alle funksjoner inn i en graf:
for n in n_list:
    x, t = ForwardEuler(1, 10, n)
    plt.plot(t, x, label =f'n = {n}')

plt.legend(loc='upper right')
plt.show()

# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 45 IN1900> python decrease_dt.py
PS C:\Python\Oblig uke 45 IN1900>
"""
