from math import exp

def N(t, k = 0.2, B = 50000, C = 9.0):  # Definerer funksjon med gitte variabler (3.7)
    N = B/(1 + C*exp(-k*t))
    return N            # Returnerer verdi N til funksjonen

a = 0       # Startverdi intervall
b = 48      # Sluttverdi intervall
n = 12      # Antall intervaller ønsket
h = round((b-a)/n)  # Lengde på hvert intervall

for t in range(a, b+1, h):
    print(f"{t}h\t| {round(N(t))}")

# Kjøretest fra terminal:
"""
PS C:Desktop\Python> python pop_func.py
0h      | 5000
4h      | 9913
8h      | 17749
12h     | 27526
16h     | 36580
20h     | 42924
24h     | 46552
28h     | 48390
32h     | 49263
36h     | 49666
40h     | 49849
44h     | 49932
48h     | 49970
"""
