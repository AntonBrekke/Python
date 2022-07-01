import numpy as np
import matplotlib.pyplot as plt

# Setter parametere
C = 1e-10
R = 1e8
r = 1e6
V0 = 100e-3

Vr = 50e-3

# Lager puls-funksjon
def Vpulse(t, t0, V0):
    return V0*np.sin(np.pi*t/t0)*(t >= 0 and t <= t0)

# Lager funksjoner for resistans
def VGR(V):
    vgR = R*(V >= Vr)
    if vgR == 0:
        vgR = np.inf
    return vgR

# Konstant puls, det samme som å la R være konstant, men pakket inn i en funksjon
def nR(V):
    return R

T = 0.1     # Simulasjons-lengde
t0 = T*0.1      # Puls-lengde
dt = 0.1*C*r
nsteps = int(T/dt)  # Antall tidssteg
N = 100    # Antall kapasitatorer
t = np.zeros((nsteps, 1))

# Løser problemet med kabellikningen
def cableeq(resistance):
    V = np.zeros((nsteps, N))
    V[0,0] = Vpulse(0, t0, V0)      # Initialbetingelse ved t=0
    print(f'Resistance is {resistance.__name__}')
    for i in range(0, nsteps-1):
        t[i+1] = t[i] + dt
        # Høyre grense
        V[i+1, N-1] = V[i, N-1] + (dt/C)*((-V[i, N-1] + V[i, N-2]) / r - V[i, N-1] / resistance(V[i, N-1]))
        # Venstre grense
        V[i+1, 0] = Vpulse(t[i+1], t0, V0)
        for j in range(1, N-1):      # Interne komponenter
            V[i+1, j] = V[i, j] + (dt/C)*((V[i, j+1] - 2*V[i, j] + V[i, j-1]) / r - V[i,j] / resistance(V[i,j]))
    return V

V1 = cableeq(nR)
V2 = cableeq(VGR)
# Noen tester jeg har gjort
print(np.max(V1))
print(np.max(V2))
print(V1==V2)
print(np.all(V1==V2))

# Plotter V for hver node over tid
fig, (ax1, ax2) = plt.subplots(2,1)
for j in range(0, N, 10):
    ax1.plot(t, V1[:,j]/np.max(V1[:,j]), label=f'Node: {j}')
    ax2.plot(t, V2[:,j]/np.max(V2[:,j]), label=f'Node: {j}')
ax1.set_title('Normal R', weight='bold')
ax2.set_title('Volt-gated R(V)', weight='bold')
ax1.set_xlabel('t', weight='bold')
ax2.set_xlabel('t', weight='bold')
ax1.set_ylabel('V', weight='bold')
ax2.set_ylabel('V', weight='bold')
ax1.legend(loc='right', prop={'size':6})
ax2.legend(loc='right', prop={'size':6})
fig.tight_layout()
plt.show()

# Maks amplitude i funksjonen
plt.plot(t, np.amax(V1, axis=1))
plt.plot(t, np.amax(V2, axis=1))
plt.xlabel('t')
plt.ylabel(r'$V_{max}$')
plt.show()

# Plotter V for hver node ved ulike tidspunkter
fig, (ax1, ax2) = plt.subplots(2,1)
for i in range(0, nsteps, 1000):
    if i != 0:
        ax1.plot(V1[i,:]/np.max(V1[i,:]), label=f't={t[i,0]:.2f}')
        ax2.plot(V2[i,:]/np.max(V2[i,:]), label=f't={t[i,0]:.2f}')
    else:
        ax1.plot(V1[i,:], label=f't={t[i,0]:.2f}')
        ax2.plot(V2[i,:], label=f't={t[i,0]:.2f}')
    print(np.all(V1[i,:]==V2[i,:]))     # Bare en test jeg har gjort
ax1.set_title('Normal R', weight='bold')
ax2.set_title('Volt-gated R(V)', weight='bold')
ax1.set_xlabel('Node', weight='bold')
ax2.set_xlabel('Node', weight='bold')
ax1.set_ylabel('V', weight='bold')
ax2.set_ylabel('V', weight='bold')
ax1.legend(loc='right', prop={'size':6})
ax2.legend(loc='right', prop={'size':6})
fig.tight_layout()
plt.show()
