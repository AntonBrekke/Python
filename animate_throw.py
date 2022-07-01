import numpy as np
import matplotlib.pyplot as plt

# Funksjon for kastlengde i retning x:
def x(t, v0, theta):
    sx = v0*np.cos(theta)*t
    return sx
# Funksjon for kastlengde i retning y:
def y(t, v0, theta):
    sy = v0*np.sin(theta)*t - 0.5*g*t**2
    return sy

g = 9.81
v0 = 2.0
theta = np.linspace(1e-10, np.pi/2, 150)    # Vinkler og parteringsintervall
tmax = 2*v0/g       # Lengste tid for et kast, for å få kontinuitet i hele grafen
x_tmax = 2*v0*np.sin(theta)/g  # Når y = 0, tid for lengste kastposisjon som forekommer i x
y_tmax = v0*np.sin(theta)/g     # Når v_y = 0, tid for høyeste kastposisjon som forekommer i y
t = np.linspace(0, tmax, 1000)   # Tidsrommet som plottes, også nøyaktighet på grafen.

xmax = np.max(x(x_tmax, v0, theta)) # Største verdi som forekommer av x
ymax = np.max(y(y_tmax, v0, theta)) # Største verdi som forekommer av y

# Animerer data med simpel modell:
for theta in theta:
    plt.plot(x(t, v0, theta), y(t, v0, theta), label=f'x = {v0*np.cos(theta)*(2*v0*np.sin(theta)/g)}\ny = {v0*np.sin(theta)*(v0*np.sin(theta)/g) - 0.5*g*(v0*np.sin(theta)/g)**2}')

    plt.title(f'$v_0$ = {v0}')
    """
    Avstanden x = v0*cos(theta)*t og y = v0*np.sin(theta)*t - 0.5*g*t**2, der t i slutten av kastet (x_tmax = 2*v0*sin(theta)*g, y_tmax = v0*np.sin(theta)/g)
    """
    plt.xlabel(f'theta = $\pi/${np.pi/theta}')
    plt.axis([0, xmax, 0, ymax])
    plt.legend()
    plt.draw()
    plt.pause(0.01)
    plt.clf()
