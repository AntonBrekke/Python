# Python-script
# Group exercise G2 week 12, 20-24 April 2020
# Group exercise G1 week 12, 21-23 April 2021 & 25-29 April, 2022
# Coriolis and sentrifugal acceleration in a spinning merry-go-round
# We make a coordinate system where the y' axis points towards person B
# Person A is first standing in origo (in the center of the disc)
# and is throwing a ball towards person B (subtask c).
# In subtask d, person A stands at the edge of the merry-go-round.
# Cecilie, April 22, 2020
# Last update: April 19, 2022
# a.c.larsen@fys.uio

# Import Python libraries
import numpy as np
import matplotlib.pyplot as plt

# Define constants.
R  = 3. # radius of the circle in m
x0  =  0. # start position x0 in m
#y0  =  0. # start position y0 in m:  it is either 0 m (subtask c) or -3. m (subtask d)
y0  =  0. # start position y0 in m:  it is either 0 m (subtask c) or -3. m (subtask d)
omega_z = 12.*2.*np.pi/60. # the z' component of the angular velocity. This is the same as the z component in this case
omega = np.array([0., 0., omega_z]) # the angular velocity vector
#v0x = 0.0 #  initial speed in the x direction, m/s (subtask c)
v0x = 0 #  initial speed in the x direction, m/s (subtask d), v0x = omega*R
v0y = 6.0 #  initial speed in the y direction, m/s
n    = 1000 # number of steps
dt   = 0.001 # time step

# Define the arrays we need for the position vector r', velocity v'
# and the time array t.
# The "prime" notation indicates that we are in an accelerated coordinate system
# and not in an inertial system
# For v and v', the intial conditions are different because of the
# the rotation of system S'. See equation (17.26) in ch.17 in the compendium:
# v = V + v' + omega x r'
# As there is no linear velocity V of system S' relative to S, V is zero
# and we get:
# v = v' + omega x r'
# => v' = v - omega x r'
# This must be taken into account for the initial velocity v0'
# In the first case, the start position is in origo, the term
# omega x r0' = 0 as a consequence, and v0' = v0. However, if r0' is different,
# we must take the term omega x r0' into account.
# The simplest way is to always include it.

r = np.zeros((n, 3), float)
r_prime = np.zeros((n, 3), float)
v_prime = np.zeros((n, 3), float)
t = np.zeros((n, 1), float)

# Initial condition for r, r'
r[0, :] = np.array([x0, y0, 0.])
# Subtask c: The ball starts in origo, before person A is throwing it
# For subtask d, the initial position of person A has changed:
# The ball starts now  at x0' = 0 m, y0' = -3.m, before person A is throwing it
r_prime[0, :] = r[0, :]

# Initial condition for the length of the r_prime vector
r_norm = np.linalg.norm(r[0, :])
r_prime_norm = np.linalg.norm(r_prime[0, :])

# Initial condition for v'
vr = np.cross(omega, r[0, :]) # this is the term omega x r' (see above)
v_prime[0, :] = np.array([v0x, v0y, 0.]) -vr

for i in range(n-1):
	if (r_prime_norm>R): break # We only want to calculate until the ball reaches the edge of the merry-go-round
	a_coriolis    = -2.*np.cross(omega, v_prime[i, :])	# Coriolis acceleration
	a_centrifugal = np.cross(omega, np.cross(r_prime[i, :], omega)) # centrifugal acceleration
	a_prime       = a_coriolis + a_centrifugal	# total acceleration
	# here we use the good, old Euler-Cromer method to calculate the next steps
	v_prime[i+1, :] = v_prime[i, :] + a_prime*dt
	r_prime[i+1, :] = r_prime[i, :] + v_prime[i+1, :]*dt
	r_prime_norm = np.linalg.norm(r_prime[i+1, :])
	t[i+1] = t[i] + dt

# Now we are done with the loop, and we want to check several things:
# 1. the time it takes for the ball to reach the edge of the circle
# 2. the position (x',y') when the ball reaches the edge
print(" Time when the ball reaches the edge (in seconds): ",t[i])
print(" Position vector (x',y'): ",r_prime[i, :])

# Let us make a circle to represent the merry-go-round:
# the angle phi:
phi = np.linspace(0., 2.*np.pi,360) # circle from 0 to 2*pi, in steps of 1 degree

# Also, make a nice plot of the position vector r_prime
# See https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
fig, ax = plt.subplots(nrows=1, figsize=(7, 6))
ax.axis('equal') # To ensure the same range on the x and y axis
ax.plot(r_prime[1: i,0], r_prime[1:i, 1]) # (x',y')
ax.set_xlabel("$x'$ (m)")
ax.set_ylabel("$y'$ (m)")
fig.tight_layout()
ax.plot(R*np.sin(phi), R*np.cos(phi))

# Make a little circle where person B is
ax.plot(0.029*R*np.sin(phi), R+0.1*np.cos(phi))

plt.show()
#Woohoo! :)
