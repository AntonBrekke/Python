import FYS2130_FreqAn as fa
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, data = wavfile.read('water-filled-cup.wav')    # data er det samplede lydsignalet
fs, data = wavfile.read('guitar.wav')    # data er det samplede lydsignalet
print(f'fs: {fs}')
N = len(data)
dt = 1 / fs
T = N*dt
t = np.linspace(0, T, N)

analyse = fa.Freq_Analysis(data, fs)
FT_freq, X_k = analyse.FourierTransform()

analyse.faster_wavelet_diagram(1, 4000, K=1000, show=False)
analyse.faster_wavelet_diagram(4000, 8000, K=2000, show=False)
analyse.faster_wavelet_diagram(8000, 12000, K=3000, show=True)
