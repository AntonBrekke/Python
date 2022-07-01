from math import sin, pi

def f(x):
    if 0 < sin(x):
        return sin(x)
    else:
        return 0

def test_f():
    expected1 = 1
    expected2 = 0
    computed1 = f(pi/2)
    computed2 = f(3/2*pi)
    msg = 'Something is wrong'
    tol = 1e-14
    success1 = abs(expected1 - computed1) < tol
    success2 = abs(expected2 - computed2) < tol
    assert success1, msg
    assert success2, msg
test_f()
# Kjøretest fra terminal:
"""
PS C:\Desktop\Python> python half_wave.py
PS C:\Desktop\Python>
"""
