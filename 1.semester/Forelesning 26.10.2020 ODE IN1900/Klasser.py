class A:
    def f(x):
        return x**2

class B(A):
    def g(x):
        return x**4

class C(B):
    def h(x):
        return x**6

"""
A: et argument, en metode f
B: et argument, to metoder f, g
C: et argument, tre metoder f, g, h
"""
print(C.f(2))
print(C.g(2))
print(C.h(2))

# Numerisk derivasjon:
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
