# Exercise A1 Langtangens bok

# a)
"""
import numpy as np

def an(N):
    res = np.zeros(N+1)
    for n in range(N+1):
        res[n] = (7+1/(n+1)) / (3-1/(n+1)**2)
    return res

a = an(100)
for n in range(len(a)):
    print(f"a_{n} = {a[n]:7.5f}")
"""

#b)
"""
import numpy as np

def Dn(N):
    res = np.zeros(N+1)
    for n in range(N+1):
        h = 2**(-n)
        res[n] = np.sin(h) / h
    return res

D = Dn(20)
for n in range(len(D)):
    print(f"D_{n} = {D[n]:7.5f}")

import matplotlib.pyplot as plt
plt.plot(range(len(D)), D, "ro")
plt.show()
"""
#c)
import numpy as np

def D(f, x, N):
    Dvec = np.zeros(N+1)
    for n in range(N+1):
        h = 2**(-n)
        Dvec[n] = (f(x+h) - f(x))/h
    return Dvec

# Let f(x)=sin(x), x=0, N=80

f = np.sin
x = 0
N = 80
D = D(f, x, N)

import matplotlib.pyplot as plt
plt.plot(range(0, N+1), D, "m")
plt.show()
