import sympy as sp
from sympy import cos, sin, factorial, exp, pi, sqrt, ln
import numpy as np
import matplotlib.pyplot as plt
import time

# Kjører while-loop så du kan gjenta uten å kjøre kode på nytt
# Ønsker du absoluttverdi skriver du det som sqrt(x**2) eller (x**2)**0.5. Eks. ln((x**2)**0.5)
# eksempel: sin(3*x)/x + cos(x), trenger ikke modulnavn som np. foran etc.
while True:
    func = input('\nInput function:')
    center = float(input('Input center:'))
    # Dekorator som lagrer og henter data som allerede er regnet ut
    def cache(f):
        cache_dict = {}
        def wrapper(*args, **kwargs):
            if args in cache_dict:
                # print('Return from cache')
                return cache_dict[args]
            else:
                # print('Calculate...')
                cache_dict[args] = f(*args, **kwargs)
                return f(*args, **kwargs)

        return wrapper

    # Dekorator som tar tiden på hvor lang tid funksjonen bruker på å kjøre
    def timer(f):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = f(*args, **kwargs)
            t2 = time.time() - t1
            print(f'{f.__name__} ran in {t2} seconds')
            return result

        return wrapper

    # Regner ut Taylor-leddet
    @cache
    def df(f, n):
        x, a = sp.symbols('x a')
        return f.diff(a, n)*(x-a)**n / sp.factorial(n)

    def Taylor(f, n):
        x, a = sp.symbols('x a')        # Gjør x og a om til symboler
        f = f.replace('exp', '~').replace('x', 'a').replace('~', 'exp')     # Triks for å unngå å bytte ut 'x' i 'exp'
        f = eval(f)         # Evaluerer uttrykket (string) som en Python funksjon
        s = 0
        for n in range(n+1):
            s += df(f, n)                   # Summerer opp Taylor-ledd
        s = sp.lambdify([x, a], s)          # Gjør om symbol-uttrykk til en ekte funksjon av x og a (gjør x og a til variabler i stedet for symboler)
        return s

    # Funksjon som looper gjennom alle gradene av Taylor-polynomet og visualiserer det
    @timer
    def animate(func, n):
        x = np.linspace(-10, 10, 300)
        func_str = func.replace('x.', 'x')
        f_plot = eval(func.replace('cos', 'np.cos').replace('sin', 'np.sin').replace('sqrt', 'np.sqrt').
                           replace('pi', 'np.pi').replace('exp', 'np.exp').replace('ln', 'np.log'))
        for n in range(1, n+1):
            T = Taylor(func, n)
            plt.plot(x, T(x, center))
            plt.plot([x[0], x[-1]], [0,0], 'k', alpha=0.8)
            plt.plot([0, 0], [x[0], x[-1]], 'k', alpha=0.8)
            plt.plot(x, f_plot, 'r')
            plt.ylim(-5, 5)
            plt.text(1,2, f'f(x)={func_str}', color='r')
            plt.title(f'n = {n}')
            plt.draw()
            plt.pause(0.3)
            plt.clf()

    animate(func, 25)
