import ast2000tools.utils as utils
from ast2000tools.relativity import RelativityExperiments
import ast2000tools.constants as const
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

"""
Potensiale rundt et sort hull
"""
c = const.c         # m/s
G = const.G         # m^3 / (kg s^2)
solar_mass = const.m_sun        # kg
kg_to_meter = G / c**2      # m
AU_to_m = const.AU          # m
meter_to_sec = 1 / c        # s
from_deg_to_rad = np.pi / 180   # rad

v = 0.993
m = 4e6 * solar_mass        # kg
R = 20*m
gamma = 1 / np.sqrt(1 - v**2)
theta = 167 * from_deg_to_rad

# oppgave 5

L_m = R*gamma*v*np.sin(theta)       # pr. masse m, m er egt ukjent i denne oppgaven
E_m = np.sqrt(1 - 2*m / R)*gamma
r = np.linspace(2, 30, 1001)       # i enheter av m
r_max = (L_m)**2 / (2*m) * (1 - np.sqrt(1 - 12*m**2 / L_m**2)) / m      # I enhet av m

print(f'Energy pr. mass: {E_m} [-]')
print(f'Spin pr. mass: {L_m} [kg]')

def V(r):
    return np.sqrt((1 - 2*m/(r*m)) * (1 + (L_m/(r*m))**2))    # Plotter i enheter av m

plt.plot(r, V(r), label=r'$V(r)$')
plt.plot(r_max, V(r_max), 'ro', label=r'$\frac{E_{crit}}{m}$')
plt.plot(r, E_m*np.ones_like(r), color='orange', linestyle ='--', label=r'$\frac{E}{m}$')
plt.xlabel('r (pr. unit M) [-]', weight='bold', fontsize=18)
plt.ylabel('V(r)', weight='bold', fontsize=18)
plt.xticks(r[::200])
plt.legend(prop={'size': 14})
plt.show()


"""
Løser et integral fordi det var for avansert for
Wolfram Alpha ... (til og med pro)
"""
r = sp.Symbol('r', positive=True)
M = sp.Symbol('M', positive=True)

f = 1/sp.sqrt((E_m)**2 - (1 - 2*M/r))

tau = sp.integrate(f, (r, 0, 2*M))

print(f'Integral (expressed nicely): {sp.N(tau, 4)}')
tau_func = sp.lambdify(M, tau)
print(f'{tau_func(m * kg_to_meter * meter_to_sec)} seconds')
