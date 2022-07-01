import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
b = 0.03
Q = np.sqrt(m*k/b**2)
print(f'Q = {Q}')

omega = np.sqrt(k/m)
gamma = b / (2*m)

F = 1
omegaF = np.linspace(0.1*omega, 2*omega, 1000)

phi = np.arctan2(2*gamma*omegaF, (omega**2 - omegaF**2))
A = (F/m) * 1 / np.sqrt((omega**2 - omegaF**2)**2 + (2*gamma*omegaF)**2)
# print(f'phi = {phi}')
# print(f'A = {A}')

fig, ax = plt.subplots(2,1)
ax[0].plot(omegaF/omega, A * m/F, color='r', linestyle='dashed')
ax[0].set_xlabel('omega'); ax[0].set_ylabel('A / (F/m)')
ax[1].plot(omegaF/omega, phi, color='b', linestyle='dashed')
ax[1].set_xlabel('omega/omegaF'); ax[1].set_ylabel('phi')
plt.show()
