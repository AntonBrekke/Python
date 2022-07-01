import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

frekvens_inn = np.array([1e2, 150, 200, 250, 300, 400, 1e3, 1e4, 1e5, 1e6])
frekvens_ut = np.array([1e2, 150, 200, 250, 300, 400, 1e3, 10.3e3, 12e3, 7e3])
A_ut = np.array([1.67, 1.425, 1.214, 1.046, 912e-3, 722e-3, 316.3e-3, 51.9e-3, 26e-3, 24.5e-3])
A_inn = np.array([1.971, 1.937, 1.935, 1.935, 1.921, 1.914, 1.896, 1.89, 1.896, 1.522])


VuPVi = A_ut / A_inn

fig = plt.figure()
ax1 = fig.add_subplot()

logy = np.log10(VuPVi[0:7])
logx1 = np.log10(frekvens_inn[0:7])

p1 = stats.linregress(logx1, logy)

logfit1 = np.poly1d(p1[:2])

ax1.plot(logx1, logy, color='r', marker='o', markerfacecolor='royalblue', markeredgecolor='royalblue', label='datapoints', zorder=3)
# plt.show()

t = np.linspace(logx1[0], logx1[-1], 300)
print(p1)
ax1.plot(t, logfit1(t), 'k', linestyle='dashed', label='fitted line')
plt.title('Logarithmic dataplot', weight='bold')
plt.xlabel('log(f [Hz])', weight='bold')
plt.ylabel('log(Vu/Vi [-])', weight='bold')
1

plt.legend()
fig.tight_layout()
plt.show()

R = 10e3
b = p1[1]
dR = 0.06e3
db = p1[-1]
C = 1 / (R*10**b)
dC = np.sqrt((dR / (R**2 * 10**b))**2 + (np.log(10)*db/(R*10**b))**2)
print(C, dC)
