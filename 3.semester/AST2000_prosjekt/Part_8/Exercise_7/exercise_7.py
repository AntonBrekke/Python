import ast2000tools.utils as utils
from ast2000tools.relativity import RelativityExperiments

seed = utils.get_seed('antonabr')
experiment = RelativityExperiments(seed)

"""
experiment.antimatter_spaceship(6)
"""

import scipy.constants as sc
import numpy as np
# Lager konstanter hentet fra MCast og scipy i SI-enheter
h = sc.h            # Plancks konstant
c = sc.c            # Lyshastighet i vakum
m = 1e6             # Masse skip (kg)
v = 0.267254*c      # Skip fart målt i MCast (v_B = -v_A)

N = 6.34794e41          # Antall fotoner utstrålt
Etot = 2*(m*c**2 + 0.5*m*v**2)          # Energi kommer fra to romskip med samme hvile-energi og kinetisk energi

l = h*c*N / Etot            # Utrykk for lambda
print(f'{l*10**9}nm')

l_n = l / c     # Fra SI til naturlige
v_n = v / c     # Fra SI til naturlige

dl = (np.sqrt((1 + v_n) / (1 - v_n)) - 1)*l_n       # Gjelder naturlige enheter
l_obs_other = abs(l_n - dl)*c      # Fra naturlige til SI

print(f'{l_obs_other*10**9}nm')

"""
Rødt: 625 - 750 nm
Blått: 450 - 485 nm
"""

# 4-vectors
v_A = v / c
gamma = 1 / np.sqrt(1 - v_A**2)
PmuA = (gamma*m, gamma*m*v_A, 0, 0)
PmuB = (gamma*m, gamma*(-m*v_A), 0, 0)

PmupA = (m, 0)
gamma_rel = np.sqrt(1 + (2*v_A / (1 + v_A**2))**2)
v_rel = -2*v_A / (1 + v_A**2)
PmupB = (gamma_rel*m, v_rel*gamma_rel*m - gamma_rel*v_rel)

print(PmuA, PmuB)
print(PmupA, PmupB)
