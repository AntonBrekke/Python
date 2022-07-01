from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

# Funker dårlig i terminal, funker bedre i Jupyter
"""
g = 9.81
v0 = 100
a = np.pi/4
T = 2*v0*np.sin(a)/g
N = 100  # Antall intervlall
t0 = np.linspace(0, T*1.1, N+1)

# Beregner hele partikkelbane først
x0 = v0*np.cos(a)*t0
z0 = v0*np.sin(a)*t0 - 0.5*g*t0**2

def partikkelbane(t):
    # plot hele partikkelbanen
    plt.figure()
    plt.plot(x0, z0, 'b')

    # plot partikkelen
    x = v0*np.cos(a)*t
    z = v0*np.sin(a)*t - 0.5*g*t**2
    plt.plot(x, z, 'ok')

    # plot en hastighetsvektor
    plt.arrow(0, 0, v0*np.cos(a)*T/4, v0*np.sin(a)*T/4, hea_width=v0*T/100)
    plt.arrow(x, z, v0*np.cos(a)*T/4, (v0*np.sin(a)-g*t)*T/4, head_width=v0*T/100)

    # posisjonsvektor
    plt.arrow(0, 0, x, z, length_includes_head=True)

    plt.ylim(z0.min(), 2*z0.max())

    plt.text(0.25*v0*np.cos(a), 0.3*v0*np.sin(a), r'$\vec{v}(0)$')
    plt.text(x+0.25*v0*np.cos(a), z+0.2*(v0*np.sin(a)-g*t), r'$\vec{v}(t)$')
    plt.text(0.5*x, 0.4*z, r'$\vec{r}(t)$')

    plt.show()


interact(partikkelbane, t=(0, T, T/20))

raise RuntimeError
"""
