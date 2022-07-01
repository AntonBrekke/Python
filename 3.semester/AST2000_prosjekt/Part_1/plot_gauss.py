import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

k = sc.k
H2_m = 2*1.6735575e-27
T = 3e3
mu = 0
sigma = np.sqrt(k*T/H2_m)
def Pvx(vx, m, mu, sigma):
    return 1 / (np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*((vx-mu) / sigma)**2)

def Pv(v, m):
    return (m/(2*np.pi*k*T))**(3/2) * np.exp(-0.5*m*v**2 / (2*k*T)) * 4*np.pi*v**2

v = np.linspace(0, 10000, 10000)
P_v = Pv(v, H2_m)

vx = np.linspace(-10000, 10000, 10000)
P_vx = Pvx(vx, H2_m, mu, sigma)

plt.plot(vx, P_vx, linewidth=4, color='r', label='Gaussian')
# plt.plot(v, P_v)
plt.xlabel(r'$v_x$', fontweight='bold', fontsize=16)
plt.title(r'$P_{vx}$', fontweight='bold', fontsize=20)
plt.legend()
plt.savefig('Gauss_vx')
plt.show()

x = np.random.normal(mu, sigma, 1000)
count, bins, ignore = plt.hist(x, 50, density=True, label='Histogram of Gaussian')
plt.plot(bins, Pvx(bins, H2_m, mu, sigma), linewidth=4, color='r', label='Gaussian')
plt.xlabel(r'$v_x$', fontweight='bold', fontsize=16)
plt.title(r'$P_{vx}$', fontweight='bold', fontsize=20)
plt.legend()
# plt.savefig('Gaussian_histogram')
plt.show()

def animate_bins():
    x = np.random.normal(mu, sigma, 1000)
    for i in range(10, 501, 10):
        plt.hist(x, i)
        plt.draw()
        plt.pause(0.1)
        plt.clf()
# animate_bins()
