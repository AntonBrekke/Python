# Exercise 7.1
from math import *
class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        return exp(-self.a*x)*sin(self.w*x)

# Class usage (fra oppgave):
f = F(a=1, w=0.1)
print(f.value(x=pi))
f.a = 2
print(f.value(pi))
