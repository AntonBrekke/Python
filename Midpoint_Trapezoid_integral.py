import numpy as np

a = 0
b = 1
N = 1
h = (b-a)/N
# f = lambda x: funksjonsuttrykk

# def f(x):
#     if x == 0:
#         return 1
#     if x != 0:
#         return (x-x**3/6)/x        # Erstatter sin(x) med Taylorpolynom av grad 3 om a = 0

def f(x):
    if x == 0:
        return 1
    if x != 0:
        return np.sin(x)/x

# Midtpunktmetoden for integraler implementert i Python
x = [0]*(N+1)
integral = 0
for n in range(1, N+1):
    x[n] = n*h
    m = (x[n]+x[n-1]) / 2
    integral += f(m)*h

print(integral)


# Trapesmetoden for integraler implementert i Python
integral = 0
for n in range(1, N+1):
    integral += 0.5 * h * (f(h*n) + f(h*(n-1)))

print(integral)


# Merk, forskjellige metoder gir forskjellige svar (grunnet feilen i metoden), men for glatte funksjoner går begge mot samme tall når N er stor
