# Oppgave 3 Oblig MAT-INF1100
from random import random

#a)
antfeil = 0; N = 100000

for i in range(N):
    x = random(); y = random(); z = random()
    res1 = (x + y) * z
    res2 = x*z + y*z
    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y; z0 = z
        ikkelik1 = res1
        ikkelik2 = res2

print (100. * antfeil/N)
print (x0, y0, z0, ikkelik1 - ikkelik2)

"""
Programmet tar 3 tilfeldige flyttall mellom 0 og 1,
og regner ut antall ganger res1 og res2
(2 like regnestykker skrevet på ulik måte) er ulike
hverandre pr. gang de regnes ut (i prosent), printer
ut hvilke verdier det har brukt, og differansen
mellom tallene.
"""
# b)
from random import random
antfeil = 0; N = 100000

for i in range(N):
    x = random(); y = random(); z = random()
    res1 = (x + y) * (y + z)
    res2 = x*y + y*y + x*z + y*z
    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y; z0 = z
        ikkelik1 = res1
        ikkelik2 = res2

print (100. * antfeil/N)
print (x0, y0, z0, ikkelik1 - ikkelik2)

#41.363 prosent ganger feil
#0.48429574035524736 0.7680057701780899 0.3567778353542159 2.220446049250313e-16
"""
Grunnen til at det blir flere feil tror jeg
er fordi det blir flere addisjonsledd mellom
x, y og z, som fører til flere avrundingsfeil
når man jobber med flyttall.
"""
