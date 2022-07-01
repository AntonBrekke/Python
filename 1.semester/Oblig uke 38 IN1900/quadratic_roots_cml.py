# Exercise 5.2
import sys      # Importerer sys for å bruke argv
from math import sqrt

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if b**2 - 4*a*c < 0:            # Tester for komplekse røtter
    print("Values gives complex roots")
    exit()

# Løsninger for x gitt ved abc-formel:
x1 = (-b + sqrt(b**2 - 4*a*c))/2
x2 = (-b - sqrt(b**2 - 4*a*c))/2
print("")
print(f"For values {a}, {b}, {c}, x1 = {x1} and x2 = {x2}")

# Kjøretest fra terminal:
"""
Terminal> python quadratic_roots_cml.py 1 -5 6
For values 1.0, -5.0, 6.0, x1 = 3.0 and x2 = 2.0
"""
