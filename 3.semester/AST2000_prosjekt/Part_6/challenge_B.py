'''
SNARVEI OG EGEN KODE
'''

import numpy as np
import matplotlib.pyplot as plt
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission, LandingSequence
import ast2000tools.utils as utils
import ast2000tools.constants as const
from ast2000tools.shortcuts import SpaceMissionShortcuts
import scipy.constants as scs

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)
mission = SpaceMission.load('mission_after_launch.pickle')
print('Look, I am still in space:', mission.rocket_launched)

'''Shortcut begin'''

# code_stable_orbit = 95927
# code_orientation = 43160
# system = SolarSystem(seed)
#
# shortcut = SpaceMissionShortcuts(mission, [code_stable_orbit, code_orientation])
#
# # Orientation software shortcut
# pos, vel, angle = shortcut.get_orientation_data()
# print("Position after launch:", pos)
# print("Velocity after launch:", vel)
#
# #Verifying orientation with shortcut data
# mission.verify_manual_orientation(pos, vel, angle)
#
# # Initialize interplanetary travel instance
# travel = mission.begin_interplanetary_travel()
#
# # Shortcut to make the landing sequence class start with a stable orbit
# shortcut.place_spacecraft_in_stable_orbit(0, 1000e3, 0, 1)
#
# # Initializing landing sequence class instance
# landing = mission.begin_landing_sequence()
#
# # Calling landing sequece oreint function
# t, pos, vel = landing.orient()
#
# print("We are at:")
# print("Time :", t)
# print("pos :", pos)
# print("vel :", vel)

'''Shortcut end'''

'''
EGEN KODE
'''
"""
Data: [lambda, sigma, fluks]

sigma_noise_load = np.loadtxt('sigma_noise.txt')
spectrum_load = np.loadtxt('spectrum_seed97_600nm_3000nm.txt')[:, -1]

data = np.zeros((len(sigma_noise_load[:,0]), 3))
data[:,0] = sigma_noise_load[:,0]
data[:,1] = sigma_noise_load[:,1]
data[:,2] = spectrum_load[:]

np.save('data', data)
"""


"""
Kan slice hvert hundrede, data[]
"""

data = np.load('data.npy')

c = const.c
k = const.k_B
lmbda0 = 632     # nm
m = 2 * 8 * (scs.m_p + scs.m_n) # kg
T = 300             # K
v_rel = 10000           # m/s

d_lmbda = v_rel / c * lmbda0      # nm
# print(d_lmbda / 2)
lmbdas = data[:,0].T
sigmas = data[:,1].T
Fs = data[:,2].T

def sigma(lmbda0, m, T):
    return 2*lmbda0 / c * np.sqrt(k*T / (4*m))

sgma = sigma(lmbda0, m, T)

def F(lmbda, lmbda0, sigma, Fmin):
    f = 1 + (Fmin - 1)*np.exp(-0.5*((lmbda - lmbda0) / sigma)**2)
    return f

index = np.logical_and(lmbdas >= lmbda0 - d_lmbda/2, lmbdas <= lmbda0 + d_lmbda/2)
plt.plot(lmbdas[index], F(lmbdas[index], lmbda0, sgma, 0.5))
plt.plot(lmbdas[index], Fs[index])
plt.plot(lmbdas[index], (Fs[index] - F(lmbdas[index], lmbda0, sgma, 0.5))**2)
plt.show()

def X_squared(fi, sigma_d, lmbda0):
    index = np.logical_and(lmbdas >= lmbda0 - d_lmbda/2, lmbdas <= lmbda0 + d_lmbda/2*1.1)
    sigma_d = sigma_d.copy()[index]
    fi = fi.copy()[index]
    print(fi.size)
    lmbd = lmbdas.copy()[index]
    Fmin = np.linspace(0, 0.7, len(fi))
    X = np.zeros((len(fi), len(fi), len(fi)))
    for i in range(len(fi)):
        for j in range(len(fi)):
            # F = fti
            for k in range(len(fi)):
                X[i,j,k] = np.sum(((fi - F(lmbd[i], lmbda0, sgma, Fmin[j])) / sigma_d[k])**2, axis=0)
    min = np.min(X)
    where = np.where(X==min)
    # print(where[0][50:100])
    print(min, where, X[where])
    return min

X_squared(Fs, sigmas, lmbda0)
