import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd
import scipy.constants as sc

from_eV_to_J = sc.elementary_charge     # Coloumb, V = J / C
lines_pr_dist = 30000
d = 1 / lines_pr_dist * 2.54e-2       # gitterkonstanten, ganger med 1 tomme = 2.54cm  fordi oppgaven oppga i tommer
print(f'd: {d:.3e}')

R = 1.097e7         # Rydberg konstant, m^-1

def get_lmbda_n(ni, nf):
    # ni: initial state, nf: final state
    return 1 / (R*(1/nf**2 - 1/ni**2))

for j in range(3, 15):
    lmbda_n = get_lmbda_n(2, j)
    # print(f'lambda_n: {lmbda_n:.3e}')

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

plt.plot(x, illuminans(x, R, a, N, A, lmbda))
plt.show()
