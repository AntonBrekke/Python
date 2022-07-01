import numpy as np
import matplotlib.pyplot as plt


"""
Masse i høyre kolonne, utslag h i venstre kolonne
"""
# data_array = np.loadtxt('maalinger_deformasjon.dat')
baseline = 881          # 1e-2 mm
m_i = np.array([0, 100, 500, 600, 1000, 1500, 1600, 2000, 2100, 2500])     # g
h_i = 881 - np.array([881, 853, 735, 705, 590, 457, 432, 329, 300, 195])     # 1e-2 mm
n = len(h_i)

E = np.sum(h_i*m_i) - 1/n*np.sum(m_i)*np.sum(h_i)
D = np.sum(m_i**2) - 1/n*np.sum(m_i)**2
slope = E / D       # Stigning i tilpasning

m_mean = 1/n*np.sum(m_i)
h_mean = 1/n*np.sum(h_i)
intercept = h_mean - slope*m_mean       # Skjæringspunkt i tilpasning

# Regner ut usikkerhetene også
F = np.sum(h_i**2) - 1/n * np.sum(h_i)**2
dslope = np.sqrt(1 / (n-2) * (D*F - E**2) / D**2)
dintercept = np.sqrt(1 / (n-2) * (D / n + m_mean**2) * (D*F - E**2) / D**2)

h_fit = slope*m_i + intercept
print(f'a = {slope}1e-2mm / g, b = {intercept}1e-2mm\nda = {dslope}1e-2mm / g, db = {dintercept}1e-2mm')

plt.plot(m_i, h_i, 'ro', label='data points')
plt.plot(m_i, h_fit, color='royalblue', label='fitted line')
plt.xlabel('masse [g]', weight='bold')
plt.ylabel('utslag [1e-2mm]', weight='bold')
plt.show()

dl = 0.002      # mm
a = slope * 1e-2        # mm / g
b = intercept * 1e-2        # mm
l = 602e-2          # mm
da = dslope * 1e-2  # mm / g
db = dintercept * 1e-2      # mm

dm = np.sqrt((dl / a)**2 + (da*(l-b) / a**2)**2 + (db / a)**2)      # g
print(f'dm = {dm}')

dm_kg = dm*1e-3         # kg
dtau = 0.012            # s
m = 2.20352     # kg

tau_mean = 0.4286       # s
dk = np.sqrt((4*np.pi**2*dm_kg / tau_mean**2)**2 + (8*np.pi**2*m*dtau / tau_mean**3)**2)
print(f'dk = {dk}')

k = 468.7
dm = np.sqrt((tau_mean**2*dk/(4*np.pi**2))**2 + (2*tau_mean*k/(4*np.pi**2)*dtau)**2)
print(dm)

# # tau = [4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05]
# tau_mean = 1 / len(tau) * np.sum(tau)
# m = 2   # kg
# k = 4*np.pi**2 * m / tau_mean**2
# print(k)
# std_tau = np.sqrt(1 / len(tau) * np.sum((tau - tau_mean)**2))
# std_tau_mean = std_tau / np.sqrt(len(tau))
# print(std_tau_mean)

# Denne er feil, vet ikke hvorfor
# dm = 2 * std_tau / tau_mean
# print(dm)
