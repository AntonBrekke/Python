import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

theta = [np.pi/6, np.pi/4, np.pi/3]
theta = {0: (np.pi/6, r'$\frac{\pi}{6}$'), 1:(np.pi/4, r'$\frac{\pi}{4}$'), 2:(np.pi/3, r'$\frac{\pi}{3}$')}

t = np.linspace(0, 1, 101)
x = t

for key in theta:
    y = t*np.tan(theta[key][0])*(1-t)
    plt.plot(x,y, label=r'$\theta$=' + f'{theta[key][1]}')
plt.xlabel(r'$x^*\;[-]$'); plt.ylabel(r'$y^*\;[-]$')
plt.legend(loc='lower center')
# plt.savefig('oppgave_1_c.png')
# plt.show()
plt.clf()

# Digresjon
"""
Her skalerer jeg med y_m = y(t_m) når t_m er tiden ballen er i topp-punktet av kastbanen.
Resultatet er et plot der jeg ser hvor langt ballen er kommert i x-retning når ballen har
nådd topp-punktet.
Plottet viser at ballen har kommet lengre i x-retning innen topp-punktet for skarpere vinkler
theta.
"""
t = np.linspace(0, 1, 101)
y = t

for key in theta:
    x = 2*np.cos(theta[key][0])*t / (np.sin(theta[key][0]))
    plt.plot(x,y, label=r'$\theta$=' + f'{theta[key][1]}')
plt.xlabel(r'$x^*\;[-]$'); plt.ylabel(r'$y^*\;[-]$')
plt.legend(loc='lower center')
plt.show()
plt.clf()

"""
Her skalerer jeg med x_m = x(t_m) når t_m er tiden ballen er i topp-punktet av kastbanen.
Resultatet er et plot der jeg ser hvor langt ballen er kommert i y-retning når ballen har
nådd lengden i x-retning når ballen er i topp-punktet.
PLottet viser at ballen har høyere topp-punkt for store vinkler theta.
"""
t = np.linspace(0, 1, 101)
x = t

for key in theta:
    y = 0.5*np.tan(theta[key][0])*t
    plt.plot(x,y, label=r'$\theta$=' + f'{theta[key][1]}')
plt.xlabel(r'$x^*\;[-]$'); plt.ylabel(r'$y^*\;[-]$')
plt.legend(loc='lower center')
plt.show()
