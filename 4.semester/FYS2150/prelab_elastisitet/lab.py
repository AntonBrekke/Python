import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd
from scipy.io import wavfile
from playsound import playsound

lab = vd.Visualize()
step = 0.5

m = np.arange(0, 3.5 + step, step)      # kg
baseline = 827       # m
h = -np.array([827, 754.5, 684, 611, 537, 465.5, 396, 327])*1e-2 * 1e-3      # m
lab.regdata(m, h)
vd.show()

l = 1.34       # m, mellom punktene staven ligger på
g = 9.81            # m / s^2
A = lab.line.slope      # m / kg
d = 16.03e-3        # m

dl = 0.002          # m
dA = lab.line.stderr       # m / kg
dd = 0.05e-3        # m
dg =  0         # m / s^2

def find_E(l, g, A, d):
    E = 4*l**3*g / (3*np.pi * abs(A)*d**4)
    print(f'\nE: {E:.5e} Pa')
    return E

def find_dE(l, g, A, d, dl, dg, dA, dd):
    dE = np.sqrt((4*l**2*g / (abs(A)*d**4) * dl)**2 + (4*l**3*g*A / (3*np.pi*abs(A)*d**4) * dA)**2
               + (16*l**3*g / (3*np.pi*abs(A)*d**3)*dd)**2 + (4*l**3 / (3*np.pi*abs(A)*d**4) * dg)**2)
    print(f'\ndE: {dE:.5e} Pa')
    return dE


E = find_E(l, g, A, d)
dE = find_dE(l, g, A, d, dl, dg, dA, dd)
L = 1.49    # m, hele staven
dL = 0.002      # m
M = 2.5035        # kg
dM = 1e-3       # kg
d = 16.03e-3        # m
dd = 0.05e-3        # m


def find_f(d, E, M, L):
    f = d / 4 * np.sqrt(np.pi*E / (M*L))
    print(f'\nf: {f} Hz')
    return f

def find_df(d, E, M, L, dd, dE, dM, dL):
    df = np.sqrt((1/4 * np.sqrt(np.pi * E / (M*L)) * dd)**2
               + (d/8 * np.sqrt(np.pi / (M*L*E)) * dE)**2
               + (d/8 * np.sqrt(np.pi * E / (L*M**3)) * dM)**2
               + (d/8 * np.sqrt(np.pi * E / (M*L**3)) * dL)**2)
    print(f'\ndf: {df} Hz')
    return df

f = find_f(d, E, M, L)
df = find_df(d, E, M, L, dd, dE, dM, dL)

def sveving(f=0, lydfil=''):
    fs, wavdat = wavfile.read(lydfil)
    N = len(wavdat)
    dt = 1 / fs
    T = N*dt
    print(f'\nfs: {fs}, N: {N}')
    A = 1       # Amplitude
    t = np.linspace(0, T, int(N))
    writedat = A * np.sin(2*np.pi*f*t) + wavdat
    wavfile.write('temp.wav', fs, writedat.astype(np.float32))
    playsound('temp.wav')

# sveving(f=1106, lydfil='messing_lyd.wav')

def find_E_from_f(f, d, M, L):
    E = (4*f / d)**2*M*L / np.pi
    print(f'\nE: {E:.5e} Pa')
    return E

def find_dE_from_f(f, d, M, L, df, dd, dM, dL):
    dE = np.sqrt((32*f*M*L / (np.pi*d**2))**2 + (16*f**2*L / (np.pi*d**2) * dM)**2 + (16*f**2*M / (np.pi*d**2) * dL)**2)
    print(f'\ndE: {dE:.5e} Pa')
    return dE
#
f = 1.179e3       # Hz
df = 0.002e3        # Hz

find_E_from_f(f, d, M, L)
find_dE_from_f(f, d, M, L, df, dd, dM, dL)

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

# plt.close()
# plot_Fourier(wavdat, N, 1 / fs, title='FT')
# vd.show()
