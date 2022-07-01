# Exercise 8.2 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

# a)
class RightTriangle:
    def __init__(self, a, b):
        if a < 0 or b < 0:          # Tester om sidelengdene på trekantene er negative
            raise ValueError('a and b must be bigger than 0.')
        else:
            self.a = a
            self.b = b
            self.c = np.sqrt(self.a**2 + self.b**2)

    def plot_triangle(self):            # Lager metode for å plotte punkter i trekant
        plt.plot([0, 0], [0, self.b])
        plt.plot([0, self.a], [0, 0])
        plt.plot([0, self.a], [self.b, 0])
        plt.xlabel('a'); plt.ylabel('b')
        plt.axis('equal')               # Setter aksene like
        plt.show()

# b)
triangle1 = RightTriangle(1,1)      # Lager objekt med sidelengde 1 og 1
triangle2 = RightTriangle(3,4)      # Lager objekt med sidelengde 3 og 4
triangle1.c                # Kaller på variablel i objekt
triangle2.c                # Kaller på variabel i objekt

# Kjøretest fra terminal (b):
"""
PS C:\Desktop\Python\Oblig uke 43 IN1900> python right_triangle.py
1.4142135623730951
5.0
"""

# c)
"""
Redigerte def __init__:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError('a and b must be bigger than 0.')
        else:
            self.a = a
            self.b = b
            self.c = np.sqrt(a**2 + b**2)
"""
# Testfunksjon for om if-test i konstruktør funker:
def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success

test_RightTriangle()

# Kjøretest fra terminal (c):
"""
PS C:\Desktop\Python\Oblig uke 43 IN1900> python right_triangle.py
PS C:\Desktop\Python\Oblig uke 43 IN1900>
"""

# d)
"""
Lagde metode for plot i class RightTriangle:
    def plot_triangle(self):
        plt.plot([0,0],[0,self.b])
        plt.plot([0,self.a],[0,0])
        plt.plot([0,self.a],[self.b,0])
        plt.xlabel('a'); plt.ylabel('b')
        plt.axis('equal')
        plt.show()
"""

triangle2.plot_triangle()           # Kaller på plot-metode for objekt triangle2

# Kjøretest fra terminal (d):
"""
PS C:\Desktop\Python\Oblig uke 43 IN1900> python right_triangle.py
PS C:\Desktop\Python\Oblig uke 43 IN1900>
"""
