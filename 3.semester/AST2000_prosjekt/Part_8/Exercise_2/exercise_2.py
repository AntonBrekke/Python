import ast2000tools.utils as utils
from ast2000tools.relativity import RelativityExperiments
import scipy.constants as sc
import numpy as np

seed = utils.get_seed('antonabr')
experiment = RelativityExperiments(seed)
c = sc.c
# experiment.cosmic_pingpong(6)

v = 0.65
gamma = 1 / np.sqrt(1 - v**2)

# Umerkede koordinater
xA = 0
tA = 0
xC = 0

# Merkede koordinater
xAm = 0
tAm = 0
xBm = 400       # km
tBm = 1.33765   # ms
xCm = 260.661
tCm = 1.33765
xDm = 0
tDm = 2.67529

# Finner Lm (= xBm)
Lm = tBm * 1e-3 * c / 1000           # km
print(f'Lm = {Lm}km')

# Finner tC
tC = np.sqrt((tBm*1e-3)**2 - (xCm*1000 / c)**2) * 1e3            # ms
print(f'tC = {tC}ms')

# Finner tB
tB = 1/2 * ((tC*1e-3)**2 + (xCm*1e3/c - xBm*1e3/c)**2 - (tCm*1e-3 - tBm*1e-3)**2) / (tC*1e-3) * 1e3    # ms
print(f'tB = {tB}ms')
# Finner xB
xB = tB * 1e-3 * c / 1000           # km
print(f'xB = {xB}km')
# Finner tD
tD = 2*gamma*tBm
print(f'tD = {tD}ms')
print(f'xD = {-v*c*tD*1e-6}km')

print(f'Difference between tD and tB: {tD - tB}ms')
