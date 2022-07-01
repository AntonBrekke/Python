import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
from scipy import stats

h = 4.135667696e-15         # eV/s
c = sc.c        # m/s
m_e = 511 / c**2        # keV / c^2
d_LiF = 401 / 2 * 1e-12     # m
d_KCF = 401 / 2 * 1e-12     # m
e = 1           # e
# print(h*c / (2*d))

step = 0.5
_2theta = np.arange(12, 22 + step, step)
print(f'2theta: {_2theta}\n')

n = np.array([92, 108, 136, 103, 140, 136, 162, 240, 272, 332, 444, 536, 578,
              664, 754, 814, 861, 894, 926, 946, 954])      # Intensitetsmål

plt.plot(_2theta, n, marker='x', linewidth=3, label='Data')

bk_rad = np.where(_2theta <= 15.5)
bk_line = stats.linregress(_2theta[bk_rad], n[bk_rad])
bk_linefit = np.poly1d(bk_line[:2])
bk_plotline = bk_linefit(_2theta)
plt.plot(_2theta, bk_plotline, linewidth=3, label='Regression background')

bragg = np.logical_and(_2theta >= 15.5, _2theta <= 20)
bragg_line = stats.linregress(_2theta[bragg], n[bragg])
bragg_linefit = np.poly1d(bragg_line[:2])
bragg_plotline = bragg_linefit(_2theta)
plt.plot(_2theta, bragg_plotline, linewidth=3, label='Regression of steep descent')

print(bk_line)
print()
print(bragg_line)
A = bragg_line.slope
B = bragg_line.intercept
C = bk_line.slope
D = bk_line.intercept
dA = bragg_line.stderr
dB = bragg_line.intercept_stderr
dC = bk_line.stderr
dD = bk_line.intercept_stderr

plt.xlabel(r'2$\theta\;[^o]$', fontsize=20, weight='bold')
plt.ylabel(r'n [tellinger på t=60s]', fontsize=20, weight='bold')

_2theta_min = (D - B) / (A - C)       # lest av
print(_2theta_min, 'her')
theta_min = _2theta_min / 2 * np.pi / 180         # rad

plt.scatter(_2theta_min, n[np.where(_2theta == 15)], marker='|', s=30**2, linewidth=3, color='r', zorder=2)
plt.text(_2theta_min + 0.1, 110, r'$2\theta_{min}$', color='r', fontsize=14)

plt.legend(prop={'size': 20})
plt.show()

def find_lambda_from_angle(angle, d, n=1):
    return 2*d * np.sin(angle) / n

def find_U_from_lambda(lmbda):
    return h*c / (lmbda*e)

def find_U_from_theta(angle, d, n=1):
    return h*c*n / (2*d*np.sin(angle))

lmbda = find_lambda_from_angle(theta_min, d_LiF)
U = find_U_from_lambda(lmbda)
U2 = find_U_from_theta(theta_min, d_LiF)
print(f'lambda: {lmbda}')
dDB = np.sqrt(dB**2 + dD**2)
dAC = np.sqrt(dA**2 + dC**2)
DB = D - B
AC = A - C
dtheta_min_stat = DB / AC * np.sqrt((dDB / DB)**2 + (dAC / AC)**2) / 2 * np.pi / 180
dtheta_min_syst = 0.5 / 2 * np.pi / 180       # rad
dtheta_min = np.sqrt((dtheta_min_syst)**2 + (dtheta_min_stat)**2)
print(dtheta_min_stat * 180 / np.pi, dtheta_min_syst * 180 / np.pi, dtheta_min * 180 / np.pi)
# print('hola', theta_min, dtheta_stat, dtheta_syst, dtheta)
dU = h*c / (2*d_LiF) * dtheta_min * np.cos(theta_min) / np.sin(theta_min)**2
print(f'U: {U, U2} +- {dU} V\n\n')

# B
# n = 1
_2theta_1 = np.arange(22, 31.5 + step, step)
I1 = np.array([260 ,229 ,713, 802, 1051, 1271, 1888, 2029, 1552, 2033, 2635,
               3572, 4414, 3898, 2023, 305, 219, 171, 145, 129])
# n = 2
_2theta_2 = np.arange(48.5, 61.5 + step, step)
I2 = np.array([72 ,91 ,86 ,112, 153, 192, 209, 227, 218, 164, 122, 108, 110, 88, 94, 114,
               195, 498, 595, 647, 619, 528, 270, 94, 90, 74, 81])

plt.plot(_2theta_1, I1, label='n=1', linewidth=2)
plt.plot(_2theta_2, I2, label='n=2', linewidth=2)
plt.xlabel(r'2$\theta\;[^o]$', fontsize=20, weight='bold')
plt.ylabel(r'n [tellinger på t=60s]', fontsize=20, weight='bold')
plt.legend(prop={'size': 20})
plt.show()

lmbdas = np.array([154.2, 138.6, 154.2, 138.6])
_2theta_topper = np.array([28, 25.5, 58, 52]) * np.pi/180
n = np.array([1,1,2,2])
_2d = np.array([637.4, 628, 636.1, 632.3])
def find_2d_from_theta(_theta_, _lmbda_, n):
    return n*_lmbda_ / np.sin(_theta_)
def find_theta_from_2d(_2d, _lmbda, n):
    return 2*np.arcsin(n*_lmbda / _2d)

print(f'2theta: {find_theta_from_2d(_2d, lmbdas, n) * 180 / np.pi}')
print(f'2d: {find_2d_from_theta(_2theta_topper/2, lmbdas, n)}')
print(f'd2d: {_2d / np.tan(_2theta_topper/2) * 0.5 * np.pi / 180}')
# C
U_step = 0.2
U_nom = np.arange(3, 5 + U_step, U_step)        # kV
I = np.array([27, 29, 30, 32, 34, 36, 38, 39, 41, 43, 45]) * 1e-3 * 1e-3        # A

indre_innerst = np.array([270, 268, 265, 254, 231, 245, 235, 230, 229, 216, 207]) * 1e-2 * 1e-2     # m
indre_ytterst = np.array([345, 320, 335, 315, 305, 294, 301, 294, 281, 275, 264]) * 1e-2 * 1e-2     # m

ytre_innerst = np.array([496, 484, 480, 456, 431, 435, 421, 426, 411, 400, 386]) * 1e-2 *1e-2       # m
ytre_ytterst = np.array([583, 551, 550, 541, 539, 507, 503, 496, 478, 470, 463]) * 1e-2 * 1e-2      # m

R = 10e6        # omega
U = U_nom - R*I*1e-3        # kV, må gjøre R*I fra V til kV -> *1e-3
print(f'U: {U} kV')

def f(U, e=1):
    # U må være i kV
    return 1 / (np.sqrt(1 + e*U / (2*m_e*c**2)))        # m_e * c**2 : keV.

lambda_c = h*1e-3 / (m_e*c)     # Må gjøre h fra eVs til keVs -> *1e-3. keVs  / keV / c = s * m/s = m
def find_lambda_from_U(U):
    return lambda_c * np.sqrt(m_e*c**2 / (2*e*U)) * f(U)        # m

lambda_i = find_lambda_from_U(U)
print(f'lambda_i: {lambda_i} nm\n\n')

D_indre = (indre_innerst + indre_ytterst) / 2
D_ytre = (ytre_innerst + ytre_ytterst) / 2
print(f'D_indre: {D_indre}, D_ytre: {D_ytre}\n')
print(f'lambda_i / D_indre: {lambda_i / D_indre}, lambda_i / D_ytre: {lambda_i / D_ytre}')

N = len(D_ytre)

phi_d10_mean = 1 / N * np.sum(lambda_i / D_indre)        # phi er snittet av forholdet lambda_i / Dytre_i
phi_std_d10 = np.sqrt(1 / N * np.sum((lambda_i / D_indre - phi_d10_mean)**2))       # std
phi_std_m_d10 = phi_std_d10 / np.sqrt(N)            # samme som dphi

phi_d11_mean = 1 / N * np.sum(lambda_i / D_ytre)        # phi er snittet av forholdet lambda_i / Dytre_i
phi_std_d11 = np.sqrt(1 / N * np.sum((lambda_i / D_ytre - phi_d11_mean)**2))       # std
phi_std_m_d11 = phi_std_d11 / np.sqrt(N)            # samme som dphi

print(f'{phi_d10_mean} + {phi_std_m_d10}\n\n')
print(f'{phi_d11_mean} + {phi_std_m_d11}\n\n')

"""
Forventer d10 ca. 213pm
Forventer d11 ca. 123pm
"""

L = 125e-3
dL = 2e-3
d10 = 2*lambda_i*L / D_indre
d11 = 2*lambda_i*L / D_ytre
dD_indre = 1e-3 / np.sqrt(2)         # må defineres
dD_ytre = 1e-3 / np.sqrt(2)     # må defineres
dd10_LD = d10 * np.sqrt((dL / L)**2 + (dD_indre / D_indre)**2)
dd11_LD = d11 * np.sqrt((dL / L)**2 + (dD_ytre / D_ytre)**2)

dd10_std = np.std(d10)
dd11_std = np.std(d11)

dd10 = np.sqrt(dd10_std**2 + dd10_LD**2)
dd11 = np.sqrt(dd11_std**2 + dd11_LD**2)


print(f'd10 / d11: {d10 / d11}')
print(f'd10: {d10}\n\n d11: {d11}\n\n')
print(f'dd10: {dd10}\n\n dd11: {dd11}\n\n')
print(f'sqrt(3):{np.sqrt(3)}\n\n')

d10_mean = 2*L*phi_d10_mean
d11_mean = 2*L*phi_d11_mean

dd10_mean = 2*L*phi_d10_mean * np.sqrt((dL / L)**2 + (phi_std_m_d10 / phi_d10_mean)**2)
dd11_mean = 2*L*phi_d11_mean * np.sqrt((dL / L)**2 + (phi_std_m_d11 / phi_d11_mean)**2)

print(f'd10_mean: {d10_mean} +- {dd10_mean}')
print(f'd11_mean: {d11_mean} +- {dd11_mean}')
last_error = d10_mean / d11_mean * np.sqrt((dd10_mean / d10_mean)**2 + (dd11_mean / d11_mean)**2)
print(f'd10_m / d11_m: {d10_mean / d11_mean} +- {last_error}')
