import numpy as np
import matplotlib.pyplot as plt

"""
Velger m, omega, hbar s.a
m*omega / hbar = 1nm^-2 = 1 / (nm)^2 = 1e-18 1/m
"""

m = 1
omega = 1
hbar = 1

print(m * omega / hbar)

def psi0(x):
    return 5*np.exp(-m*omega/(2*hbar) * x**2)

x = np.linspace(-5, 5, 600)

Vx = 0.5 * m * omega**2 * x**2
psi_0 = psi0(x)
psi_1 = (2*m*omega/hbar)**1/2 * x*psi_0
psi_2 = np.sqrt(2) / hbar * (m*omega*x**2 - hbar/2) * psi_0

fig, (ax1, ax2, ax3) = plt.subplots(3,1)

ax1.plot(x, abs(psi_0)**2, label=r'$|\Psi_0|^2$')
ax2.plot(x, abs(psi_1)**2, label=r'$|\Psi_1|^2$')
ax3.plot(x, abs(psi_2)**2, label=r'$|\Psi_2|^2$')

ax1.plot(x, Vx, label='V(x)')
ax2.plot(x, Vx, label='V(x)')
ax3.plot(x, Vx, label='V(x)')

ax1.set_xlabel('x [m]', weight='bold', fontsize=12)
ax2.set_xlabel('x [m]', weight='bold', fontsize=12)
ax3.set_xlabel('x [m]', weight='bold', fontsize=12)

ax1.set_ylabel(r'$|\Psi_0\|^2;[m^{-1/2}]$', weight='bold', fontsize=12)
ax2.set_ylabel(r'$|\Psi_1\|^2;[m^{-1/2}]$', weight='bold', fontsize=12)
ax3.set_ylabel(r'$|\Psi_2\|^2;[m^{-1/2}]$', weight='bold', fontsize=12)

fig.tight_layout()
ax1.legend()
ax2.legend()
ax3.legend()
plt.show()
