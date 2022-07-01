# Oblig MAT-INF1100 Oppgave 2
# a)
def prod1(i, n):
    p = 1
    for j in range(1, i + 1):
        p *= (n - j + 1)/j
    return p
print(prod1(4, 5000.))
print(prod1(500, 1000.))
print(prod1(99940, 100000.))


#1 n = 5000, i = 4 -> 26010428123750.0
#2 n = 1000, i = 500 -> 2.702882409454359e+299 (2.702882409454366e+299)
#3 n = 100000, i = 99940 -> inf (1.1806919799625e+218)

print(type(4.0))
"""
"""

#b)
"""
Det er fullt mulig og få overflow underveis
i utregningen selv om tallet jeg skal beregne
er mindre enn det største flyttallet datamaskinen
kan representere. Tallet fra forsøk 2 i oppgave
a er større en tallet fra forsøk 3, og begge
er mindre enn det største flyttallet maskinen
kan representere, dermed må det ha skjedd en overflow
underveis. Det er fordi tallene i og n ikke kan
representeres fordi de blir for store, selv om
binomialkoeffisienten i seg selv ikke er så stor.
"""

#c)
"""
Metoden over er inneffektiv for verdier
i > n/2. Jo større ulikheten blir, dess
større unøyaktighet forekommer i datamaskinen.
Ved å bruke den opprinnelige definisjonen
for binomialkoeffisienten (gitt i oppgaven)
får du mer nøyaktige svar. Dette er fordi det
er en modul som regner ut fakultetene istedet for
en loop, og modulen bruker ressursene i hardwaren
på pcen for å gjennomføre beregningene.
"""

import numpy as np
def prod2(i, n):
    p = np.math.factorial(n)/(np.math.factorial(i)*np.math.factorial(n-i))
    return p

print(prod2(40000, 100000))

#n = 100000, i = 99940 -> 1.1806919799625e+218
