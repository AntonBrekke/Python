import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

# Definerer konstanter
a = 0.614       # nm
eV_to_Joule = sc.value('electron volt')
Joule_to_eV = 1 / eV_to_Joule
hbar = sc.hbar * Joule_to_eV        # eV*s
print(hbar)

# Definerer psi(x) for energinivå n
def psi(x, n):
    if n % 2 == 0:
        return 1/np.sqrt(a) * np.sin(n*np.pi / (2*a) * x)       # Hvis partall - sinus 2, 4, 6, ...
    else:
        return 1/np.sqrt(a) * np.cos(n*np.pi / (2*a) * x)       # Hvis ikke partall (oddetall) - cosinus 1, 3, 5, ...

"""
(1240 nm eV)
0.511MeV
pi**2 * (1240nm eV)**2 / (8*0.614**2 nm**2 * 10**6 eV)
"""
# Regner ut energinivåer
def E(n):
    return 1240**2 / (32*a**2*0.511e6) * n**2       # eV

for n in range(1, 5):
    print(f'E{n}: {E(n)} eV')

# Samler alle koeffisienter i en array
c1 = np.sqrt(4/10)
c2 = np.sqrt(3/10)
c3 = np.sqrt(2/10)
c4 = np.sqrt(1/10)
c_array = np.array([c1, c2, c3, c4])

# Tidsanvhengig del av Psi
def phi(t, n):
    return np.exp(-1j * E(n) / hbar * t)

# Funksjon av Psi som superposisjon av psi*phi
def Psi(x, t, c_array):
    sum = 0
    for n in range(len(c_array)):
        sum += c_array[n]*psi(x, n+1)*phi(t, n+1)
    return sum


# Plotter sannsynlighetstettheter
fig = plt.figure()

t = 5e-15       # s
x = np.linspace(-a, a, 800)     # nm
dx = x[1] - x[0]
print(f'Normalisation: {np.sum(abs(Psi(x, t, c_array))**2)*dx}')

plt.plot(x, abs(Psi(x, t, c_array))**2, color='royalblue', label=r'$|\Psi(x,t)|^2$ [1/nm]')
plt.xlabel('x [nm]', weight='bold', fontsize=14)
plt.ylabel(r'$|\Psi|^2$ [1/nm]', weight='bold', fontsize=14)

Psi2 = psi(x, 2) * phi(t, 2)
plt.plot(x, abs(Psi2)**2, color='r', label=r'$|\Psi_2(x,t)|^2$ [1/nm]')

plt.legend(prop={'size': 14})
plt.savefig('wavefunc.pdf')
plt.show()

# Regner ut forventningsverdier og spredning
n_array = np.array([1,2,3,4])
E_array = E(n_array)
mid_H = np.sum(c_array**2 * E_array)
mid_HS = np.sum((c_array * E_array)**2)
sigma_H = np.sqrt(mid_HS - mid_H**2)
E2 = E(2)
mid_H_2 = E2
mid_HS_2 = E2**2
sigma_H_2 = np.sqrt(mid_HS_2 - mid_HS**2)
mid_p_2 = 0
mid_pS_2 = np.pi**2 * hbar**2 / (a*1e-9)**2         # Må gjøre om enhet a til m for å gå opp med eV.
# mid_pS_2 = 1240**2 / (4*(3e8*a)**2)         # (eVnm)^2 / (m/s nm)^2 = (kg^2m^4/s^4nm^2) / (m^2/s^2 nm^2) = kg^2m^2/s^2 : eV^2 / c^2
sigma_p_2 = np.sqrt(mid_pS_2 - mid_p_2)
print(f'mid_H: {mid_H} eV')
print(f'mid_HS: {mid_HS} eV')
print(f'sigma_H: {sigma_H} eV')
print(f'mid_H_2: {mid_H_2} eV')
print(f'mid_HS_2: {mid_HS_2} eV')
print(f'sigma_H_2: {sigma_H_2} eV')
print(f'mid_p_2: {mid_p_2} eV / c')
print(f'mid_pS_2: {mid_pS_2} eV / c')
print(f'sigma_p_2: {sigma_p_2} eV / c')


"""
Kjøretest fra terminal:
C:>python midtveis.py

6.582119569509067e-16
E1: 0.24942256988031392 eV
E2: 0.9976902795212557 eV
E3: 2.2448031289228254 eV
E4: 3.9907611180850227 eV
oppgave_1.py:72: RuntimeWarning: invalid value encountered in sqrt
  sigma_H_2 = np.sqrt(mid_HS_2 - mid_HS**2)
mid_H: 1.2471128494015695 eV
mid_HS: 2.9239460631879037 eV
sigma_H: 1.1698955526222852 eV
mid_H_2: 0.9976902795212557 eV
mid_HS_2: 0.9953858938512012 eV
sigma_H_2: nan eV
mid_p_2: 0 eV / c
mid_pS_2: 1.13421278338361e-11 eV / c
sigma_p_2: 3.3678075707849017e-06 eV / c
"""
