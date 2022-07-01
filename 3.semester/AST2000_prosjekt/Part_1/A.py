import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

# 1.1)
def P(a, b, mu, sigma):
    x = np.linspace(a, b, 100000)
    dx = np.sum(np.diff(x)) / (np.size(x) - 1)
    f = 1 / (np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*((x-mu) / sigma)**2)
    int = np.sum(f)*dx
    return int

def P2(a, b, mu, sigma):
    x = np.linspace(a, b, 100000)
    f = 1 / (np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*((x-mu) / sigma)**2)
    int = 0
    for i in range(len(f)-1):
        dx = x[i+1] - x[i]
        int += (f[i+1] + f[i])*dx / 2
    return int

# 1.3)
mu = 0
H2_mass = 2*1.6735575e-27
sigma = np.sqrt(sc.k*3e3/H2_mass)
a = mu - sigma
b = mu + sigma
print(P(a, b, mu, sigma))
print(P2(a, b, mu, sigma))

# 2.1)
vx = np.linspace(-2.5e4, 2.5e4, 10000)
def Pvx(vx):
    m = H2_mass     # H2 gas
    T = 3e3
    return np.sqrt(m / (2*np.pi*sc.k*T)) * np.exp(-0.5*m*vx**2 / (sc.k*T))

plt.plot(vx, Pvx(vx))
plt.show()

# 2.2)
mu = 0
sigma = np.sqrt(sc.k*3e3/H2_mass)
a = 5000
b = 30000
N = 100000
print(P(a, b, mu, sigma))
print(P2(a, b, mu, sigma))
print(P(a, b, mu, sigma)*N)
print(P2(a, b, mu, sigma)*N)

# 2.3
v = np.linspace(0, 3e4, 1000)
def Pv(v):
    m = H2_mass
    T = 3e3
    return (m / (2*np.pi*sc.k*T))**(3/2) * np.exp(-0.5*m*v**2 / (sc.k*T)) * 4*np.pi*v**2

plt.plot(v, Pv(v))
plt.show()
