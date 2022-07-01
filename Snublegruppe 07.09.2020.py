a = ['a', 'd', 'g', 'j']
b = ['b', 'e', 'h', 'k']
c = ['c', 'f', 'i', 'l']
alf = zip(a,b,c)
alf = list(alf)
print(alf)
for index, al in enumerate(alf):
    print(f'Number {index + 1} is {al[0]} {al[1]} {al[2]}')

print(False == (True == True))
print(True == (False == False))
print(True == (False and True))
print(False == (True or False))

def f(x):
    f = x**2
    return f

x = 10
print(f"f({x}) = {f(x)}")

from math import cos, pi
import random

def f(x):
    if 0 <= x <= pi:
        return cos(x)
    else:
        return 'x is not 0 <= x <= pi'
n = random.randint(-3,3)
m = random.randint(0,10)
x = pi*n/m
print(f(x))
