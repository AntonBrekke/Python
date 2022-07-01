import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd

k_data = np.array([2, 7, 5, 5, 6, 3, 3, 4, 0, 10, 4, 8, 5, 2, 2, 2, 2, 3, 3, 4, 10,
     3, 5, 8, 3, 5, 7, 1, 6, 4, 6, 7, 3, 9, 5, 6, 4, 4, 4, 5, 6,
     1, 3, 4, 4, 4, 8, 4, 2, 5, 3, 4, 8, 4, 5, 8, 2, 3, 1, 0, 3,
     6, 4, 5, 5, 7, 3, 3, 6, 1, 7, 4, 4, 2, 5, 3, 2, 3, 0, 0, 5,
     2, 3, 5, 3, 4, 3, 2, 5, 4, 2, 5, 7, 4, 5, 4, 6, 3, 3, 6, 5])

m = np.mean(k_data)
std = np.sqrt(1 / (len(k_data)) * np.sum((k_data - m)**2))
std_from_m = np.sqrt(m)

print(f'm: {m}, std: {std}, std_m: {std_from_m}')
print(np.std(k_data))

# fig = plt.figure(facecolor='k')
# ax = fig.add_subplot(facecolor='k')
fig = plt.figure()
ax = fig.add_subplot()
hist, bins, patches = plt.hist(k_data, bins=range(np.min(k_data), np.max(k_data)+2), ec='black', label='Data', align='left')

"""
ax.set_xlabel('k')
ax.set_ylabel('Antall målinger')
ax.spines['bottom'].set_color('w')      # Setter aksen hvit
ax.spines['left'].set_color('w')
ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
ax.tick_params(axis='y', colors='w')

get_cmap = plt.get_cmap('jet')
cmap = np.array(get_cmap(hist / np.max(hist)))

for color, p in zip(cmap, patches):
    plt.setp(p, 'facecolor', color)
"""

N = len(k_data)
M = len(bins)
print(M)
def Poisson():
    y_k = np.zeros(M-1)
    y_k[0] = N*np.exp(-m)
    for i in range(1, M-1):
        y_k[i] = m/i * y_k[i-1]
    return y_k


ax.plot([*range(0, M-1)], Poisson(), 'r', linewidth=3, label='P(k)')
ax.set_xlabel('k', fontsize=16, weight='bold')
ax.set_ylabel('Antall målinger', fontsize=16, weight='bold')
ax.set_xticks([*range(0, M-1)])
# ax.set_xticklabels(range(0, M))

plt.legend(prop={'size': 16})
plt.show()

lab = vd.gammastraling()
lab.GeigerMuller(nr=138/60, nb=31/60, A=149e3, r=28/10/2, d=16)

nb = 175 / 600
n = np.array([1000/31, 1000/46, 1000/75, 1000/126, 1000/246, 1000/360, 1000/595]) - nb
z = np.array([0, 0.3, 0.8, 1.3, 1.8, 2.3, 2.8]) * 1e-2      # m

lab.n_and_z_expreg(n=n, z=z, color='r', xlabel='z [m]', ylabel='n [Bq]')
lab.find_z_from_absorbed(mu=lab.mu, perc_absorbed=99)

CS137 = np.loadtxt('CS137.asc')[:,1]
CO60 = np.loadtxt('CO60.asc')[:,1]

lab.plot_spectrum(CS137, dE=1, start_stop_top=[290, 370], label=r'Spectrum ${}^{137}$Cs', show=True, spec_legend=True)

lab.plot_spectrum(CO60, dE=1, start_stop_top=[540, 620], label='Spectrum ${}^{60}$Co', show=False, spec_legend=True)
lab.plot_spectrum(CO60, dE=1, start_stop_top=[620, 695], show=True)

# Finner I = 335 for CS137 og I=581 og I=659 for CO60.
# Bruker siste I for CO60 til kalibrering, I=659
# Får oppgitt at E = 662keV for CS137 og E = 1333keV for CO60


lab.estimate_dispersion(E1=662, E2=1333, I1=335, I2=659)

E = lab.dE * 581 + lab.E0
print(f'E: {E}\n')

klokke_spectrum = np.loadtxt('klokke.asc')[:,1]
lab.plot_spectrum(klokke_spectrum, dE=1, start_stop_top=[65, 100], label='Spectrum clock', show=False, spec_legend=True)
E1 = lab.dE * lab.I_top + lab.E0

lab.plot_spectrum(klokke_spectrum, dE=1, start_stop_top=[107, 121], show=False)
E2 = lab.dE * lab.I_top + lab.E0

lab.plot_spectrum(klokke_spectrum, dE=1, start_stop_top=[121, 160], show=False)
E3 = lab.dE * lab.I_top + lab.E0

lab.plot_spectrum(klokke_spectrum, dE=1, start_stop_top=[160, 195], show=False)
E4 = lab.dE * lab.I_top + lab.E0

lab.plot_spectrum(klokke_spectrum, dE=1, start_stop_top=[270, 335], show=True)
E5 = lab.dE * lab.I_top + lab.E0

print(f'Energy tops:\nE1: {E1}\nE2: {E2}\nE3: {E3}\nE4: {E4}\nE5: {E5}')
