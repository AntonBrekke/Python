import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd
import scipy.constants as sc

from_eV_to_J = sc.elementary_charge     # Coloumb, V = J / C
lines_pr_dist = 30000
d = 1 / lines_pr_dist * 2.54e-2       # gitterkonstanten, ganger med 1 tomme = 2.54cm  fordi oppgaven oppga i tommer
print(f'd: {d:.3e} m\n')

Rb = 1.097e7         # Rydberg konstant, m^-1

def get_lmbda_n(n1, n2):
    return 1 / (Rb*(1/n1**2 - 1/n2**2))

def illuminans(x, R, a, N, A, lmbda):
    """
    E_N = E_1 * F_N er illuminansfunksjonen
    E_N prop. (sin(acx)/(acx))**2 * (sin(Nacx)/(sin(acx)))**2
    c = pi / (lambda * R)
    R: avstand fra spalte til der mønsteret plukkes opp
    a: spaltebredde
    lambda: bølgelengde på lyset
    sinc(x) = sin(pi*x) / (pi*x)
    """
    c = np.pi / (lmbda * R)
    arg = a*c*x / np.pi         # må dele bort pi i sinc-argument
    Arg = A*c*x
    E_1 = 1/N*(np.sinc(arg))**2
    F_N = 1/N*(np.sin(N*Arg) / np.sin(Arg))**2
    if N == 1: F_N = 1
    return E_1 * F_N


x = np.arange(-50, 50, 0.1) * 1e-3       # skal se på antall maksima innenfor +- 50 mm
lmbda = 632.8e-9        # m, He-Ne
R = 5       # m
a = 0.12e-3         # m
N = 1       # kun én spalte
A = 1              # Kun en spalte, så avstand mellom flere spalter er 0

# plt.plot(x, illuminans(x, R, a, N, A, lmbda))
# plt.show()

lines_pr_dist = 30000           # Lest av gitteret
d = 1 / lines_pr_dist * 2.54e-2       # gitterkonstanten, ganger med 1 tomme = 2.54cm  fordi gitteret oppga i tommer
m = 1
theta_v = np.array([27.0, 28.7, 30.6, 31.4, 38.8, 46.5]) * np.pi / 180
theta_h = np.array([323.3, 321.4, 319.5, 318.7, 310.8, 302.4]) * np.pi / 180
theta = (theta_h - theta_v) / 2

def find_lmbda(d, m, theta):
    lmbda = d / m * np.sin(theta)
    # print(lmbda)
    dtheta_h = 0.1      # grader
    dtheta_v = 0.1      # grader
    dtheta = 0.5 * np.sqrt((dtheta_h)**2 + (dtheta_v)**2) * np.pi/180       # rad
    dlambda = abs(lmbda * dtheta / np.tan(theta))            # Neglisjert feil i gitteret, dd

    for l, dl in zip(lmbda, dlambda):
        print(f'lambda: {l:.3e} +- {dl:.3e} m')
    print()

find_lmbda(d, m, theta)

theta_v = np.array([172.4, 168.2, 152.9]) * np.pi / 180
theta_h = np.array([234.0, 239.2, 254.5]) * np.pi / 180
theta = (theta_h - theta_v) / 2

find_lmbda(d, m, theta)

for j in range(5, 2, -1):
    lmbda_n = get_lmbda_n(2, j)
    print(f'lambda_n: {lmbda_n:.3e} m')
print()


# Zeeman-effekten
t = 3e-3        # m
c = sc.c
h = sc.h
B_indre_3A = 533e-3   #    T, 3A indre
B_ytre_3A = 520e-3    #    T, 3A ytre
B_indre_4A = 694e-3    #    T, 4A indre
B_ytre_4A = 677e-3    #    T, 4A ytre

def find_dnu(delta):
    return c / (2*t) * delta

def find_muB(dnu, B):
    return h*dnu / (2*B)

# 3A, 90 grader
ring_1 = np.array([[401, 398], [423, 420]])       # indre1, indre2, ytre1, ytre2
ring_2 = np.array([[481, 478], [501, 497]])       # indre1, indre2, ytre1, ytre2
ring_3 = np.array([[636, 632], [654, 648]])       # indre1, indre2, ytre1, ytre2

ring_1 = np.sum(ring_1, axis=1) / 2               # snitt indre, snitt ytre
ring_2 = np.sum(ring_2, axis=1) / 2               # snitt indre, snitt ytre
ring_3 = np.sum(ring_3, axis=1) / 2               # snitt indre, snitt ytre

d1_i, d1_y = ring_1
d2_i, d2_y = ring_2
d3_i, d3_y = ring_3

delta_i = (d2_i**2 - d1_i**2) / (d3_i**2 - d1_i**2)
delta_y = (d2_y**2 - d1_y**2) / (d3_y**2 - d1_y**2)
print(f'3A: delta_i: {delta_i}, delta_y: {delta_y}\n')

dnu_i = find_dnu(delta_i)
dnu_y = find_dnu(delta_y)
print(f'dnu_i: {dnu_i:.4e}, dnu_y: {dnu_y:.4e}')

muB_i = find_muB(dnu_i, B_indre_3A)
muB_y = find_muB(dnu_y, B_ytre_3A)
muB_snitt_3A = 0.5 * (muB_i + muB_y)
print(f'muB_i: {muB_i:.4e}, muB_y: {muB_y:.4e}\n')

# 4A, 90 grader
ring_1 = np.array([[384, 386], [409, 412]])       # indre1, indre2, ytre1, ytre2
ring_2 = np.array([[490, 488], [511, 509]])       # indre1, indre2, ytre1, ytre2
ring_3 = np.array([[627, 623], [647, 643]])       # indre1, indre2, ytre1, ytre2

ring_1 = np.sum(ring_1, axis=1) / 2               # snitt indre, snitt ytre
ring_2 = np.sum(ring_2, axis=1) / 2               # snitt indre, snitt ytre
ring_3 = np.sum(ring_3, axis=1) / 2               # snitt indre, snitt ytre

d1_i, d1_y = ring_1
d2_i, d2_y = ring_2
d3_i, d3_y = ring_3

delta_i = (d2_i**2 - d1_i**2) / (d3_i**2 - d1_i**2)
delta_y = (d2_y**2 - d1_y**2) / (d3_y**2 - d1_y**2)
print(f'4A: delta_i: {delta_i}, delta_y: {delta_y}\n')

dnu_i = find_dnu(delta_i)
dnu_y = find_dnu(delta_y)
print(f'dnu_i: {dnu_i:.4e}, dnu_y: {dnu_y:.4e}')

muB_i = find_muB(dnu_i, B_indre_4A)
muB_y = find_muB(dnu_y, B_ytre_4A)
muB_snitt_4A = 0.5 * (muB_i + muB_y)
print(f'muB_i: {muB_i:.4e}, muB_y: {muB_y:.4e}\n')

muB_snitt_snitt = 0.5 * (muB_snitt_3A + muB_snitt_4A)
print(f'muB_snitt_3A: {muB_snitt_3A:.4e}, muB_snitt_4A: {muB_snitt_4A:.4e}\n<mu_snitt>: {muB_snitt_snitt:.4e}')
mu_B_theory = 9.274009994e-24       # J/T
relative_error = abs(mu_B_theory - muB_snitt_snitt) / mu_B_theory
print(f'relative error: {relative_error*100} %')
