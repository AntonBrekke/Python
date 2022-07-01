import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time

"""
Anton Brekke / antonabr@uio.no
Egen kode
"""

class Freq_Analysis:
    def __init__(self, sampled_signal, fs, t):
        self.sampled_signal = sampled_signal
        self.fs = fs    # Sample frekvens
        self.t = t
        self.T = t[-1] - t[0]      # Total samplingstid
        self.dt = 1 / fs    # Tid mellom samplingspunkter
        self.N = len(t)      # Antall samplingspunkter

    def FourierTransform(self):
        x_n = self.sampled_signal
        X_k = np.fft.fft(x_n)   # FT av samplet frekvens
        FT_freq = np.fft.fftfreq(self.N, self.dt)     # FT-frekvens (korrekt)

        return FT_freq, X_k

    # Morlet-Wavelet
    def wavelet(self, tn, omega_a, tk, K):
        C = 0.798 * omega_a / (fs*K)
        # C = 1
        w = C*(np.exp(-1j*omega_a*(tn - tk)) - np.exp(-K**2))*np.exp(-omega_a**2 * (tn - tk)**2 / (2*K)**2)
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

    # Wavelet-transformasjon i tidsdomenet
    def wavelet_transform(self, x_n, omega_a, tk, K):
        tn = self.t.copy()
        gamma = np.sum(x_n * self.wavelet(tn, omega_a, tk, K).conjugate())
        return gamma

    # Lager selve diagrammet ved å iterere gjennom verdier
    def wavelet_diagram(self, omega_a, K):
        x_n = self.sampled_signal.copy()
        self.tk = self.t.copy()
        self.omega_a = omega_a
        N = len(self.tk)
        M = len(omega_a)
        WT = np.zeros([N, M], dtype=np.complex128)
        for m in range(M):
            for n in range(N):
                WT[n,m] = self.wavelet_transform(x_n, self.omega_a[m], self.tk[n], K)

        return WT

    # Fouriertransform av Morlet-wavelet
    def FT_wavelet(self, omega, omega_a, K):
        w = 2 * (np.exp(-(K * (omega - omega_a)/omega_a)**2) - np.exp(-K**2) * np.exp(-(K*omega/omega_a)**2))
        return w

    # Den raskere algoritmen som bruker Konvolusjonsteoremet i frekvensdomenet
    def faster_wavelet_diagram(self, omega_a, K):
        tk = self.t.copy()
        omega_a_mesh, tk_mesh = np.meshgrid(omega_a, tk, indexing='ij')
        omega_0 = np.fft.fftfreq(self.N, self.dt) * 2*np.pi
        x_n = self.sampled_signal.copy()
        x_nFT = np.fft.fft(x_n)
        N = len(tk)
        M = len(omega_a)
        WT = np.zeros([M, N], dtype=np.complex128)
        for i in range(M):
            WT[i, :] = np.fft.ifft(x_nFT * self.FT_wavelet(omega_0, omega_a[i], K)) # Konvolusjonsteoremet
        return tk_mesh, omega_a_mesh, WT
# 1a)
A = 1.0     # m

def g(t, f):
    return A*np.sin(2*np.pi*f*t)

fs = 1e3       # Samplingsfrekvens, Hz
T = 1       # Total samplingstid
dt = 1 / fs     # Tid mellom hvert samplingspunkt
N = int(T / dt)      # Antall samplingspunkter
f = 200     # Frekvens vi analyserer
t = np.linspace(0, T, N)        # Array for signal

x_n = g(f, t)

analyse1 = Freq_Analysis(x_n, fs, t)
FT_freq, X_k = analyse1.FourierTransform()

# Plotter FT
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(t, x_n, color='royalblue', linestyle='solid', marker='o')
ax1.set_xlabel('t [s]', weight='bold'); ax1.set_ylabel('Amplitude [m]', weight='bold')
ax2 = fig.add_subplot(212)
ax2.bar(FT_freq, abs(X_k))
ax2.set_xlabel('freq [Hz]', weight='bold'); ax2.set_ylabel('X_k', weight='bold')

ax1in = ax1.inset_axes([0.8, 0, 0.2, 0.3])
ax1in.plot(t, x_n, color='royalblue', linestyle='solid', marker='o')
ax1in.set_xlim(0.5, 0.55)
ax1in.set_xticks([])
ax1in.set_yticks([])
ax1.indicate_inset_zoom(ax1in, edgecolor="black")

fig.tight_layout()
plt.show()

# 1b)
f_list = [800, 1400, 1800]      # Liste med frekvenser som plottes, Hz

# Funksjon som lager n antall plots
def make_FT_plots(f_list):
    n = len(f_list)
    fig, ax = plt.subplots(n, 2)
    fig.suptitle('Aliasing', weight='bold')
    c = plt.rcParams['axes.prop_cycle'].by_key()['color']
    c[0], c[1] = 'royalblue', 'r'
    for i, f in enumerate(f_list):
        x_n = g(t, f)       # Skifter frekvens på samplet signal
        analyse = Freq_Analysis(x_n, fs, t)
        FT_freq, X_k = analyse.FourierTransform()
        line, = ax[i, 0].plot(t, x_n, color=c[i], linestyle='solid')
        ax[i,0].set_xlabel('t [s]', weight='bold'); ax[i,0].set_ylabel('A [m]', weight='bold')
        ax[i,0].set_title(f'freq = {f}Hz', weight='bold')
        ax[i, 1].bar(FT_freq, abs(X_k), color=line.get_color())
        ax[i,1].set_xlabel('freq [Hz]', weight='bold'); ax[i,1].set_ylabel('X_k', weight='bold')
        ax[i,1].set_title(f'freq = {f}Hz', weight='bold')
    fig.tight_layout()

# Henter plots og viser
make_FT_plots(f_list)
plt.show()

# 2a)
# Definerer konstanter fra oppgave
A1 = 1.0    # m
f1 = 100    # Hz
t1 = 0.2    # s
std1 = 0.05 #s

A2 = 1.7    # m
f2 = 160    # Hz
t2 = 0.6    # s
std2 = 0.1 #s

# Signal gitt i oppgave
def f(t):
    f = A1*np.sin(2*np.pi*f1*t)*np.exp(-((t-t1)/std1)**2) + A2*np.sin(2*np.pi*f2*t)*np.exp(-((t-t2)/std2)**2)
    return f

x_n = f(t)      # Samplet signal fra ny funksjon
analyse2 = Freq_Analysis(x_n, fs, t)
FT_freq, X_k = analyse2.FourierTransform()

# Plotter FT
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
# plt.show()

# 2b / c)
# Definerer analysefrekvens (vinkelfrekvens)
omega_a = np.logspace(np.log10(2*np.pi*80), np.log10(2*np.pi*200), 100)

# Finner wavelet-transformasjonen med ulike K-verdier, tar tiden på koden
time1 = time.time()
WT1 = analyse2.wavelet_diagram(omega_a, K=6)
WT2 = analyse2.wavelet_diagram(omega_a, K=60)
time2 = time.time()
print(f'wavelet_diagram ran in {time2 - time1}')

# Kun for plotting, lager meshgrid
t_mesh, freq_mesh = np.meshgrid(t, omega_a / (2*np.pi), indexing='ij')

# Plotter WT
fig = plt.figure()
fig.suptitle('Wavelet Transform', weight='bold')
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
p1 = ax1.contourf(t_mesh, freq_mesh, abs(WT1), levels=300, cmap='hot')
p2 = ax2.contourf(t_mesh, freq_mesh, abs(WT2), levels=300, cmap='hot')
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

# 3a)
fs, data = wavfile.read('mistle_thrush.wav')    # data er det samplede lydsignalet
print(fs)       # Samplingsfrekvens
data = data[:,0]  # Returnerer to kanaler for stereo, omtrent identiske
N = len(data)   # Antall datapunkter
dt = 1 / fs     # Tid mellom hvert samplede punkt
T = N*dt        # Total samplingstid
t = np.linspace(0, T, N)

analyse3 = Freq_Analysis(data, fs, t)

FT_freq, X_k = analyse3.FourierTransform()
"""
# Tar lang tid å kjøre, så kommenterer den ut
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(t, data)
ax1.set_xlabel('t [s]', weight='bold')
ax1.set_ylabel('A [m]', weight='bold')
ax1.set_title('Incoming signal', weight='bold')
ax2.bar(FT_freq, abs(X_k))
ax2.set_xlabel('freq [Hz]', weight='bold')
ax2.set_ylabel('X_k', weight='bold')
ax2.set_title('Fourier Transform', weight='bold')

ax2in = ax2.inset_axes([0.05, 0.4, 0.2, 0.5])
ax2in.bar(FT_freq, abs(X_k))
ax2in.set_xlim(2000, 3600)
ax2.indicate_inset_zoom(ax2in, edgecolor="black")

fig.tight_layout()
plt.show()
"""
# FFT gir meg ca. 1800 - 4000 Hz for analysefrekvens

# 3c / d)
N_skip = 6      # Høyetse lovlige skip, fs = 48000 N_skip = 6 -> fs = 8000. Vi har frekvenser på ca. 4000
t1 = 0.8
t2 = 1.0
time_interval = np.logical_and(t > t1, t < t2)      # Slicer intervallet
analyse3.t = t.copy()[time_interval][::N_skip]
analyse3.sampled_signal = data.copy()[time_interval][::N_skip]

omega_a = np.logspace(np.log10(2*np.pi*1800), np.log10(2*np.pi*4000), 100)
K = 40

# Finner wavelet-transformasjonen med ulike K-verdier
# Tar tiden på hvor lang tid det tar å generere diagrammet
time_start = time.time()
WT = analyse3.wavelet_diagram(omega_a, K)
time_end = time.time()
time_3 = time_end - time_start
print(f'wavelet_diagram ran in {time_3}')

# Kun for plotting, lager meshgrid
t_mesh, freq_mesh = np.meshgrid(t[time_interval][::N_skip], omega_a / (2*np.pi), indexing='ij')

# Plotter WT
fig = plt.figure()
fig.suptitle('Wavelet Transform', weight='bold')
ax = fig.add_subplot()
p = ax.contourf(t_mesh, freq_mesh, abs(WT), levels=300, cmap='hot')
cbar_ax = fig.colorbar(p, ax=ax)

cbar_ax.set_label('Amplitude', weight='bold')
ax.set_xlabel('t [s]', weight='bold'); ax.set_ylabel('freq [1/s]', weight='bold')
ax.set_title(f'K = {K}', weight='bold')

fig.tight_layout()
plt.show()

# 4a/b)
# Tester raskere algortime på samme data
t_new = t.copy()[time_interval][::N_skip]
data_new = data.copy()[time_interval][::N_skip]
fs *= 1/N_skip

analyse4 = Freq_Analysis(data_new, fs, t_new)

# Tar tiden det tar å lage diagram og genererer data som skal plottes
time_start = time.time()
t_mesh, omega_a_mesh, WT = analyse4.faster_wavelet_diagram(omega_a, K)
time_end = time.time()
time_4 = time_end - time_start
print(f'faster_wavelet_diagram ran in {time_4}')
print(f'WTFT-method is {time_3 / time_4} times faster than regular WT-method.')
"""
Fra terminal:
wavelet_diagram ran in 18.070337295532227
faster_wavelet_diagram ran in 0.013502836227416992
WTFT-method is 1338.262346605456 times faster than regular WT-method.
"""

# Plotter raskere WT
fig = plt.figure()
fig.suptitle('Faster Wavelet Transform', weight='bold')
ax = fig.add_subplot()

p = ax.contourf(t_mesh, omega_a_mesh / (2*np.pi), abs(WT), levels=300, cmap='hot')

cbar_ax = fig.colorbar(p, ax=ax)

cbar_ax.set_label('Amplitude', weight='bold')
ax.set_xlabel('t [s]', weight='bold'); ax.set_ylabel('freq [1/s]', weight='bold')
ax.set_title(f'K = {K}', weight='bold')

fig.tight_layout()
plt.show()

# 4c)
# Leser inn nytt lydsignal
fs, data = wavfile.read('tawny_owl.wav')    # data er det samplede signalet
print(fs)
data = data[:,0]  # Returnerer to kanaler for stereo, omtrent identiske
N = len(data)   # Antall datapunkter
dt = 1 / fs     # Tid mellom samplingspunkter
T = N*dt        # Total samplingstid
t = np.linspace(0, T, N)

# time_interval = np.logical_and(t > 1, t < 2.5)

analyse5 = Freq_Analysis(data, fs, t)
FT_freq, X_k = analyse5.FourierTransform()

"""
# Dette tar LANG tid
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(t, data)
ax1.set_xlabel('t [s]', weight='bold')
ax1.set_ylabel('A [m]', weight='bold')
ax1.set_title('Incoming signal', weight='bold')
ax2.bar(FT_freq, abs(X_k))
ax2.set_xlabel('freq [Hz]', weight='bold')
ax2.set_ylabel('X_k', weight='bold')
ax2.set_title('Fourier Transform', weight='bold')
#
ax2in = ax2.inset_axes([0.05, 0.4, 0.2, 0.5])
ax2in.bar(FT_freq, abs(X_k))
ax2in.set_xlim(0, 4000)
ax2in.set_ylim(0, 3300)
ax2.indicate_inset_zoom(ax2in, edgecolor="black")

fig.tight_layout()
plt.show()
"""
# FT-plot : freq [500 - 1000], tid [1s - 2.5s]

omega_a = np.logspace(np.log10(2*np.pi*500), np.log10(2*np.pi*1000), 500)
K = 40

# Plotter WT
fig = plt.figure()
fig.suptitle('Faster Wavelet Transform', weight='bold')
ax = fig.add_subplot()

# Tar tiden det tar å lage diagram og genererer data som skal plottes
time_start = time.time()
t_mesh, omega_a_mesh, WT = analyse5.faster_wavelet_diagram(omega_a, K)
time_end = time.time()
time_5 = time_end - time_start
print(f'faster_wavelet_diagram ran in {time_5}')

# Plotter kun hvert 10 punkt så matplotlib ikke bruker 1000 år på å plotte
p = ax.contourf(t_mesh[::10, ::10], omega_a_mesh[::10, ::10] / (2*np.pi), abs(WT)[::10, ::10], levels=300, cmap='hot')
cbar_ax = fig.colorbar(p, ax=ax)

cbar_ax.set_label('Amplitude', weight='bold')
ax.set_xlabel('t [s]', weight='bold'); ax.set_ylabel('freq [1/s]', weight='bold')
ax.set_title(f'K = {K}', weight='bold')

fig.tight_layout()
plt.show()


"""
Kjøretest fra terminal:
C:> python oppgaver.py
wavelet_diagram ran in 15.663588762283325
oppgaver.py:224: WavFileWarning: Chunk (non-data) not understood, skipping it.
  fs, data = wavfile.read('mistle_thrush.wav')    # data er det samplede lydsignalet
48000
wavelet_diagram ran in 18.07032328819275
faster_wavelet_diagram ran in 0.013503207038096264
WTFT-method is 1338.2245593370073 times faster than regular WT-method.
oppgaver.py:336: WavFileWarning: Chunk (non-data) not understood, skipping it.
  fs, data = wavfile.read('tawny_owl.wav')    # data er det samplede signalet
48000
faster_wavelet_diagram ran in 13.04445505142212
"""
