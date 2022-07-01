# Exercise 6.13
import numpy as np
import matplotlib.pyplot as plt

N = 4           # Setter N = 4 som gitt i oppgaven
x = np.linspace(-np.pi, np.pi, 100)         # Lager en array med verdier fra -pi til pi i 100 like store intervaller

# Definerer opprinnelig funksjon
def f(x):
    return abs(x)

# Definerer approksimasjonen til abs(x) gitt i oppgave
def abs_approx(x, N):
    s = 0
    for n in range(1, N+1):
        s += np.cos((2*n-1)*x) / (2*n-1)**2
    f = (np.pi/2) - (4/np.pi)*s
    return f

y0 = f(x)       # Alle y0 er gitt som f(x) med alle x-verdier i array

plt.plot(x, y0, 'k', label='f (x)=|x|', linewidth=4)    # Plotter funksjoner i matplotlib
# Looper gjennom og plotter for N=1, N=2 etc.
for N in range(1,N+1):
    y1 = abs_approx(x, N) # Alle y1 er gitt som abs_approx(x, N) med alle x-verdier i array
    plt.plot(x, y1, label='abs_approx(x)')

plt.axis([x[0], x[-1], 0, 5])       # Definerer akse fra -pi til pi i x og 0 til 5 i y
plt.title("Comparison f(x), abs_approx(x)")
plt.xlabel("$x\in[-\pi, \pi]$")
plt.ylabel("y")
plt.legend()
plt.show()

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 40 IN2900> python approx_abs.py
PS C:Desktop\Python\Oblig uke 40 IN2900>
"""
