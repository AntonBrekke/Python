import numpy as np
import matplotlib.pyplot as plt

# Setter parametere
C = 1e-10
R = 1e11
r = 1e6
V0 = 100e-3

Vr = 50e-3

# Lager puls-funksjon
def Vpulse(t, t0, V0):
    return V0*np.sin(2*np.pi*t/t0)

# Lager funksjoner for resistans
def VGR(V):
    vgR = R*(V >= Vr)
    if vgR == 0:
        vgR = np.inf
    return vgR

def nR(V):
    return R

T = 0.1     # Simulasjons-lengde
t0 = T*0.1      # Puls-lengde
dt = 0.1*C*r
nsteps = int(T/dt)  # Antall tidssteg
N = 100    # Antall kapasitatorer
t = np.zeros((nsteps, 1))

def cableeq(resistance):
    V = np.zeros((nsteps, N))
    V[0,0] = Vpulse(0, t0, V0)      # Initialbetingelse ved t=0
    print(f'Resistance is {resistance.__name__}')
    for i in range(0, nsteps-1):
        t[i+1] = t[i] + dt
        V[i+1, 0] = Vpulse(t[i+1], t0, V0)     # Venstre grense
        for j in range(1, N-1):      # Interne komponenter
            V[i+1, j] = V[i, j] + (dt/C)*((V[i, j+1] - 2*V[i, j]+V[i, j-1]) / r - V[i,j] / resistance(V[i,j]))
        # Høyre grense
        V[i+1, N-1] = V[i, N-1] + (dt/C)*((-V[i, N-1]+V[i, N-2]) / r - V[i, N-1] / resistance(V[i, N-1]))
    return V

V = cableeq(VGR)
# Plotter V for hver node over tid
for j in range(0, N, 10):
    plt.plot(t, V[:,j], label=f'Node: {j}')
plt.xlabel('t')
plt.ylabel('V')
plt.legend()
plt.show()

# Maks amplitude i funksjonen
plt.plot(t, np.amax(V, axis=1))
plt.show()

# Plotter V for hver node ved ulike tidspunkter
for i in range(0, nsteps, 1000):
    plt.plot(V[i,:], label=f't={t[i,0]:.2f}')
plt.legend()
plt.show()
