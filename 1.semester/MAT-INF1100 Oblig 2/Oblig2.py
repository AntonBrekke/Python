# Oblig 2 MAT-INF1100
import numpy as np
import matplotlib.pyplot as plt

# Oppgave 1
t = []
v = []
infile = open('running.txt','r')
for line in infile:
    tnext, vnext = line.strip().split(',')
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()

# a)
def a(t):
    a = [0]*len(t)
    for i in range(1, len(t)):  # Antar at v = 0 i t = 0
        a[i] = (v[i] - v[i-1]) / (t[i] - t[i-1])
    return a

# plt.plot(t, a(t), 'r', label = 'Acceleration')
plt.xlabel('Time')
plt.legend()
# plt.savefig('Acceleration_time.png')
# plt.show()

# b)
def s(t):
    s = [0]*len(t)
    for i in range(1, len(t)):  # Vet at s(0) = 0
        s[i] = s[i-1] + ((v[i-1] + v[i])*(t[i] - t[i-1])) / 2       # Trapesmetoden
    return s

# c)
# plt.plot(t, s(t), 'k', label = f'Distance, Total length of run = {s(t)[-1]:.2f}')
plt.xlabel('Time')
plt.legend()
# plt.savefig('Distance_time.png')
# plt.show()

# Oppgave 2
# b)
import numpy as np
import matplotlib.pyplot as plt

"""
For oppgave b og c lager jeg en klasse for å løse differensiallikninger.
Klassen vil inneholde metodene Forward-Euler og Euler-Midpoint (RungeKutta2).
"""
class ODESolver:
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

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        return u[k] + dt * f(u[k], t[k])

class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = f(u[k], t[k])
        K2 = f(u[k] + dt2*K1, t[k] + dt2)
        unew = u[k] + dt*K2
        return unew

# Differensial-likning u' = u*(1/2 - u) / u' = f(u, t)
f = lambda u, t: u*(0.5 - u)

# Eksakt funksjon:
def x(t):
    return (np.exp(t/2)) / (2*np.exp(t/2) - 1)

# b)
U0 = 1      # Initialbetingelse
# Intervall [0, 3]
T_0 = 0
T = 3

N = 6      # Antall steg
time_points = np.linspace(T_0, T, N+1)      # N+1 fordi vi skal ha steg, + 0. T/N = 0.5 , [0 0.5 1 1.5 2 2.5 3] er 0 til 3 fordelt på 7 punkter

fe = ForwardEuler(f)
fe.set_initial_condition(U0)
u, t = fe.solve(time_points)
# plt.plot(t,u,'royalblue', label = 'Forward Euler method')

t = np.linspace(T_0, T, 1000)        # Ny for å gjøre den eksakte grafen smooth
# plt.plot(t, x(t),'r', label='Analytical form')

plt.xlabel(f'$D_f\,x(t)\in[{T_0},{T}]$,')
plt.title(r"Analytical: ${x'}=x\cdot(\frac{1}{2}-x)\Rightarrow x(t)=\frac{e^{\frac{t}{2}}}{2\cdot e^{\frac{t}{2}}-1}$")
plt.legend()
# plt.savefig('Forward-Euler.png')
# plt.show()

# c)
U0 = 1      # Initialbetingelse
# Intervall [0, 3]
T_0 = 0
T = 3
N = 6       # Antall steg
time_points = np.linspace(T_0, T, N+1)  # N+1 fordi vi skal ha steg, + 0. T/N = 0.5 , [0 0.5 1 1.5 2 2.5 3] er 0 til 3 fordelt på 7 punkter
# Plotting
fe = ForwardEuler(f)
fe.set_initial_condition(U0)
u, t = fe.solve(time_points)
# plt.plot(t, u, 'royalblue',label = 'Forward Euler method')

mp = ExplicitMidpoint(f)
mp.set_initial_condition(U0)
u, t = mp.solve(time_points)
# plt.plot(t, u, 'g',label = 'Midtpoint method')

t = np.linspace(T_0, T, 1000)        # Ny for å gjøre den eksakte grafen smooth
# plt.plot(t, x(t),'r', label='Analytical form')

plt.xlabel(f'$D_f\,x(t)\in[{T_0},{T}]$,')
plt.title(r"Analytical: ${x'}=x\cdot(\frac{1}{2}-x)\Rightarrow x(t)=\frac{e^{\frac{t}{2}}}{2\cdot e^{\frac{t}{2}}-1}$")
plt.legend()
# # plt.savefig('Midpoint-Euler.png')
# plt.show()

# d)
"""
Forklar hvorfor løsningen x(t) alltid vil være begrenset av 1/2 ≤
x(t) ≤ 1 for t ≥ 0. Gjelder den samme begrensningen for Eulers
metode for steglengden fra b), uansett hvor mange tidssteg du tar?
Begrunn svaret ditt.
"""
U0 = 1      # Initialbetingelse
# Intervall [0, 3]
T_0 = 0
T = 12

N = 12      # Antall steg
time_points = np.linspace(T_0, T, N+1)      # N+1 fordi vi skal ha steg, + 0. T/N = 0.5 , [0 0.5 1 1.5 2 2.5 3] er 0 til 3 fordelt på 7 punkter

fe = ForwardEuler(f)
fe.set_initial_condition(U0)
u, t = fe.solve(time_points)
print(u)
plt.plot(t,u,'royalblue', label = 'Forward Euler method')

t = np.linspace(T_0, T, 1000)        # Ny for å gjøre den eksakte grafen smooth
plt.plot(t, x(t),'r', label='Analytical form')

plt.xlabel(f'$D_f\,x(t)\in[{T_0},{T}]$,')
plt.title(r"Analytical: ${x'}=x\cdot(\frac{1}{2}-x)\Rightarrow x(t)=\frac{e^{\frac{t}{2}}}{2\cdot e^{\frac{t}{2}}-1}$")
plt.legend()
# plt.savefig('Forward-Euler-2.png')
plt.show()
