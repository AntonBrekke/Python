import numpy as np
import matplotlib.pyplot as plt

fs = 1e3       # Hz
T = 1       # Total samplingstid
dt = 1 / fs     # Tid mellom hvert samplingspunkt
N = int(T / dt)      # Antall samplingspunkter

def f(t):
    return np.sin(2*np.pi * 200 * t)

t = np.linspace(0, T, N)
x_n = f(t)      # Samplet frekvens
X_k = np.fft.fft(x_n)   # FT av samplet frekvens
FT_freq = np.fft.fftfreq(N, dt)     # FT-frekvens (korrekt)
x_n2 = np.fft.ifft(X_k)

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.plot(t, x_n)
ax1.set_xlabel('t [s]', weight='bold')
ax1.set_ylabel('A [m]', weight='bold')
ax2.bar(FT_freq, abs(X_k))
ax2.set_xlabel('freq [Hz]', weight='bold')
ax2.set_ylabel('X_k', weight='bold')
ax3.plot(t, x_n2)

fig.tight_layout()
plt.show()
