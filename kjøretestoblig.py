# listing 1
list = [1, 1]
for i in range(2,100+1):
    x_n2 = list[i-2]
    x_n1 = 4*list[i-1]
    x_n = x_n1 + x_n2
    list.append(x_n)
    print(f'{i}\t|{x_n:6g}')

# listing 2
import numpy as np
list2 = [1, 2 - np.sqrt(5)]
for i in range(2,100+1):
    x_n2 = list2[i-2]
    x_n1 = 4*list2[i-1]
    x_n = x_n1 + x_n2
    list2.append(x_n)
    print(f'{i}\t|{x_n:6g}')

# Listing 3
from sympy import symbols, solve
import numpy as np

epsilon = symbols('epsilon')
# For n = 100:
expr = (epsilon/(2*np.sqrt(5)))*(2 + np.sqrt(5))**100 + ((2*np.sqrt(5) - epsilon)
        /(2*np.sqrt(5)))*(2 - np.sqrt(5))**100 + 1.20719e+46
sol = solve(expr)

# Listing 4
def prod1(i, n):
    p = 1
    for j in range(1, i + 1):
        p *= (n - j + 1)/j
    return p
print(prod1(4, 5000))
print(prod1(500, 1000))
print(prod1(99940, 100000))

#Listing 5
def prod1(i, n):
    p = 1
    for j in range(1, n - i + 1):
        p *= (i + j)/j
    return p
print(prod1(99940, 100000))

# Listings 6
from random import random
antfeil = 0; N = 100000

for i in range(N):
    x = random(); y = random(); z = random()
    res1 = (x + y) * (y + z)
    res2 = x*y + y*y + x*z + y*z
    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y; z0 = z
        ikkelik1 = res1
        ikkelik2 = res2

print (100. * antfeil/N)
print (x0, y0, z0, ikkelik1 - ikkelik2)
