# Exercise 7.11 Langtangen

from math import *

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x):
        return exp(-self.a*x)*sin(self.w*x)

    def __str__(self):
        return f'exp({-self.a}*x) * sin({self.w}*x)'

f = F(a=1.0, w=0.1)
print(f(x=pi))
f.a = 2     # Redigerer self.a i klassen
print(f(pi))

print(f)
