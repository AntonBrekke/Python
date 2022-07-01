import numpy as np
import matplotlib.pyplot as plt

# c)
# Størrelser funnet i oppgave
mean = 0
lmbda = 1   # Bare setter lambda til en verdi
std = 1 / (np.sqrt(2)*lmbda)
A = np.sqrt(lmbda)

# Definerer punkter og plot-område
n = 5
m = 1
x1 = mean - m*std
x2 = mean + m*std
x = np.linspace(mean - n*std, mean + n*std, 1000)

def psi_absq(x):
    return A**2 * np.exp(-2*lmbda*abs(x))   # Uttrykk for |psi|^2 fra oppgave

# Lager plot
plt.plot(x, psi_absq(x), 'royalblue', linewidth=2, label=r'$|\Psi|^2$')
plt.plot([0,0], [0, psi_absq(mean)], 'k--')
plt.plot([x1, x2], [psi_absq(x1), psi_absq(x2)], 'k', linewidth=2)
plt.plot(x1, psi_absq(x1), 'ro')
plt.plot(x2, psi_absq(x2), 'ro')
plt.plot([x1, x1], [0, psi_absq(x1)], 'r--')
plt.plot([x2, x2], [0, psi_absq(x2)], 'r--')
plt.text(x1 - 0.6, -0.1, r'$\langle x \rangle - \sigma$', fontsize=14, color='r')
plt.text(x2 - 0.1, -0.1, r'$\langle x \rangle + \sigma$', fontsize=14, color='r')
plt.text(mean - 0.1, -0.1, r'$\langle x \rangle$', fontsize=14, color='k')

plt.ylim(-0.2, 1.1)

plt.xlabel('x [m]', weight='bold')
fill_area = np.logical_and(x <= x2, x >= x1)
plt.fill_between(x, psi_absq(x), where=fill_area, alpha=0.4, color='green')

plt.legend()
plt.show()

# d)
dx = (x[-1] - x[0]) / (len(x) - 1)  # Finner dx i array
prob = np.sum(psi_absq(x[fill_area])) * dx  # Enkleste mulige integral
print(prob, 1 - prob)       # Printer sannsynlighet for inni og utenfor
analytic_prob = 1 - np.exp(-2*lmbda*std)    # Sammenlikner med analytisk uttrykk
print(analytic_prob, 1 - analytic_prob)     # Printer sannsynlighet for inni og utenfor

# Kjøretest fra terminal:
"""
C:> python oppgave_4.py
0.7572208623942253 0.24277913760577474
0.7568832655657858 0.24311673443421422
"""
