# Exercise 5.3
import sys      # Importerer sys for å burke argv
from math import sqrt
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])


except IndexError:
    if len(sys.argv) == 3:
        print("Missing value c")
        c = float(input("Input missing c:"))
    elif len(sys.argv) == 2:
        print("Missing values b and c")
        b = float(input("Input missing b:"))
        c = float(input("Input missing c:"))
    else:
        print("Missing values a, b and c")
        a = float(input("Input missing a:"))
        b = float(input("Input missing b:"))
        c = float(input("Input missing c:"))

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
Terminal> python quadratic_roots_error.py 1 -5 6
For values 1.0, -5.0, 6.0, x1 = 3.0 and x2 = 2.0

Terminal> python quadratic_roots_error.py
Missing values a, b and c
Input missing a:1
Input missing b:-5
Input missing c:6
For values 1.0, -5.0, 6.0, x1 = 3.0 and x2 = 2.0
"""
