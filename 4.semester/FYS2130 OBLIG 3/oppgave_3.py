import numpy as np
import matplotlib.pyplot as plt

# Verdier gitt i oppgave
R = 1
C = 100e-9
L = 25e-6

# Konstanter funnet i diff.likning
gamma = R / (2*L)
omega_0 = np.sqrt(1 / (C*L))
omega_F = np.sqrt(omega_0**2 - R**2 / (2*L**2))

# Finner Q-faktor
Q = np.sqrt(L / (C*R**2))
print(f'Q = {Q}')
# omega_0 = omega_F
omega_F = omega_0 + omega_0 / (2*Q)
phi_QV = np.arctan2(2*gamma*omega_F, (omega_0**2 - omega_F**2)) # Bruker arctan2 for riktig kvadrant
phi_IV = phi_QV - np.pi/2
print(f'phi_IV = {phi_IV}')
