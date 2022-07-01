"""
Problem 2.4. Solve the quadratic equation
"""
from math import sqrt

# Formula 6x**2 + 5x + 1 = 0
a = 6
b = 5
c = 1

x_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f"When 6x^2 + 5x + 1 = 0, x equals x_1 ={x_1} and x ={x_2}")

#Kjøretest find_roots.py:
"""
PS C:\Desktop\python> python find_roots.py
When 6x^2 + 5x + 1 = 0, x equals x_1 =-0.3333333333333333 and x =-0.5
"""
