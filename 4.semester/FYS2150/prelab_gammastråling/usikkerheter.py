import numpy as np

E2 = 1333       # keV
E1 = 662

I2 = 659
I1 = 335
I = 581

dI2 = 1
dI1 = 1
dI = dI2

DE = (E2 - E1) / (I2 - I1)
E0 = E2 - I2 * DE
print(DE, E0)

dDE = DE / (I2 - I1) * np.sqrt(dI1**2 + dI2**2)
dE0_1 = np.sqrt((I1 * dDE)**2 + (DE * dI1)**2)
dE0_2 = np.sqrt((I2 * dDE)**2 + (DE * dI2)**2)
print(dDE, dE0_1, dE0_2)
# Bruker dE0_1

E = DE * I + E0
dE_1 = np.sqrt((I * dDE)**2 + (DE * dI)**2 + (dE0_1)**2)
dE_2 = np.sqrt((I * dDE)**2 + (DE * dI)**2 + (dE0_2)**2)
print(E, dE_1, dE_2)

dE0 = dE0_1
def find_dE(I, DE, E0, ddE, dE0):
    print(f'E: {DE * I}')
    print(f'dE: {np.sqrt((I * dDE)**2 + (DE * dI)**2 + (dE0)**2)}\n')

I_list = [90, 119, 146, 172, 300]
for I in I_list:
    find_dE(I, DE, E0, dDE, dE0)


r = 1.4
d = 16
dd = 0.1
A = 149e3
n = 107 / 60
dn = 3 / 60
omega = np.pi * r**2 / d**2
domega = 2*omega / d * dd
print(omega, domega)
eff = 4*np.pi * n / (A*omega)
deff = np.sqrt((4*np.pi*n / (A*omega) * domega)**2 + (4*np.pi / (A*omega) * dn)**2)
print(eff*100, deff*100)
