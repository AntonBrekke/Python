# Eksempel A
"""
Anta vi har likningen:
u'(t) = a
Hva kan vi lese ut av likningen?
Stigningen i funksjonen er a for alle t.
Altså må u(t) være en rett linje,
og u(t) = a*t + C.

Dersom likningen er på formen:
u(t) = u'(t)
Ser vi at stignigen i et punkt t skal
være lik funksjonen i alle t. Eneste type
funksjon som oppfyller dette kravet er
eksponentialfunksjoner.
Løser vi likinngen får vi et svar på formen:
C*e**t.
"""
# Eksempel C:
"""
En mer avansert likning på formen:
u'(t) = u(t)*(1 - u(t))
Hva kan vi lese ut?
u'(0) = 0
u(t) = 1 gir u'(t) = 0
Når 0 < u(t) < 1, så er stigningen positiv
og u(t) < 0 eller u(t) > 1 er stigningen negaativ
"""

# Finne numeriske løsninger for differensiallikninger
import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f, U0, T, n):
    # n er antall løsningspunkter
    t = np.linspace(0, T, n+1)    # Løsning for [0, T]
    u = np.zeros(n+1)
    u[0] = U0       # Initialbetingelse
    h = T/n
    for n in range(n-1):
        u[n+1] = u[n] + h*f(u[n], t[n])

    return u, t

f = lambda u, t: 1/u
u, t = ForwardEuler(f, U0 = 1, T = 2, n = 50)
plt.plot(t,u)
plt.show()

# ForwardEuler implenetert i klasse:
class ForwardEulerC:
    def __init__(self, f):
        self.f = f

    def set_initial_condition(self, U0):
        self.U0 = U0

    def solve(self, time_points):
        n = time_points.size
        self.t = time_points
        self.u = np.zeros(n)
        self.u[0] = self.U0
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        u = self.u; t = self.t; f = self.f; k = self.k
        dt = t[k+1] - t[k]
        return u[k] + dt * f(u[k], t[k])

f = lambda u, t: u**2 * (1-u) # u'(t) = u**2 * (1-u)

fe = ForwardEulerC(f)
fe.set_initial_condition(0.5)
t = np.linspace(0,5,100)
u, t = fe.solve(t)
plt.plot(t, u)
plt.show()

"""
Det finnes andre metoder som er bedre
enn Forward-Euler.
Flere RungeKutta-metoder er bedre, fordi
funksjonen når approksimasjonen fortere.
I numerisk implementasjon er Forward Euler
og RungeKutta helt like, untatt i metoden
advance(). Dette peker mpt inheritance av klasser.
"""
class ODESolver:
    def __init__(self, f):
        self.f = f

    def set_initial_condition(self, U0):
        if isinstance(U0, (float,int)):  # skalar ODE
            self.neq = 1                 # Antall likninger
            U0 = float(U0)
        else:                            # system av ODEs
            U0 = np.asarray(U0)          # Vektor-ODE
            self.neq = U0.size           # Antall likninger
        self.U0 = U0

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        if self.neq == 1:  # scalar ODEs
            self.u = np.zeros(N)
        else:              # systems of ODEs
            self.u = np.zeros((N,self.neq))

        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0

        # Time loop
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        unew = u[n] + dt*f(u[n], t[n])
        return unew

class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        dt2 = dt/2.0
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt2*k1, t[n] + dt2)
        unew = u[n] + dt*k2
        return unew
