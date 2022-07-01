# Exercise 8.9 oppgaveheftet
import numpy as np

# a)
class Coords:
    def __init__(self, x, y, z):        # Lager konstrukør som lagrer koordinater
        self._x = x
        self._y = y
        self._z = z

    def __len__(self):      # Regner lengde på dimensjoner (alltid 3)
        length = len([self._x, self._y, self._z])
        return length

    def __abs__(self):      # Regner lengde fra origo til koordinatet
        abs = np.sqrt((self._x)**2 + (self._y)**2 + (self._z)**2)
        return abs

    def __add__(self, other):       # Metode som legger sammen respektive koordinater
        x_new = self._x + other._x
        y_new = self._y + other._y
        z_new = self._z + other._z
        return Coords(x_new, y_new, z_new)  # Returnerer en instanse med de nye verdiene for å få ut tall og ikke en tuppel

    def __sub__(self, other):       # Metode som subtraherer respektive koordinater
        x_new = self._x - other._x
        y_new = self._y - other._y
        z_new = self._z - other._z
        return Coords(x_new, y_new, z_new)  # Returnerer en instanse med de nye verdiene for å få ut tall og ikke en tuppel

    def __str__(self):      # Spesiell metode som returnerer strengen
        s = f'({self._x:.2f}, {self._y:.2f}, {self._z:.2f})'
        return s

sqrt3 = np.sqrt(3)
close = Coords(1/sqrt3, 1/sqrt3, 1/sqrt3)
far = Coords(3/sqrt3, 15/sqrt3, 21/sqrt3)
print(close)        # Bruk av '__str__'
print(far)

# Kjøreekmsempel i terminal a):
"""
PS C:\Desktop\Python\Oblig uke 44 IN1900> python Coords.py
(0.58, 0.58, 0.58)
(1.73, 8.66, 12.12)
"""

# b)
"""
La til metode '__len__' og '__abs__' i class Coords:
"""
# Kall fra oppgave:
print(f"The class represents coordinates in {len(close)} dimensions")
print(f"The distance from the centre to the point close is {abs(close):.2f}")
print(f"The distance from the centre to the point far is {abs(far):.2f}")

# Kjøreekmsempel i terminal b):
"""
PS C:\Desktop\Python\Oblig uke 44 IN1900> python Coords.py
The class represents coordinates in 3 dimensions
The distance from the centre to the point close is 1.00
The distance from the centre to the point far is 15.00
"""

# c)
"""
La til metode '__add__' og '__sub__' i class Coords:
"""
# Kall fra oppgave:
further = close + far
print(f"The coordinates further are at {further}")
distance = abs(far - close)
print(f"The distance from far to close is {distance:.2f}")
centre = further - further
print(f"The coordinates at the centre are {centre}")


# Kjøreekmsempel i terminal c):
"""
PS C:\Desktop\Python\Oblig uke 44 IN1900> python Coords.py
The coordinates further are at (2.31, 9.24, 12.70)
The distance from far to close is 14.14
The coordinates at the centre are (0.00, 0.00, 0.00)
"""
