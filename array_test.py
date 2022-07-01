

# Sender elementer i en array gjennom en funksjon og fyller en ny array med dissee verdiene
import numpy as np
def f(x):
    return x
"""
n = 20       # Number of points
x = np.linspace(0, 1, n)    #n ponts in [0,1]
y = np.zeros(n)     # n zeros (float data type)
for i in range(n):
    y[i] = f(x[i])
print(y)
"""

A = np.linspace(0, 10, 11)
B = np.linspace(0, 5, 11)
print(A-B)
print(A*B)
# Konklusjon: kan gjøre regneoperasjoner med arrays

A = [*range(0, 11, 1)]
B = [*range(2, 13, 1)]
print(A, B)
print(B-A)
print(B*A)
# Konklusjon: kan ikke gjøre regneoperasjoner med lister
