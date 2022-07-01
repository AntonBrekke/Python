import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd
import scipy.constants as sc

h = 4.135667696e-15         # eV/s
c = sc.c        # m/s
Emax = 20e3     # kV / ekV for 1 elektron
e = 1
d = 200.5e-12           # m

lambda_min = h*c / (Emax * e)
print(lambda_min)
nu = np.arange(12, 26, 1)
I = np.array([130, 124, 133, 131, 128, 132, 138, 192, 244, 301, 348, 403, 462, 508])
plt.plot(nu, I)
plt.show()


m_e = 511 / c**2       # keV/c^2
def f(U, e=1):
    # U must be in kV
    return 1 / (np.sqrt(1 + e*U / (2*m_e*c**2)))

print(f(U=8))


diam_dat = np.loadtxt('diameter.dat')
U = diam_dat[:,0] * 1e-3        # kV
Dytre_i = diam_dat[:,1]

lambda_c = h*1e-3 / (m_e*c)         # må gjøre h fra eVs til keVs -> *1e-3
print(lambda_c)

def find_lambda_i(U):
    return lambda_c * np.sqrt(m_e*c**2 / (2*e*U)) * f(U)

def lambda_from_angle(angle, n=1):
    return 2*d * np.sin(angle) / n

print(lambda_from_angle(18 * np.pi / 180))

def find_U(lmbda, e=1):
    return h*c / (lmbda * e)

print(find_U(lambda_from_angle(18 * np.pi / 180)))

N = len(Dytre_i)
lambda_i = find_lambda_i(U)

phi = 1 / N * np.sum(lambda_i / Dytre_i)        # phi er snittet av forholdet lambda_i / Dytre_i
std = np.sqrt(1 / N * np.sum((lambda_i / Dytre_i - phi)**2))       # std
std_m = std / np.sqrt(N)            # samme som dphi

print(phi, f'+', std_m)
