import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd
from scipy.io import wavfile
from playsound import playsound

data = np.loadtxt('maalinger_h.dat')

m = data[:,0]       # kg
h = data[:,1]       # mm

"""
Antar lineær sammenheng, h = Am + b
"""

lab = vd.Visualize()
lab.regdata(m, h)
vd.show()

l = 1.213       # m
g = 9.81            # m / s^2
A = -1.393e-3           # m / kg
d = 14.91e-3        # m

dl = 0.002          # m
dA = 0.021e-3       # m / kg
dd = 0.03e-3        # m
dg =  0         # m / s^2

E = 4*l**3*g / (3*np.pi * abs(A)*d**4)
# Regner ut dE
dE = np.sqrt((4*l**2*g / (abs(A)*d**4) * dl)**2 + (4*l**3*g*A / (3*np.pi*abs(A)*d**4) * dA)**2
           + (16*l**3*g / (3*np.pi*abs(A)*d**3)*dd)**2 + (4*l**3 / (3*np.pi*abs(A)*d**4) * dg)**2)

print(f'\nYoungs Modulus E: {E:.3e} +- {dE:.3e}')       # prelab : 108 +- 2 GPa

E = 107e9       # GPa
L = 1.530    # m
M = 2.500        # kg
# Bruker samme d

fhat = d / 4 * np.sqrt(np.pi*E / (M*L))
print(f'\nfhat: {fhat}')

fs, wavdat = wavfile.read('messing_lyd.wav')
N = len(wavdat)
dt = 1 / fs
T = N*dt
print(f'\nfs: {fs}, N: {N}')

A = 1       # Amplitude

def sound(f, t):
    return A * np.sin(2*np.pi*f*t)

fhat = 1.106e3         # Hz
t = np.linspace(0, T, int(N))
writedat = sound(fhat, t) + wavdat
wavfile.write('temp.wav', fs, writedat.astype(np.float32))
wavfile.write('temp2.wav', fs, wavdat.astype(np.float32))
playsound('temp.wav')

def plot_Fourier(data, N, dt, title='', xlim=None):
    X_k = np.fft.fft(data)   # FT av samplet frekvens
    FT_freq = np.fft.fftfreq(int(N), dt)     # FT-frekvens (korrekt)
    t = np.linspace(0, N*dt, int(N))

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.plot(t, data, label='Sampled signal')
    ax2.plot(FT_freq, abs(X_k), label='Fourier Transform')
    fig.suptitle('Fourier Transform', weight='bold', fontsize=20)
    ax1.set_xlabel('t [s]', weight='bold', fontsize=18)
    ax1.set_ylabel('x_n', weight='bold', fontsize=18)
    ax2.set_xlabel('f [Hz]', weight='bold', fontsize=18)
    ax2.set_ylabel('X_k', weight='bold', fontsize=18)
    if xlim is not None:
        ax2.set_xlim(-xlim, xlim)    # Setter grenser på begge plott så det blir enklere å se, siden de har ulike nyquistfrekvenser

    fig.tight_layout()
    ax1.legend(prop={'size':14}); ax2.legend(prop={'size':14})

plt.close()
plot_Fourier(wavdat, N, 1 / fs, title='FT')
vd.show()
