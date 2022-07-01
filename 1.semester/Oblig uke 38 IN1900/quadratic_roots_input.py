# Exercise 5.1

from math import sqrt
print("The quadratic formula is written for a function ax^2 + bx + c = 0 to solve x.")
a = float(input("Input value a in quadratic formula:"))
b = float(input("Input value b in quadratic formula:"))
c = float(input("Input value c in quadratic formula:"))

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
Terminal> python quadratic_roots_input.py
The quadratic formula is written for a function ax^2 + bx + c = 0 to solve x.
Input value a in quadratic formula:1
Input value b in quadratic formula:-5
Input value c in quadratic formula:6
For values 1.0, -5.0, 6.0, x1 = 3.0 and x2 = 2.0
"""
