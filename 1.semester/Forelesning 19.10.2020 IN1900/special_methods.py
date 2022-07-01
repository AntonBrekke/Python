# Spepcial methods

"""
Spesielle metoder er metoder som
er allerede innebygd i Python. Python
gjenkjenner metoden automatisk når
man kaller på en instanse og kjører
den uten at brukeren må kalle på den.
Konstruktøren '__init__' er f.eks en spesiell metode,
samt '__call__' etc.
"""

class Y:
    def __init__(self, v0):
        self._v0 = v0
        self._g = 9.81

    def __call__(self, t):
        return self._v0*t - 0.5*self._g*t**2

y = Y(3)
v = y(0.1)      # Dette gitt den spesielle metoden '__call__'


"""
Det finnes også metoder for strenger,
som '__str__' eller '__repr__'.

Det finnes også metoder for
aritmetiske operasjoner:
c = a + b   #   c = a.__add__(b)
c = a - b   #   c = a.__sub__(b)
c = a * b   #   c = a.__mul__(b)
c = a / b   #   c = a.__div__(b)
c = a**e   #   c = a.__pow__(e)

og samme for å sammenlikne opbjekter:
a == b   #   c = a.__eq__(b)
a != b   #   c = a.__ne__(b)
a < b   #   c = a.__lt__(b)
a <= b   #   c = a.__le__(b)
a > b   #   c = a.__gt__(b)
a >= b   #   c = a.__ge__(b)
"""

# Class for polynomials

class Polynomial:
    def __init__(self, coefficients):       # Tar liste som argument
        self._coeff = coefficients

    def __call__(self, x):
        s = 0
        for i in range(len(self._coeff)):
            s += self._coeff[i]*x**i
        return

# Addition
class PolyAdd:
    def __init__(self, coefficients):       # Tar liste som argument
        self._coeff = coefficients

    def __add__(self, other):
        # return self + other

        if len(self._coeff) > len(other._coeff):
            coeffsum = self.coeff[:] # Copy
            for i in range(len(other._coeff)):
                coeffsum[i] += other._coeff[i]
        else:
            coeffsum = self.coeff[:] # Copy
            for i in range(len(self._coeff)):
                coeffsum[i] += self._coeff[i]
        return PolyAdd(coeffsum)

# Multiply
class PolyMul:
    def __init__(self, coefficients):       # Tar liste som argument
        self._coeff = coefficients

    def __mul__(self, other):
        M = len(self._coeff) - 1
        N = len(other._coeff) - 1
        coeff = [0]*(M+N+1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                coeff[j+i] += self._coeff[i]*other._coeff[j]
        return PolyMul(coeff)
