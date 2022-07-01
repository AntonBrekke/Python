import numpy as np
import matplotlib.pyplot as plt

# a)
# konstanter gitt i oppgave
k0 = 1e-6
kL = 1e-1
rho0 = 1500
rhoL = 2500

N = 3000        # Antall nerveceller

# [m]
b0 = 1e-4
h0 = 3e-4
bL = 3e-4
hL = 1e-4

L = 3e-2    # Total

x = np.linspace(0, L, N)

# Antar lineære først
# k = (kL - k0) / L * x + k0
# rho = (rhoL - rho0) / L * x + rho0
k = np.linspace(k0, kL, N)
klog = np.logspace(np.log10(k0), np.log10(kL), N)       # Base = 10

# klog = np.log10(np.linspace(10**k0, 10**kL, N))

rho = np.linspace(rho0, rhoL, N)

dl = L / N

V = np.linspace(b0, bL, N) * np.linspace(h0, hL, N) * dl
# V = ((bL - b0) / L * x + b0) * ((hL - h0) / L * x + h0) * dl

m = rho * V

omegalog = np.sqrt(klog / m)
omega = np.sqrt(k / m)
# omega = omegalog

f = omega / (2*np.pi)
flog = omegalog / (2*np.pi)

plt.plot(x, f, 'royalblue', label='linear k')
plt.plot(x, flog, 'r', label='logarithmic k')
plt.xlabel('length [m]', weight='bold'); plt.ylabel('frequency [Hz]', weight='bold')
plt.legend()
plt.show()

# b)
f1 = 261.63
f2 = 277.18
omegaF1 = 2*np.pi*f1        # Hz
omegaF2 = 2*np.pi*f2

F = 1
slice = np.where(f < 400)

"""
b = np.linspace(1e-9, 1e-6, len(slice[0]))[None,:]

m = m[slice][:,None]
omega = omega[slice][:,None]
x = x[slice][:,None]

A1 = F / (m*np.sqrt((omega**2 - omegaF1**2)**2 + (b*omegaF1 / m)**2))
A2 = F / (m*np.sqrt((omega**2 - omegaF2**2)**2 + (b*omegaF2 / m)**2))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, b, A1, cmap='viridis', alpha=0.8)
ax.plot_surface(x, b, A2, cmap='jet', alpha=0.8)
"""

fig, axes = plt.subplots(2,2)

# Slicer så det er lettere å se på plot
space = np.linspace(-6, -9, 4)
b = 10**space[:,None]

A1 = F / (m*np.sqrt((omega**2 - omegaF1**2)**2 + (b*omegaF1 / m)**2))
A2 = F / (m*np.sqrt((omega**2 - omegaF2**2)**2 + (b*omegaF2 / m)**2))

for i, ax in enumerate(axes.flat):
    ax.plot(x, A1[i], 'royalblue', label=f'f = {f1} [Hz]')
    ax.plot(x, A2[i], 'r', label=f'f = {f2} [Hz]')
    ax.set_xlabel('length [m]', weight='bold'); ax.set_ylabel('Amplitude [m]', weight='bold')
    title = r'10^{' + f'{b[i]}'.strip('[]')[-3::2] + '}'
    ax.set_title(fr'b = ${title}$ [kg/s]', fontweight='bold')
    ax.legend()

fig.tight_layout()
plt.show()

fig, axes = plt.subplots(2,2)

# Slicer så det er lettere å se på plot
space = np.linspace(-6, -9, 4)
b = 10**space[:,None]
m_slice = m[slice][None,:]
omega_slice = omega[slice][None,:]
x_slice = x[slice]
k_slice = k[slice][None,:]
print(f'b = {b}')

# Amplituderesponsen 
A1 = F / (m_slice*np.sqrt((omega_slice**2 - omegaF1**2)**2 + (b*omegaF1 / m_slice)**2))
A2 = F / (m_slice*np.sqrt((omega_slice**2 - omegaF2**2)**2 + (b*omegaF2 / m_slice)**2))

for i, ax in enumerate(axes.flat):
    ax.plot(x_slice, A1[i], 'royalblue', label=f'f = {f1} [Hz]')
    ax.plot(x_slice, A2[i], 'r', label=f'f = {f2} [Hz]')
    ax.set_xlabel('length [m]', weight='bold'); ax.set_ylabel('Amplitude [m]', weight='bold')
    title = r'10^{' + f'{b[i]}'.strip('[]')[-3::2] + '}'
    ax.set_title(fr'b = ${title}$ [kg/s]', fontweight='bold')
    ax.legend()

fig.tight_layout()
plt.show()

# c)
# Finner Q-faktor der amplituden er størst
maxA1 = np.max(A1, axis=1)[:,None]
maxA2 = np.max(A2, axis=1)[:,None]
wheremax1 = np.where(A1 == maxA1)
wheremax2 = np.where(A2 == maxA2)
Q = np.sqrt(k*m / b**2)
print(Q.shape, A1.shape)

max1b3 = wheremax1[1][3]        # Max for b = 1e-8 for f1
max2b3 = wheremax2[1][3]        # Max for b = 1e-8 for f2

print(f'm1b3 = {m[max1b3]}kg, m2b3 = {m[max2b3]}kg')
print(f'k1b3 = {k[max1b3]}kg/s, k2b3 = {k[max2b3]}kg/s')

Q1 = Q[wheremax1]       # Max Q for f1
Q2 = Q[wheremax2]       # Max Q for f2
print(f'Q1 = {Q1}')
print(f'Q2 = {Q2}')
plt.plot(x, Q.transpose(1,0))
plt.xlabel('x [m]', weight='bold')
plt.ylabel('Q-factor [-]', weight='bold')
plt.legend([f'b={c[0]}' for c in b])
plt.show()

# d)
# Finner svingetid etter endt ytre kraft
T = 1 / f1
t = Q1[3] / (2*np.pi) * T
print(t)
t2 = Q1[3] / omega[max1b3]
print(t2)
