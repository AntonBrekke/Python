import numpy as np
import matplotlib.pyplot as plt

# Lager dekorator-funksjoen
def decor(func):
    def wrapper(*args, **kwargs):   # Lager wrapper funksjon
        print('Bruker decorator:')
        val = func(*args, **kwargs)
        return val

    return wrapper

"""
For å bruke dekoratoren skriver jeg
@decor over funksjonen jeg skal dekorere.
@decor er det samme som å skrive
f = decor(f)
Hvorfor bruke dekorator? Om du skal
alternere flere funksjoner med samme
egenskap sparer det deg kode kontra copy-paste
"""

def f(x):
    return 2*x
print(f(2))

@decor
def f(x):
    return x**2
print(f(2))

# Kan også bruke det med numpy
x = np.linspace(0, 1, 800)
plt.plot(x, f(x), 'r')
plt.show()

# Eksempel på ofte brukt dekorator: timer

import time
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{func.__name__} ran in {t2} seconds')
        return result

    return wrapper

@timer
def f(x):
    time.sleep(2)
    return x**2

x = np.linspace(0, 1, 800)
plt.plot(x, f(x), 'r')
plt.show()
