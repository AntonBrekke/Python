import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.loadtxt('terminal_hastighet_rdata.dat')

r = data[:,0]   # Ulike radiuser på kule
# 3 ulike teorier: Stokes, Rayleigh, og en annen (vi vet ikke hvem enda)
# dataen er terminalhastigheter for de ulike radiene
"""
Litt teori:
d = 2r
Stokes - v_T ~ d**2 = 4r**2
log(v_T) = 2 * log(r) + A

Rayleigh - v_T ~ d**0.5 = sqrt(2) * r**0.5
log(v_T) = 0.5*log(r) + B

Forventer log med stigning 2 på Stokes og 0.5 på Rayleigh
"""
theory_1 = data[:,1]
theory_2 = data[:,2]
theory_3 = data[:,3]

logr = np.log(r)
log1 = np.log(theory_1)
log2 = np.log(theory_2)
log3 = np.log(theory_3)

line1 = stats.linregress(logr, log1)
line2 = stats.linregress(logr, log2)
line3 = stats.linregress(logr, log3)

fig, (ax1, ax2, ax3) = plt.subplots(3,1)

ax1.plot(logr, log1, 'r', label=f'Theory_1 : {line1[:2]}')
ax2.plot(logr, log2, 'royalblue', label=f'Theory_2 : {line2[:2]}')
ax3.plot(logr, log3, 'tab:orange', label=f'Theory_3 : {line3[:2]}')

print(f'line1 : {line1}')
print(f'line2 : {line2}')
print(f'line3 : {line3}')

ax1.legend()
ax2.legend()
ax3.legend()
fig.tight_layout()
plt.show()

"""
Konklusjon:
Theory_1 = Stokes : stigning 2
Theory_2 = Rayleigh : stigning 0.5
Theory_3 = Annen : stigning 1

(i prelab :
Stokes - 2 kolonne
Rayleigh - 3 kolonne
Annen - 4 kolonne)
"""
