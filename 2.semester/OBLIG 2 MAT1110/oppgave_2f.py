import numpy as np
import sympy as sp

epsilon = 0
theta = np.linspace(-np.pi/4 + epsilon, np.pi/4 - epsilon, 100000)

# Taylorutvikling for cos(2x)
def Taylor_series(n, a):
    sum = 0
    x = sp.Symbol('x')
    for i in range(n+1):
        sum += (-1)**i*2**(2*i)*(x-a)**(2*i) / np.math.factorial(2*i)
    sum = sp.lambdify(x, sum)
    return sum

cos2x = Taylor_series(2, 0)

# Funksjon som skal integreres
def r(theta):
    return 1 / np.sqrt(cos2x(theta))

# Bruker trapes-metoden:
integral1 = 0
for i in range(len(theta)-1):
    dt = theta[i+1] - theta[i]
    integral1 += (r(theta[i]) + r(theta[i+1]))*dt / 2

print(integral1)

# Bruker midtpunkt-metoden:
integral2 = 0
for i in range(len(theta)-1):
    M = (theta[i+1] + theta[i]) / 2
    dt = theta[i+1] - theta[i]
    integral2 += dt * r(M)

print(integral2)

# Bruker Simpsons metode:
integral3 = 0
for i in range(len(theta)-1):
    dt = theta[i+1] - theta[i]
    integral3 += (dt/6) * (r(theta[i]) + 4*r((theta[i] + theta[i+1])/2) + r(theta[i+1]))

print(integral3)

# print(f'Mean: {(integral1 + integral2 + integral3) / 3}')
