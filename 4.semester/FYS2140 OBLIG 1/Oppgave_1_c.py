import numpy as np
import matplotlib.pyplot as plt

# Plotter potensiell energi i en fjær
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

x = np.linspace(-1, 5, 300)
Ep = 0.5*x**2

ax1.plot(x, Ep, label=r'$E_p$')
ax1.set_title('Potential energy in a spring', weight='bold')
ax1.set_xlabel('x [m]', weight='bold'); ax1.set_ylabel(r'$E_p$[J]', weight='bold')
ax1.legend()

# Energi elektron i et hydrogenatom

ax2.set_title('Energy of electon in hydrogen atom', weight='bold')
n = np.linspace(2, 20, 19)
E = -13.6 / n**2
get_cmap = plt.get_cmap('jet')
cmap = np.array(get_cmap(n / np.max(n))) # Må normaliseres et)
ax2.bar(n, E, color=cmap[::-1])
ax2.invert_yaxis()
ax2.set_xlabel('n [-]', weight='bold'); ax2.set_ylabel('E [eV]', weight='bold')
plt.show()
