import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import cos, sin, factorial, exp, pi, sqrt, ln
# Advarsel: Ikke pen kode

# Eksempel: Sadel: x**2 - x*y - y**2
# Eksempel: Crazy: cos(x**2 + y**2)
# Eksempel: Ripples: cos(x**2 + y**2) / (x**2 + y**2 + 1)
# Eksempel: Wonky chip: cos(2*x) + sin(2*y) + 0.3*(x**2 - y**2)
# Eksempel: Øygruppe ute i havet (bruk cmap 'terrain') (Sett A = 5.5):
# 5 / (1 + x**2 + y**2)**2 + 3 / (1 + (x - 1.5)**2 + (y - 1.5)**2) + 4 / (1 + (x - 2.5)**2 + (y - 2.5)**2) + 4 / (1 + (x - 2.5)**2 + (y + 2.5)**2) + 0.5*cos(2*x)*sin(x+y)

# MERK: Store funksjonsverdier gjør at pilhodene blir små, så i stedet for x**2 - y**2, prøv å skaler ned litt, f.eks 0.1*(x**2 - y**2)

A = 6
B = A
func = input('Input scalar field: ')
x, y = sp.symbols('x y')
f = eval(func)

# Lager figur
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Skalarfunksjon
# Lager domene for skalarfunksjonen
I_scalar = np.linspace(-A, B, 800)
J_scalar = np.linspace(-A, B, 800)
x_scalar, y_scalar = np.meshgrid(I_scalar, J_scalar, indexing='ij')

# Lager skalarfunksjon og bytter ut så den kan evaluere i Python
f_scalar = eval(func.replace('cos', 'np.cos').replace('sin', 'np.sin').replace('ln', 'np.log')
                .replace('sqrt', 'np.sqrt').replace('pi', 'np.pi')
                .replace('exp', '~').replace('x', 'x_scalar')
                .replace('y', 'y_scalar').replace('~', 'np.exp'))   # Bytter exp med dummy-string så x'en i exp ikke byttes, og bytter til np.exp senere

if isinstance(f_scalar, (int, float)):
    f_scalar = f_scalar*np.ones_like(x_scalar)
# Plotter skalarfunksjon
cc = input('Input colormap (enter for standard):')
if cc == '':
    ax.plot_surface(x_scalar, y_scalar, f_scalar, cmap='jet')
else:
    cc = cc.strip(' ')
    ax.plot_surface(x_scalar, y_scalar, f_scalar, cmap=cc)

# Quiver-plott
# Deriverer skalarfunksjonen f for gradienten med sympy
if isinstance(f, (float, int)):
    dfdx = lambda x, y: 0       # Pakker tallet inn som en funksjon så funksjonskall alltid funker
    dfdy = lambda x, y: 0
else:
    dfdx = f.diff(x, 1)
    dfdx = sp.lambdify([x,y], dfdx)
    dfdy = f.diff(y, 1)
    dfdy = sp.lambdify([x,y], dfdy)

# Lager grid for gradienten
I = np.linspace(-A, B, 20)
J = np.linspace(-A, B, 20)
K = np.linspace(np.min(f_scalar) - A, np.max(f_scalar) + 1, 1)  # Hva som er max er ikke så viktig, men np.min() og step 1 legger gradientfeltet på gulvet av domenet

x, y, z = np.meshgrid(I, J, K, indexing='ij')

# Tester om de deriverte ble skalarer og gjør om til arrays
if isinstance(dfdx(x,y), (int, float)):
    alpha = dfdx(x,y)*np.ones_like(x)
    dfdx = lambda x, y: alpha   # Pakker arrayen inn som en funksjon så funksjonskall alltid funker

if isinstance(dfdy(x,y), (int, float)):
    beta = dfdy(x,y)*np.ones_like(y)
    dfdy = lambda x, y: beta

# Definerer gradientvektorene i gridet
u = dfdx(x,y)
v = dfdy(x,y)
w = np.zeros_like(z)

# Plotter piler i 3D-grid med skalerte størrelser for pil og hode
ax.quiver(x[::2, ::2], y[::2, ::2], z[::2, ::2], u[::2, ::2], v[::2, ::2], w[::2, ::2], normalize=True, arrow_length_ratio=0.5, color='k')

ax.set_title(func)

plt.show()
