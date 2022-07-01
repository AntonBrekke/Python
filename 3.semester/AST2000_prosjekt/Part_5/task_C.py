import numpy as np
import matplotlib.pyplot as plt
import ast2000tools.constants as const
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission
from ast2000tools.space_mission import InterplanetaryTravel
from ast2000tools.shortcuts import SpaceMissionShortcuts
from numba import njit
from scipy import interpolate

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)
mission = SpaceMission(seed)

r_all = np.load('positions_all_planets.npy')
time = np.load('time_planets.npy')

code_engine = 50557
code_launch = 25206
code_escape_trajectory = 14143

shortcut = SpaceMissionShortcuts(mission, [code_engine, code_launch, code_escape_trajectory])

number_density = 1e5 / (1e-6)**3
temperature = 5e3
hole_area = 0.25 * 1e-6**2

thrust_pr_box, mass_loss_pr_box = shortcut.compute_engine_performance(number_density, temperature, hole_area)

time_of_launch = 0
dt = time[1] - time[0]
launch_index = int(time_of_launch / dt)
print(launch_index)

G_sol = const.G_sol
planet_mass = system.masses[6]
M_star = system.star_mass
axis = system.semi_major_axes[6]
P = np.sqrt(4 * np.pi**2 * axis**3 / (G_sol * (M_star + planet_mass)))
AU = const.AU / 1000   # km
home_planet_R = system.radii[0] / AU # [AU]
print(home_planet_R)

N_box = 2e30
initial_fuel_mass = 1e20 # kg
est_launch_dur = 500 # s
thrust = thrust_pr_box * N_box
mass_loss_rate = mass_loss_pr_box * N_box
r_p_vec = r_all[:, 0, launch_index]
r_p_unit = r_p_vec / np.linalg.norm(r_p_vec)
radius_vec = home_planet_R * r_p_unit
r_0 = r_p_vec + radius_vec

mission.set_launch_parameters(thrust, mass_loss_rate, initial_fuel_mass, est_launch_dur, r_0, time_of_launch)
mission.launch_rocket()
shortcut.get_launch_results()

travel = mission.begin_interplanetary_travel()
