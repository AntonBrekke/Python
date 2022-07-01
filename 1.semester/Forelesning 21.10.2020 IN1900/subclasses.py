# Subklasser

"""
Klasser kan ha 'underklasser', 'subklasser',
eller 'datterklasser' (kjært barn mange navn).
En underklasse arver egenskapene fra
moderklassen, og skrives på formen:
class MotherClass:
    ...
class Subclass(MotherClass):
    ...
Det handler i grunn om god kodeskriving,
der man unngår mye copy-paste i koden
for optimalisering og mer lesbare koder etc.
OOP er ikke så viktig i Python hvis man
sammenlikner OOP i C++, Java og C#, så
fordelene er ikke like åpenbare i Python.
"""
# Eksempel:
class A:
    def __init__(self, v0, v1):
        self.v0 = v0
        self.v1 = v1
    def f(self, x):
        return x**2


class B(A):
    def g(self, x):
        return x**4

class C(B):
    def h(self, x):
        return x**6

"""
A attributer v0,v1 og metode f
B har attributer v0, v1 og metoder f, g
C har attributer v0,v1 og metoder f, g, h
"""
# Eksempel på kode som unngår duplikering:
class A:
    def __init__(self, v0, v1):
        self.v0 = v0
        self.v1 = v1
    def f(self, x):
        return x**2


class B(A):
    def __init__(self,v0, v1, v2):
        super().__init__(v0,v1) # eller A.__init__(self,v0,v1)
        self.v2 = v2

    def g(self, x):
        return x**4

# Eksempel; En klasse for rette linjer:
class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1

    def __call__(self,x):
        return self.c0 + self.c1*x

    # Metode for plotting

# Kan breuke 'isinstance(object, class)' for å sjekke om et objekt hører til en klasse
