# Snublegruppeppgave fra fysikkheftet: height.py

from math import cos, sin, pi

# Skrevet som def:
def y(t, v0, theta, g=9.81):
    return -1/2*g*t**2 + v0*t*sin(theta) # Funksjon for høyde gitt i oppgave

# Skrevet med lambda-funksjon:
g = 9.81
y = lambda t, v0, theta:-1/2*g*t**2 + v0*t*sin(theta)

a = y(6, 20, pi/6)
print(a)

def points(v0, theta=pi/4, b=3.5, h0=3, h1=3.5): # Verdier gitt i oppgave
    T = b/(v0*cos(theta))
    x = y(T, v0, theta)
    if x < h0 or x > h1:
        return 0
    elif h0 <= x < 1/2*(h1 + h0):
        return 1
    elif 1/2*(h1+h0)<= x <= h1:
        return 2

for v0 in [15, 16, 19, 22]:
    print(f"v0 = {v0}m/s gives {points(v0)} point")

# Oppgae fra hefte: factorial.py
from math import factorial

def myfactorial(n):
    fac_n = 1
    for i in range(1, n+1):
        fac_n *= i      # fac_n = fac_n * i
    return fac_n

from math import factorial
def test_myfactorial():
    n = 34
    expected = factorial(n)
    computed = myfactorial(n)
    success = expected == computed
    tol = 1e-14
    success = abs(expected - computed) < tol
    assert success

test_myfactorial()

n1 = 10
assert factorial(n1) == myfactorial(n1)
