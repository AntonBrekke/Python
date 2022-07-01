import numpy as np
import matplotlib.pyplot as plt

# a)
A = 1.0     # m

def g(t, f):
    return A*np.sin(2*np.pi*f*t)

fs = 1e3       # Hz
T = 1       # Total samplingstid
dt = 1 / fs     # Tid mellom hvert samplingspunkt
N = int(T / dt)      # Antall samplingspunkter
f = 200

fig = plt.figure()
ax1 = fig.add_subplot(211)
t = np.linspace(0, T, N)
x_n = g(t, f)
ax1.plot(t, x_n, color='royalblue', linestyle='solid', marker='o')
# plt.show()
X_k = np.fft.fft(x_n)
FT_freq = np.fft.fftfreq(N, dt)
ax2 = fig.add_subplot(212)
ax2.bar(FT_freq, abs(X_k))
plt.show()

# b)
f_list = [800, 1400, 1800]      # Hz

# Generell funksjon som lager n antall plots
def make_FT_plots(f_list):
    n = len(f_list)
    fig, ax = plt.subplots(n, 2)
    c = plt.rcParams['axes.prop_cycle'].by_key()['color']
    c[0], c[1] = 'royalblue', 'r'
    for i, f in enumerate(f_list):
        x_n = g(t, f)
        X_k = np.fft.fft(x_n)
        FT_freq = np.fft.fftfreq(N, dt)
        line, = ax[i, 0].plot(t, x_n, color=c[i], linestyle='solid', marker='o')
        ax[i,0].set_xlabel('t [s]', weight='bold'); ax[i,0].set_ylabel('A [m]', weight='bold')
        ax[i,0].set_title(f'freq = {f}Hz', weight='bold')
        ax[i, 1].bar(FT_freq, abs(X_k), color=line.get_color())
        ax[i,1].set_xlabel('freq [Hz]', weight='bold'); ax[i,1].set_ylabel('X_k', weight='bold')
        ax[i,1].set_title(f'freq = {f}Hz', weight='bold')
    fig.tight_layout()

# Henter plots og viser
make_FT_plots(f_list)
plt.show()
