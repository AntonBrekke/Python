from PIL import Image
import numpy as np
import ast2000tools.constants as const
import ast2000tools.utils as utils
from ast2000tools.solar_system import SolarSystem
from ast2000tools.space_mission import SpaceMission
import random
import matplotlib.pyplot as plt
import time
from numba import njit

"""
Egen kode !!!
"""

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)
mission = SpaceMission(seed)

img = Image.open('sample0000.png') # Åpner sample-bildet
pixels = np.array(img) # png til numpy-array
# print(pixels.dtype)   #uint8
shape = np.shape(img)   # Shape av sample-bildet
# print(shape)
from_grad_to_rad = np.pi / 180      # Til konvertering mellom grader og radianer

at = 70 * from_grad_to_rad      # FOV a_theta
ap = 70 * from_grad_to_rad      # FOV a_phi
phi0 = 0                        # samme i grader og radianer
theta0 = 90 * from_grad_to_rad
# Max/min verdier for xy-grid
Xmax = 2*np.sin(ap/2) / (1 + np.cos(ap/2))
Ymax = 2*np.sin(at/2) / (1 + np.cos(at/2))
Xmin = -Xmax
Ymin = -Ymax
# Lager et meshgrid
I = np.linspace(Xmin, Xmax, 640)
J = np.linspace(Ymin, Ymax, 480)
X, Y = np.meshgrid(I, J, indexing='xy')
rho = np.sqrt(X**2 + Y**2)
beta = 2*np.arctan(rho/2)

himmelkule = np.load('himmelkule.npy')

theta = theta0 - np.arcsin(np.cos(beta)*np.cos(theta0) + Y/rho*np.sin(beta)*np.sin(theta0)) # Polar angle
phi = phi0 + np.arctan(X*np.sin(beta) / (rho*np.sin(theta0)*np.cos(beta) - Y*np.cos(theta0)*np.sin(beta)))  # Azimuth-angle

# kappa = 2 / (1 + np.cos(theta0)*np.cos(theta) + np.sin(theta0)*np.sin(theta)*np.sin(phi - phi0))

pixel_array = np.zeros(shape, dtype=np.uint8)
for i in range(len(theta[:,0])):
    for j in range(len(theta[0,:])):
        pixel_index = mission.get_sky_image_pixel(theta[i,j], phi[i,j])
        pixel_array[i,j,:] = himmelkule[pixel_index,2:]

print(pixel_array.dtype)
img2 = Image.fromarray(pixel_array[::-1, :, :])
img2.save('itry.png')
