import numpy as np
import matplotlib.pyplot as plt


"""
Masse i høyre kolonne, utslag h i venstre kolonne
"""
data_array = np.loadtxt('maalinger_deformasjon.dat')
m_i = data_array[:,0]
h_i = data_array[:,1]
n = len(h_i)

E = np.sum(h_i*m_i) - 1/n*np.sum(m_i)*np.sum(h_i)
D = np.sum(m_i**2) - 1/n*np.sum(m_i)**2
slope = E / D

m_mean = 1/n*np.sum(m_i)
h_mean = 1/n*np.sum(h_i)
intercept = h_mean - slope*m_mean

# Regner ut usikkerhetene også
F = np.sum(h_i**2) - 1/n * np.sum(h_i)**2
dslope = np.sqrt(1 / (n-2) * (D*F - E**2) / D**2)
dintercept = np.sqrt(1 / (n-2) * (D / n + m_mean**2) * (D*F - E**2) / D**2)

h_fit = slope*m_i + intercept
print(slope, intercept, dslope, dintercept)

plt.plot(m_i, h_i, 'ro', label='data points')
plt.plot(m_i, h_fit, color='royalblue', label='fitted line')
plt.xlabel('masse [kg]', weight='bold')
plt.ylabel('utslag [mm]', weight='bold')
plt.show()

tau = [4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05]
tau_mean = 1 / len(tau) * np.sum(tau)
m = 2   # kg
k = 4*np.pi**2 * m / tau_mean**2
print(k)
std_tau = np.sqrt(1 / len(tau) * np.sum((tau - tau_mean)**2))
std_tau_mean = std_tau / np.sqrt(len(tau))
print(std_tau_mean)

# Denne er feil, vet ikke hvorfor
dm = 2 * std_tau / tau_mean
print(dm)
