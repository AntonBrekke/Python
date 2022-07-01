# Forelesning 20.01.2021
# Anton Brekke
# antonabr@uio.no

import numpy as np
import matplotlib.pyplot as plt

# Plot av konturene i et skalarfelt:
N = 40
I = np.linspace(-1, 1, N)
x, y = np.meshgrid(I, I, indexing='ij') # Lager meshgrid  med array (40, 40) for x og y i [-1, 1]
z = (0.1, 0.4, 0.8, 1.3) # Velger hvilke kontur som skal med, uten å definere velger plt egen
CS = plt.contour(x, y, x**2 + y**2, z)  # Plotter kontur
plt.clabel(CS, inline=1, fontsize=10, fmt=f'%1.2f',colors='k')  # Får frem T0 på alle konturlinjene
# plt.show()
plt.clf()       # Fjerner tidligere plots
# Kan plotte fylte konturer
plt.contourf(x, y, x**2 + y**2, 100)     # Siste tallet beskriver kvaliteten. Lavt tall = dårlig kvalitet. Høyt tall = bra kvalitet.
# plt.show()
plt.clf()



# Plotting av vektorfelt:
plt.quiver(x, y, x**2, y**2)        # Funksjon for å plotte 2D-felt av piler. Piler blir ofte tette, så se neste plot for å ordne det
# plt.show()
plt.clf()

plt.quiver(x[::2, ::2], y[::2, ::2], x[::2, ::2]**2, y[::2, ::2]**2)    # Notasjonen [::, ::N] gjør at vi kan plotte hver N-te pil. N=2 plotter annenhver pil
# plt.show()
plt.clf()

# Annet eksempel på vektorfelt
plt.quiver(x[::2, ::2], y[::2, ::2], -y[::2, ::2], x[::2, ::2])     # f(x,y) = (-y, x) eller u = -y*i + x*j
# plt.show()
plt.clf()


# NYTT: Plotly
import plotly.graph_objects as go

fig = go.Figure(data=go.Contour(x=I, y=I, z=x**2 + y**2))
# fig.show()

import plotly.figure_factory as ff
ff.create_quiver(x, y, x**2, y**2)
fig.update_layout(width=500, height=500)
# fig.show()
