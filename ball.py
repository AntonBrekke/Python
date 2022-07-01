"""
Posisjon ball y som funksjon av tiden t, y(t))
"""
v_0 = 5
g = 9.81
t = 0.6
y = v_0*t - 1/2*g*t**2
print(y)


a = "10"
b = 10
print(a*b)


"""
From math import gir deg frihet til å velge ut spesifike funksjoner, f.eks:
from math import sqrt
r = sqrt(2)
 math import gir deg alle matematiske funksjoner, men du må skrive inn
 modulen før du bruker den, f.eks r = math.sqrt(2).
 Import math * gir
 deg tilgang til alle funksjoner i math, men kan være problematisk siden
 den deler funksjoner med flere moduler.
"""
from math import sin, cos, log

x = 1.2
print(sin(x)*cos(x) + 4*log(x))
