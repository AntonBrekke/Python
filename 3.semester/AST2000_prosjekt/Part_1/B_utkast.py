import ast2000tools.constants as const
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission
import numpy as np
import random
import scipy.constants as sc
import matplotlib.pyplot as plt
import time

def timer(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = f(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{f.__name__} ran in {t2} seconds')
        return result

    return wrapper

# print('One astronomical unit is defined as', const.AU, 'meters.')

seed = utils.get_seed('antonabr')
"""
"""
system = SolarSystem(seed)
print('My system has a {:g} solar mass star with a radius of {:g} kilometers.'
      .format(system.star_mass, system.star_radius))

for planet_idx in range(system.number_of_planets):
    print('Planet {:d} is a {} planet with a semi-major axis of {:g} AU.'
          .format(planet_idx, system.types[planet_idx], system.semi_major_axes[planet_idx]))

# print(help(system))
print(system.has_moons)     # True
system.print_info()

mission = SpaceMission(seed)

home_planet_idx = 0 # The home planet always has index 0
print('My mission starts on planet {:d}, which has a radius of {:g} kilometers.'
      .format(home_planet_idx, mission.system.radii[home_planet_idx]))

print('My spacecraft has a mass of {:g} kg and a cross-sectional area of {:g} m^2.'
      .format(mission.spacecraft_mass, mission.spacecraft_area))

def P(a, b, mu, sigma):
    x = np.linspace(a, b, 50000)
    dx = np.sum(np.diff(x)) / (np.size(x) - 1)
    print(dx)
    f = 1 / (np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*((x-mu) / sigma)**2)
    int = np.sum(f)*dx
    return int

def P2(a, b, mu, sigma):
    x = np.linspace(a, b, 50000)
    f = 1 / (np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*((x-mu) / sigma)**2)
    int = 0
    for i in range(len(f)-1):
        dx = x[i+1] - x[i]
        int += (f[i+1] + f[i])*dx / 2
    return int


mu = 0
sigma = np.sqrt(sc.k*3e3/1.6735575e-27)
a = 5000
b = 300000
print(P(a, b, mu, sigma))
print(P2(a, b, mu, sigma))

# b)

class Particle:
    def __init__(self, m):
        self.mass = m

particle = Particle(2*1.6735575e-27)  # H2 particle
random.seed(1)

"""
Fra oppgavetekst
Tidsintervall: 1e-9
Antall tidssteg: 1000
dt = 1e-12
"""
class Box:
    def __init__(self, L, T, N, nz_side):
        self.Temp = T; self.N = N
        self.nozzle_side = nz_side
        self.p_pos = np.zeros((N, 1000, 3))
        self.p_vel = np.zeros((N, 1000, 3))
        self.L = L

    def set_initials(self):
        for i in range(self.N):
            for j in range(3):
                self.p_pos[i, 0, j] = random.uniform(-self.L/2, self.L/2)
                self.p_vel[i, 0, j] = random.gauss(0, np.sqrt(sc.k*self.Temp / particle.mass))
    @timer
    def simulate(self):
        v = self.p_vel; r = self.p_pos
        dt = 1e-12
        particels_out = 0
        for i in range(1000-1):
            v[:,i+1,:] = v[:,i,:]
            r[:,i+1,:] = r[:,i,:] + v[:,i+1,:]*dt
            for j in range(self.N):
                if abs(r[j, i+1, 0]) >= self.L/2:
                    v[j, i+1, 0] = -v[j, i+1, 0]
                if abs(r[j, i+1, 1]) >= self.L/2:
                    v[j, i+1, 1] = -v[j, i+1, 1]
                if r[j, i+1, 2] >= self.L/2:     # Tester z-koordinat for tak-kollisjon
                    v[j, i+1, 2] = -v[j, i+1, 2]
                # Tester z-koordinat for kollisjon med gulvet, evt. ut gjennom hullet
                if r[j, i+1, 2] <= -self.L/2:
                    if abs(r[j, i+1, 0]) < self.nozzle_side/2 and abs(r[j, i+1, 1]) < self.nozzle_side/2:
                        particels_out += 1
                        r[j, i+1, :] = [0, 0, self.L/2 - 1e-12]
                    else:
                        v[j, i+1, 2] = -v[j, i+1 , 2]
        print(particels_out)
        return v, r

engine = Box(L=1e-6, T=3e3, N=3, nz_side=0)  # Må kjøre på 100 000 !!!!!
engine.set_initials()
v, r = engine.simulate()
"""
"""
# Plotter initialpunkt og bane for partiklene bare for å se
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
for i in range(engine.N):
    ax.scatter(r[i,0,0], r[i,0,1], r[i,0,2])
    ax.plot(r[i,:,0], r[i,:,1], r[i,:,2], alpha=0.6)
plt.savefig('engine_box')
plt.show()
