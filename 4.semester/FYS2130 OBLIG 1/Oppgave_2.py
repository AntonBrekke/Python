import numpy as np
import matplotlib.pyplot as plt


# d) Plotter fasrommet posisjon og bevegelsesmengde
t = np.linspace(0, 5, 500)

A = np.sqrt(29)/5
phi = 1.19
m = 2
k = 8
omega = np.sqrt(k/m)

x = A*np.cos(omega*t + phi)
p = -omega*A*np.sin(omega*t + phi) * m

plt.plot(x, p)
plt.title('Phase-space', weight='bold')
plt.xlabel('x [m]', weight='bold'); plt.ylabel('p [m/s]', weight='bold')
plt.axis('equal')
plt.show()

"""
Ep = 0.5*k*x**2
Ek = 0.5*p**2 / m

plt.plot(t, Ek, 'b', label=r'$E_k$')
plt.plot(t, Ep, 'r', label=r'$E_p$')
plt.plot(t, Ep + Ek, 'purple', label=r'$E_{tot}$')
plt.legend()
plt.show()
"""

# e) Gjør likningene dimensjonsløse
"""
A: [m]
omega: [1/s]
k: m/s^2
m: kg

Kan identifisere hva som gir likningene dimensjons og fjerne konstanter

x(t): [m]: A*cos(omega*t + phi) -> cos(omega*t + phi)
v(t): [m]: -omega*A*sin(omega*t + phi) -> sin(omega*t + phi)

Litt mer formelt velger man skaleringsfaktorer:
T = -1/omega, X = A

-> V = X/T = -omega*A

x* = x / X = cos(omega*t + phi)
v* = v / V = sin(omega*t + phi)

P = m*V -> p* = p / P = v* = sin(omega*t + phi)
"""

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.suptitle('Phase-space', weight='bold')

X = A
T = -1 / omega
V = X / T
P = m*V

x_s = x / X
p_s = p / P

ax1.set_title('Non-dimensionless', weight='bold')
ax1.plot(x, p)
ax1.set_xlabel('x [m]', weight='bold'); ax1.set_ylabel('p [m/s]', weight='bold')
ax1.axis('equal')

ax2.set_title('Dimensionless', weight='bold')
ax2.plot(x_s, p_s, 'r')
ax2.set_xlabel('x [-]', weight='bold'); ax2.set_ylabel('p [-]', weight='bold')
ax2.axis('equal')

fig.tight_layout()
plt.show()

t = np.linspace(0, 10, 400)
x = abs(np.cos(t))
plt.plot(t,x)
plt.show()
