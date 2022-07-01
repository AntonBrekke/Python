import numpy as np
import matplotlib.pyplot as plt

# Eksempel:
# 5*cos(3*x)*exp(-0.5*x)*u(x+4)
# c*(x - a)*u(x - a) + d*(-x + b)*u(x - b)
# a er der linja knekker opp og b er der linja knekker ned, c < d
# eks. (x + 5)*u(x+5) + 2*(-x + 0)*u(x-0)

# Implementerer unit-step funksjonen
def u(t):
    d = t.copy()    # For å unngå at x-arrayen endres (skjedde om jeg brukte u(x) og ikke lagde kopi av t)
    for i in range(len(d)):
        if d[i] > 0:
            d[i] = 1
            # print(i, t[i])
        else:
            d[i] = 0
            # print(i, t[i])
    return d
# Implementerer dirac-delta funksjonen
def d(x, a):
    if isinstance(a, (int, float)):
        a = a,
    s = np.zeros_like(x)
    epsilon = 1e-2
    print(a)
    for j in range(len(a)):
        d = x.copy()
        for i in range(len(d)):
            if x[i] <= a[j] + epsilon and x[i] >= a[j] - epsilon:
                d[i] = 1
            else:
                d[i] = 0
        s += d

    return s

while True:

    func = input('Input function (enter to show plot): ')
    if func.strip() == '':
        break

    x = np.linspace(-10, 10, 1500)

    f = eval(func.replace('cos', 'np.cos').replace('sin', 'np.sin').replace('ln', 'np.log')
                    .replace('sqrt', 'np.sqrt').replace('pi', 'np.pi').replace('exp', 'np.exp')
                    .replace('tan', 'np.tan').replace('arcsin', 'np.arcsin').replace('arccos', 'np.arccos')
                    .replace('arcnp.sin', 'np.arcsin').replace('arcnp.cos', 'np.arccos')
                    .replace('arcnp.tan', 'np.arctan'))
    # Tester om f bare er en skalar
    if isinstance(f, (int, float)):
        f = f*np.ones_like(x)

    plt.plot(x, f, label=func)
    plt.legend(loc='upper right')

plt.show()
