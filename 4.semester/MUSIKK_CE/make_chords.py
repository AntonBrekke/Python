import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from matplotlib.animation import FuncAnimation
from scipy.io import wavfile
from IPython.display import Audio
from playsound import playsound
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time

dt = 5e-6
L = 0.65
Nx = 100
l = 2e-6        # m^2
gamma = 8e-5
h = 1e-2           # m
dx = L / Nx

def make_sound(freq=130.81, len_sim=5, time_wait=0):
    # Konstanter og variabler
    Nt = len_sim / dt
    f = freq         # C3
    # f = 146.83         # D3
    v = 2*L*f       # v = 1 / (2*L) * np.sqrt(T / mu)
    x = np.linspace(0, L, Nx)
    print(f'Simulating for {Nt * dt} seconds')
    print(f'Courant-betingelsen: dt < {dx / v}')

    # Hvor man plukker gitarstrengen, initialbetingelse
    x0 = 0.15
    pluck_index = int(x0 / dx)
    y1 = np.linspace(0, h, pluck_index)
    y2 = np.linspace(h, 0, Nx - pluck_index)
    y0 = np.concatenate((y1, y2))

    sol = np.zeros((int(Nt), Nx))
    t0 = time_wait
    t0_index = int(t0 / dt)
    sol[0:t0_index+1] = y0

    # Regner ut (diskretisert bølgelikning med demping og alt)
    @njit
    def compute_d(d, times, length, dt, dx, l, gamma):
        for i in range(t0_index, times-1):
            for j in range(2, length-2):
                outer_factor = (1/(v**2 * dt**2) + gamma/(2*dt))**(-1)
                p1 = 1 / dx**2 * (d[i, j+1] - 2*d[i, j] + d[i, j-1])
                p2 = 1 / (v**2 * dt**2) * (2*d[i, j] - d[i-1, j])
                p3 = gamma / (2*dt) * d[i-1, j]
                p4 = -l**2 / dx**4 * (d[i, j+2] - 4*d[i, j+1] + 6*d[i, j] - 4*d[i, j-1] + d[i, j-2])
                d[i+1, j] = outer_factor * (p1 + p2 + p3 + p4)
        return d

    sol = compute_d(sol, Nt, Nx, dt, dx, l, gamma)

    # Finner koeffisientene A_n som er i signalene
    def get_integral(m):
        sin_arr = np.sin(m*np.pi*x/L)
        return np.array([np.sum(sin_arr*s, axis=0) for s in sol])       # Egentlig et integral, så må ha med dx. Men da blir lyden lav, og tenker at amplituden er prop. med integralet og ignorerer dx.

    harmonics = [get_integral(m) for m in range(10)]

    sound = np.sum(harmonics, axis=0)
    return sound

def write_sound(list_names, list_notes, list_times):
    list_sounds = []
    for name, note, time_len in zip(list_names, list_notes, list_times):
        sound = make_sound(note, time_len)
        wavfile.write(f'{name}.wav', int(1/dt), sound.astype(np.float32))

def play_sounds(soundfile_list=[], timers=[]):
    for s, t in zip(soundfile_list, timers):
        playsound(f'{s}.wav')
        time.sleep(t)

def raise_note(note, frets):
    return note * 2**(frets / 12)

# Definerer grunnnoter strenger gitar
E2 = 82.41
A2 = raise_note(E2, 5)
D3 = raise_note(A2, 5)
G3 = raise_note(D3, 5)
B3 = raise_note(G3, 4)
E4 = raise_note(B3, 5)

C3 = raise_note(A2, 3)
E3 = raise_note(D3, 2)
C4 = raise_note(B3, 1)
notes = [E2, G3, B3, E4]
notes_name = ['E2', 'G3', 'B3', 'E4']
play_list = ['E2', 'G3', 'B3', 'E4', 'B3', 'G3']
# write_sound(notes_name, notes, [0.5, 0.3, 0.3, 0.3])
timers = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
for i in range(3):
    play_sounds(play_list, timers)
