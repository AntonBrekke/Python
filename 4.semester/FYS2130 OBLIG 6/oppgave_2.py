import numpy as np
import matplotlib.pyplot as plt

# a)
# Definerer konstanter gitt i oppgave
A1 = 1.0    # m
f1 = 100    # Hz
t1 = 0.2    # s
std1 = 0.05 #s

A2 = 1.7    # m
f2 = 160    # Hz
t2 = 0.6    # s
std2 = 0.1 #s

# Samme som i oppgave 1
fs = 1e3       # Hz
T = 1       # Total samplingstid
dt = 1 / fs     # Tid mellom hvert samplingspunkt
N = int(T / dt)      # Antall samplingspunkter

def f(t):
    f = A1*np.sin(2*np.pi*f1*t)*np.exp(-((t-t1)/std1)**2) + A2*np.sin(2*np.pi*f2*t)*np.exp(-((t-t2)/std2)**2)
    # f = np.sin(2*np.pi*f1*t)
    return f

t = np.linspace(0, T, N)
x_n = f(t)      # Samplet frekvens
X_k = np.fft.fft(x_n)   # FT av samplet frekvens
FT_freq = np.fft.fftfreq(N, dt)     # FT-frekvens (korrekt)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(t, x_n)
ax1.set_xlabel('t [s]', weight='bold')
ax1.set_ylabel('A [m]', weight='bold')
ax1.set_title('Incoming signal', weight='bold')
ax2.bar(FT_freq, abs(X_k))
ax2.set_xlabel('freq [Hz]', weight='bold')
ax2.set_ylabel('X_k', weight='bold')
ax2.set_title('Fourier Transform', weight='bold')

ax2in = ax2.inset_axes([0.05, 0.4, 0.2, 0.5])
ax2in.bar(FT_freq, abs(X_k))
ax2in.set_xlim(80, 175)
ax2.indicate_inset_zoom(ax2in, edgecolor="black")

fig.tight_layout()

# b)
tn = t.copy()
tk = t.copy()
omega_a = np.logspace(np.log10(2*np.pi*80), np.log10(2*np.pi*200), 100)

# Kun for plotting
tnp, freq_ap = np.meshgrid(tk, omega_a / (2*np.pi), indexing='ij')

def wavelet(tn, omegaa, tkk, K):
    C = 0.798 * omegaa / (fs*K)
    # C = 1
    w = C*(np.exp(-1j*omegaa*(tn - tkk)) - np.exp(-K**2))*np.exp(-omegaa**2 * (tn - tkk)**2 / (2*K)**2)
    """
    Animerer for å sjekke om wavelet faktisk beveger seg gjennom signal
    (C=1 hensiktsmessig her)
    """
    # plt.plot(tn, x_n, 'k')
    # plt.plot(tn, np.real(w))
    # plt.plot(tn, np.imag(w))
    # plt.draw()
    # plt.ylim(-A2, A2)
    # plt.pause(0.01)
    # plt.clf()
    return w

def wavelet_transform(sign, omegaa, tkk, K):
    gamma = np.sum(sign * wavelet(tn, omegaa, tkk, K).conjugate())
    return gamma

def wavelet_diagram(K):
    N = len(tk)
    M = len(omega_a)
    WT = np.zeros([N, M], dtype=np.complex128)
    for m in range(M):
        for n in range(N):
            WT[n,m] = wavelet_transform(x_n, omega_a[m], tk[n], K)

    return WT

import time

time1 = time.time()
WT1 = wavelet_diagram(K=6)
WT2 = wavelet_diagram(K=60)
time2 = time.time()
print(f'wavelet_diagram ran in {time2 - time1}')

fig = plt.figure()
fig.suptitle('Wavelet Transform', weight='bold')
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
p1 = ax1.contourf(tnp, freq_ap, abs(WT1), levels=300, cmap='hot')
p2 = ax2.contourf(tnp, freq_ap, abs(WT2), levels=300, cmap='hot')
cbar_ax1 = fig.colorbar(p1, ax=ax1)
cbar_ax2 = fig.colorbar(p2, ax=ax2)

cbar_ax1.set_label('Amplitude', weight='bold')
cbar_ax2.set_label('Amplitude', weight='bold')
ax1.set_xlabel('t [s]', weight='bold'); ax1.set_ylabel('freq [1/s]', weight='bold')
ax2.set_xlabel('t [s]', weight='bold'); ax2.set_ylabel('freq [1/s]', weight='bold')
ax1.set_title('K = 6', weight='bold')
ax2.set_title('K = 60', weight='bold')

fig.tight_layout()
plt.show()
