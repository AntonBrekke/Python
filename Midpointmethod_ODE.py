import numpy as np
import matplotlib.pyplot as plt

N = 100       # Antall steg
a = 0       # Nedre grense intervall
b = 2       # Øvre grense intervall
U0 = 1      # Initialbetingelse

u = np.zeros(N+1)
t = np.linspace(a, b, N+1)
u[0] = U0

f = lambda u, t: u*t    # Høyreside av ODE på formen u' = f(u,t)

# Løser ODE med Midtpunktmetoden
for n in range(N):
    dt = t[n+1] - t[n]
    K1 = u[n] + dt/2*f(u[n], t[n])
    K2 = dt/2
    u[n+1] = u[n] + dt*f(u[n] + K1, t[n] + K2)

plt.plot(t, u)
plt.show()
