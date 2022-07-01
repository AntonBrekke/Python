import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

"""
f = 1 / (2*L) * np.sqrt(T / mu)
"""

# A2-note av gitar

L = 0.65    # m, lengden av strengen
mu = 0.034    # kg / m, tettheten av strengen
f = 110     # Hz, frekvens på note
T = (2*L * f)**2 * mu       # N, hvor stram strengen må være
print(f'String tension: {T} N')
lmbda = 313.64e-2    # m, bølgelengde
omega = 2*np.pi*f
k = 2*np.pi / lmbda    # 1 / m, x = L =>

fs = 44100

t = np.linspace(0, 1, fs)
Amax = np.iinfo(np.int16).max
b = 3

def A(t):
    return Amax*np.exp(-b*t)

def signal(t, omega):
    return A(t) * np.sin(omega*t)

def func(x):
    return np.cos(x)*np.sin(x)

data_signal = 0
for i in range(0, 1):
    data_signal += signal(t, omega)
print(Amax)

plt.plot(t, data_signal)
plt.show()

data = wavfile.write('test.wav', fs, data_signal.astype(np.int16))
