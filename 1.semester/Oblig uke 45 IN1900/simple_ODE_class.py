# Exercise E.2 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

# a - d)
# Setter opp en ODESolver:
class ForwardEuler_v1:
    def __init__(self, f, U0, T, N):
        self.f, self.U0, self.T, self.N = f, U0, T, N
        self.dt = T/N
        self.u = np.zeros(self.N+1)
        self.t = np.zeros(self.N+1)

    def solve(self):
        self.u[0] = float(self.U0)
        for n in range(self.N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.u, self.t

    def advance(self):
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        unew = u[n] + dt*f(u[n], t[n])
        return unew

# Funksjon implementert som klasse:
class Function:
    def __init__(self, R, U0):
        self.R, self.U0 = R, U0

    def __call__(self, u, t):
        return u/self.R

U0 = 0.1        # Initialbetingelse
T = 20          # Intervall [0,20]
N = 4           # I fire steg, steglengde = 5

# Numerisk plot:
problem = Function(5, U0)
method = ForwardEuler_v1(problem, U0, T, N)
time_points = np.linspace(0, T, N+1)   # T = 20 og N=4 så dt = 5 slik som i E.1
u, t = method.solve()
plt.plot(t, u, label = 'ForwardEuler-Method')

# Analytisk plot:
t = np.linspace(0,20,1000)
def A(t):
    return np.exp(t/problem.R)/10
plt.plot(t, A(t),'r', label = 'Anaytical')

# Plot:
plt.legend()
plt.show()

# f)
def exact(t):   # Analytisk løsning
    return 0.1*np.exp(t/5)

# Simulering for mindre dt:
N_list = *range(2,202,5),
for N in N_list:
    method = ForwardEuler_v1(problem, U0, T, N)
    u, t = method.solve()
    plt.plot(t, u, label = 'Forward Euler')
    t = np.linspace(0, T, 1000)
    plt.plot(t, exact(t),'r',label = 'Analytical')
    plt.legend()
    plt.draw()
    plt.pause(0.01)
    plt.clf()

# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 45 IN1900> python simple_ODE_class.py
PS C:\Python\Oblig uke 45 IN1900>
"""
