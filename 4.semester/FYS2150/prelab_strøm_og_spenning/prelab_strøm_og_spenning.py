import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
V_u / V_i på venstre side, frekvens på høyre side
"""

data = np.loadtxt('RC_data.csv')

logx = np.log10(data[:,1])
logy = np.log10(data[:,0])

plt.plot(logx, logy, 'r')

p = np.polyfit(logx[9:], logy[9:], 1)       # Enten eller polyfit eller linregress, merk vi må ha a[:2]
a = stats.linregress(logx[9:], logy[9:])
logfit = np.poly1d(p)
t = np.linspace(0, logx[-1])
plt.plot(t, logfit(t))
print(p)
plt.show()

# Ser på skjæringspunkt i grafen og finner at log(omega0) er skjæringspunktet, p[1]
omega0 = 10**p[1]
print(omega0)
