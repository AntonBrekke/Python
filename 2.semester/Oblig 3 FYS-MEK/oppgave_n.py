from oppgave_k import *

N = method.N
m = method.m
F_net = m * a
T = method.T
# F_net = np.ones((N+1, 2))

integral = 0
for n in range(N):
    dr = r[n+1,0] - r[n,0]
    integral += dr * (F_net[n+1,0] + F_net[n,0]) / 2
print(f'Integral by trapezoid rule: {integral}')


W = np.trapz(F_net[:,0], dx=[r[n+1,0] - r[n,0] for n in range(N)])
print(f'Trapz: {W}')

# From terminal:
"""
PS C:\Desktop\Python\2.semester\Oblig 3 FYS-MEK> python .\oppgave_n.py
Integral by trapezoid rule: 0.005628310153645069
Trapz: 0.005628310153628691
"""
