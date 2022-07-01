from scipy.io.wavfile import write
import numpy as np

samplerate = 44100; fs = 100
t = np.linspace(0., 5, samplerate)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2. * np.pi * fs * t)
write("example.wav", samplerate, data.astype(np.int16))
