# Exercise E.1 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

# a-c)
# Eksempelfunksjon u' = u/5
def f(u,t):
    return u/5

def ForwardEuler(U0, T, N): # Funksjon for ForwardEuler
    u = [0]*(N+1)       # N+1 elementer fordi vi skal ha N antall steg som gir N+1 antall løsningspunkter
    t = [0]*(N+1)
    dt = T/N        # Steglengde = Intervall / antall
    u[0] = U0
    for k in range(N):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

def exact(t):   # Analytisk løsning
    return 0.1*np.exp(t/5)

U0 = 0.1        # Gitt initialbetingelse
T = 20
N = 4  # Gir gitt delta_t i oppgave (dt = T/N = 5)


# d) Plotter graf:
u, t = ForwardEuler(U0, T, N)
plt.plot(t, u, label = 'Forward Euler')
t = np.linspace(U0, T, 1000)
plt.plot(t, exact(t),'r',label = 'Analytical')
plt.legend()
plt.show()

# f) Simulerer for avtakende dt:
N_list = *range(2, 202, 5),      # Lager en liste med verdier i range (xx, lager [xx])
for N in N_list:
    u, t = ForwardEuler(U0, T, N)
    plt.plot(t, u, label = 'Forward Euler')
    t = np.linspace(U0, T, 1000)
    plt.plot(t, exact(t),'r',label = 'Analytical')
    plt.legend()
    plt.draw()
    plt.pause(0.01)
    plt.clf()

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 45 IN1900> python simple_ODE_func.py
PS C:\Desktop\Python\Oblig uke 45 IN1900>
"""
