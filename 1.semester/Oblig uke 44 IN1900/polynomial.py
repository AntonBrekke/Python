# Exercise 9.2 oppgaveheftet

"""
I denne oppgaven antar jeg at inputen skal komme på
formen [a,b,c] eller (a,b,c) der a er koeffisienten
foran tredje grad, b er koeffisienten foran andre grad,
og c er en konstant.
"""
# a)
class Quadratic:
    def __init__(self, coeff):      # Coeff må være liste/tuppel med koeffisienter
        self._a = coeff[0]
        self._b = coeff[1]
        self._c = coeff[2]

    def __call__(self, x):          # Spesiell metode '__call__' for penere syntax
        return self._a*x**2 + self._b*x + self._c

    def __str__(self):              # Spesiell metode '__str__' for penere kode
        s = f'Polynomial: {self._a}*x^2 + {self._b}*x + {self._c}'
        return s

poly = (1,3,2)
y1 = Quadratic(poly)    # Objekt/instanse med koordinater poly
print(y1)               # Bruk av '__call__'
print(f'Evaluated in x = 1: {y1(1)}')   # Bruk av '__str__'
print(f'Evaluated in x = 2: {y1(2)}')
print("")   # Penere output

# b)
class Cubic(Quadratic):         # Lager subclass av Quadratic, og tar med meg egenskaper fra Quadratic inn i Cubic
    def __init__(self, coeff):
        Quadratic.__init__(self, coeff)
        self._d = coeff[3]

    def __call__(self, x):      # Oppgraderer annengrad til tredjegrad
        return (Quadratic.__call__(self, x))*x + self._d

    def derivative(self):       # Derivert for tredjegrads polynomer
        self._a *= 3; self._b *= 2
        temp = [self._a, self._b, self._c]
        return Quadratic(temp)      # Leverer temp til Quadratic

    def __str__(self):
        s = f'Polynomial: {self._a}*x^3 + {self._b}*x^2 + {self._c}*x + {self._d}'
        return s


poly2 = (1,3,2,4)
y2 = Cubic(poly2)   # Objekt/instanse med koordinater poly2
print(y2)
print(f'Evaluated in x = 1: {y2(1)}')
print(f'Evaluated in x = 2: {y2(2)}')
print(f'Cubic Derivative = {y2.derivative()}, {type(y2.derivative())}')


# Kjøreekmsempel fra terminal a og b:
"""
PS C:\Desktop\python\Oblig uke 44 IN1900> python polynomial.py
Polynomial: 1*x^2 + 3*x + 2
Evaluated in x = 1: 6
Evaluated in x = 2: 12

Polynomial: 1*x^3 + 3*x^2 + 2*x + 4
Evaluated in x = 1: 10
Evaluated in x = 2: 28
Cubic Derivative = Polynomial: 3*x^2 + 6*x + 2, <class '__main__.Quadratic'>
"""
