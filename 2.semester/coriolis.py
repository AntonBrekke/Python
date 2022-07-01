import numpy as np
import matplotlib.pyplot as plt

R = 3
v0 = 6
omz = 12*2*np.pi/60     # rad/s
om = np.array([0,0,omz])
N = 1000
dt = 0.001
r = np.zeros([N,3])
v = np.zeros([N,3])
t = np.zeros([N,1])
r[0,:] = np.array([0,0,0])
v[0,:] = np.array([0,v0,0])
rr = 0
i = 0
while rr < R:
    ac = -2*np.cross(om, v[i,:])        # Coreolis-akselerasjon
    asf = -np.cross(om, np.cross(om, r[i,:]))   # Sentrifugalakselerasjon
    a = ac + asf
    v[i+1,:] = v[i,:] + dt*a
    r[i+1,:] = r[i,:] + dt*v[i+1,:]
    t[i+1] = t[i] + dt
    rr = np.linalg.norm(r[i+1,:])
    i += 1

print(f't = {t[i]}')
print(f'r = {r[i]}')
plt.plot(r[0:i, 0], r[0:i, 1])
theta = np.linspace(0, 2*np.pi, 101)
plt.plot(R*np.cos(theta), R*np.sin(theta))
plt.axis('equal')
plt.show()
