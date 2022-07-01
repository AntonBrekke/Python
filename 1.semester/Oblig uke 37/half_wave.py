from math import sin, pi

def f(x):               # f(x), returnerer positive verdier fra sin(x)
    if 0 < sin(x):
        return sin(x)
    else:
        return 0

def test_f():       # Testfunksjon som tester om verdien fra funksjonen stemmer
    expected1 = 1           # Forventer returnert verdi lik 1
    expected2 = 0           # Forventer returnert verdi lik 2
    computed1 = f(pi/2)     # Positiv verdi for sin(x)
    computed2 = f(3/2*pi)   # Negativ verdi for sin(x)
    msg = 'Something is wrong'
    tol = 1e-14             # Toleranseverdi, dersom differansen mellom forventet og beregnet er mindre enn tol er svaret ok
    success1 = abs(expected1 - computed1) < tol
    success2 = abs(expected2 - computed2) < tol
    assert success1, msg        # Dersom success1 er usann returnerer assert msg
    assert success2, msg
test_f()
# Kjøretest fra terminal:
"""
PS C:\Desktop\Python> python half_wave.py
PS C:\Desktop\Python>
"""
