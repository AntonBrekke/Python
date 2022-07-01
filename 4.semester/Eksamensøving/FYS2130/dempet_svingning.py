import numpy as np
import matplotlib.pyplot as plt
import FYS2130_FreqAn as fa
from scipy.io import wavfile

b = 1
m = 1
k = 100
omega = np.sqrt(k / m)
gamma = b / (2*m)
# print(omega, gamma)
omegad = np.sqrt(omega**2 - gamma**2)
A = 1
T = 10
Nt = 10000
dt = T / (Nt-1)
fs = 1 / dt     # Sample-frekvens
t = np.linspace(0, T, Nt)
# print(dt, t[1]-t[0])
y = A*np.exp(-gamma*t)*np.cos(omegad*t)     # Løsning så lenge gamma < omega
# y = (np.sin(2*omega*t)*(t < 4) + np.cos(5*omega*t) * (t > 4)) * np.exp(-0.5*gamma*t)       # Test
# plt.plot(t, y)
# plt.show()

# print(omega / (2*np.pi))
"""
# Tester ny kode med eksempel fra oblig som jeg vet hvordan skal se ut
fs, data = wavfile.read('mistle_thrush.wav')    # data er det samplede lydsignalet
y = data[:,0]
omega_a = np.linspace(1800, 4000, 200) * 2*np.pi
"""
omega_a = np.linspace(1, 10, 200) * 2*np.pi
osc = fa.Freq_Analysis(y, fs)
osc.plot_Fourier(show=False)        # Holder igjen plot så jeg kan se det sammen med WT transformasjon
osc.faster_wavelet_diagram(omega_a, 10, ani=True)
# Virker som at modulen funker fint
