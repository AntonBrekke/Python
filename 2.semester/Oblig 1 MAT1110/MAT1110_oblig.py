import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 3

def x(t):   # x-komponent i r
    return a*np.arcsinh(t/a)

def y(t):   # y-komponent i r
    return np.sqrt(t**2 + a**2)

t = np.linspace(-b, b, 600) # Intervall fra -b, b

plt.plot(x(t), y(t), 'r',label='r(t)')
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.title('Kjedelinje', fontweight='bold')
# plt.savefig('kjedelinje.png')
plt.show()
