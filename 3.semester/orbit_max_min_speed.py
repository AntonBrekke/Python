import numpy as np
import scipy.constants as scs

def speeds(m, r):
    vmin = np.sqrt(scs.G*m / r)
    vmax = np.sqrt(2*scs.G*m / r)
    return vmin, vmax



r_p = 1861.74 * 10**3           # m
# r_p = 6371 * 10**3       # Jorda, m
r = 2000 * 10**3                # m
R = r_p + r

# M = 5.97e24             # Jorda kg
M = 1.63e23             # Jorda kg

vmin, vmax = speeds(M, R)
print(f'vmin = {vmin}m/s, vmax = {vmax}m/s')
print(f'vmin = {3.6*vmin}km/t, vmax = {3.6*vmax}km/t')
