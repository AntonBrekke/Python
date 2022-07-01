# Exercise 8.7 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

# a)
class Diff:
    def __init__(self, function):       # Tar inn funksjon som argument
        self._f = function

    def diff1(self, x, h):      # Første metode for approksimasjon av deriverte
        df1 = (self._f(x + h) - self._f(x)) / h
        return df1

    def diff2(self, x, h):      # Andre metode for approksimasjon av deriverte
        df2 = (self._f(x + h) - self._f(x - h)) / (2*h)
        return df2

    def diff3(self, x, h):      # Tredje metode for approksimasjon av deriverte
        df3 = (-self._f(x + 2*h) + 8*self._f(x + h) - 8*self._f(x - h) + self._f(x - 2*h)) / (12*h)
        return df3

# b)
f = lambda x: np.sin(2*np.pi*x)

# def f(x):
#     return np.sin(2*np.pi*x)

object = Diff(f)      # Bruker lambda fordi jeg kan sende hele funksjonsuttrykket inn (ser penere ut)


x = np.linspace(-1, 1, 1000)        # Lager array med Df = [-1,1] for plot
f_ex = 2*np.pi*np.cos(2*np.pi*x)    # Eksakt uttrykk for den deriverte

h_list = [0.9, 0.6, 0.3, 0.1]       # Delta-verdier for approksimasjon

# Animerer fordi jeg kan, kan evt. bruke subplot som bedre løsning
for h in h_list:
    plt.plot(x, object.diff1(x, h), 'r', label='diff1')
    plt.plot(x, object.diff2(x, h), 'orange', label='diff2')
    plt.plot(x, object.diff3(x, h), 'tab:blue', label='diff3')

    plt.plot(x, f_ex, 'k--', label='exact', linewidth = 3)

    plt.xlabel(f'h = {h}')
    plt.legend()
    plt.title(f'h = {h}')

    plt.draw()
    plt.pause(1.8)      # Setter pause på 1.8s så jeg kan se bedre
    plt.clf()

# Kjøreekmsempel i terminal:
"""
PS C:\Desktop\Python\Oblig uke 44 IN1900> python class_diff.py
PS C:\Desktop\Python\Oblig uke 44 IN1900>
"""
