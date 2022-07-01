# Exercise E.6 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

# a)
# Funksjon for Heun's metode:
def Heuns_method(T, U0, N):
    u = [0]*(N+1)
    t = [0]*(N+1)
    dt = T/N
    u[0] = U0
    for n in range(N):
        t[n+1] = t[n] + dt
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt*k1, t[n] + dt)
        u[n+1] = u[n] + dt*(k1/2 + k2/2)
    return u, t

def f(u, t):        # diff, u' = u/5
    return u/5

# b)
def exact(T,N):     # Analytisk løsning gitt ved variabler T, N
    t = np.linspace(0,T,N+1)
    return np.exp(t/5)

def test_heuns_against_hand_calculations(): # Testfunksjon
    T = 1
    N = 2       # Løsning i to tidssteg
    U0 = 1
    u1 = Heuns_method(T, U0, N)[0]
    u2 = exact(T,N)
    tol = 1e-3
    for i in range(N+1):    # Tester for alle listeverdier
        success = abs(u1[i] - u2[i]) < tol
        msg = 'something funky'
        assert success, msg

test_heuns_against_hand_calculations()

# c)
def exact_plot(t):      # Analytisk løsning gitt ved en liste / array i argument
    return np.exp(t/5)

# Simulerer approksimasjon
T = 10; U0 = 1
N_list = *range(1,20),
for N in N_list:
    u, t = Heuns_method(T, U0, N)
    plt.plot(t, u,'--', label = 'Heuns method')

    t = np.linspace(0, T, 1000)
    plt.plot(t, exact_plot(t),'r-.', label = 'Analytical')
    plt.legend()
    plt.draw()
    plt.pause(0.3)
    plt.clf()

# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 45 IN1900> python heuns_method_func.py
PS C:\Python\Oblig uke 45 IN1900>
"""
