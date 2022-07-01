import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from playsound import playsound
from numba import njit

def pluck_guitar(freq, T0):
    # Konstanter og variabler
    Nx = 100
    Nt = 1e6
    L = 0.65
    dx = L / Nx
    dt = 5e-6
    f = freq         # Hz
    v = 2*L*f       # v = 1 / (2*L) * np.sqrt(T / mu)
    x = np.linspace(0, L, Nx)
    h = 1e-2           # m
    x0 = 0.15    # x0 er der man plukker gitaren fra pickupen, m

    # Hvor man plukker gitarstrengen, initialbetingelse
    pluck_index = int(x0 / dx)
    y1 = np.linspace(0, h, pluck_index)
    y2 = np.linspace(h, 0, Nx - pluck_index)
    y0 = np.concatenate((y1, y2))

    f = np.zeros((int(Nt), Nx))    # Funksjonen vår f
    t0 = T0             # s, der vi starter å løse likningen (ønsker 0.5s så lyden ikke spiller med én gang)
    t0_index = int(t0 / dt)   # Finner indeksen for t0
    f[0:t0_index+1] = y0     # Setter initialbetingelse

    @njit
    def solve_waveeq(f_array, times, length, dt, dx):
        for i in range(t0_index, times-1):
            for j in range(2, length-2):
                outer_factor = (v*dt)**2
                p1 = 1 / dx**2 * (f_array[i, j+1] - 2*f_array[i, j] + f_array[i, j-1])
                p2 = 1 / (v**2 * dt**2) * (2*f_array[i, j] - f_array[i-1, j])
                f_array[i+1, j] = outer_factor * (p1 + p2)
        return f_array

    sol = solve_waveeq(f, Nt, Nx, dt, dx)

    #   Finner koeffisientene A_n(t) som er i signalene
    def inner_prod(m):
        sin_arr = np.sin(m*np.pi*x/L)
        return np.array([np.sum(sin_arr*s, axis=0) for s in sol])       # Egentlig et integral, så må ha med dx. Men da blir lyden lav, og tenker at amplituden er prop. med integralet og ignorerer dx.

    M = 10
    harmonics = np.array([inner_prod(m) for m in range(1, M+1)])

    tot = np.sum(harmonics, axis=0)
    return tot

def pluck_strings(note_list, timer_list=None, dt=5e-6):
    # if timer_list is None: timer_list = np.zeros_like(note_list)
    s = 0
    for n, t in zip(note_list, timer_list):
        s += pluck_guitar(n, t)
    print(s)

    wavfile.write('temp_guitar.wav', int(1/dt), s.astype(np.float32))
    # playsound('temp_guitar.wav')

note_list = [440, 130]
pluck_strings(note_list, np.zeros(2))
