import numpy as np

def h(n=1):
    x = np.zeros(n+1, int) # Int er datatypen
    x[0] = 1
    x[1] = 1
    for i in range(2, n+1):
        x[i] = -x[i-1] + 2*x[i-2]
    return n, x[n]      # Returnerer tuppel

print(h(n=3))
