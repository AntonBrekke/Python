import sympy as sp
from sympy import cos, sin, factorial, exp
import numpy as np
import matplotlib.pyplot as plt

func = input('Input function:')

def Taylor(f, n):
    x, a = sp.symbols('x, a')
    f = eval(f.replace('(x)', '(a)'))
    s = 0
    for n in range(n+1):
        s += f.diff(a, n)*(x-a)**n / sp.factorial(n)
    s = sp.lambdify([x, a], s)
    return s



x = np.linspace(-10, 10, 300)
for n in range(1, 25):
    T = Taylor(func, n)

    plt.plot(x, T(x, 0))
    # plt.plot(x, np.sin(x), 'r')
    plt.ylim(-5, 5)
    plt.title(f'n = {n}')
    plt.draw()
    plt.pause(0.1)
    plt.clf()
