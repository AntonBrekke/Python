"""
Oppgave 3.8, oppgavehefte
"""
#a)
from math import exp

t_list = []     #list for time
n_list = []     # List for amount N

B = 50000   # Systemets bæreevne
k = 0.2
C = 9.0
a = 0
b = 48      # Total lengde på intervall
n = 12       # Antall intervaller ønsket
h = round((b-a)/n)     # Lengde på vært intervall

for t in range(a, b+1, h):  # Plotter inn verdier i liste med for-loop
    N = B/(1 + C*exp(-k*t))
    n_list.append(round(N)) # Runder av verdien N til første heltall
    t_list.append(t)

tN1 = [t_list, n_list]  # Lager nested list og printer ut verdier
for k in range(len(t_list)):
    print(f"{tN1[0][k]}h\t| {tN1[1][k]}")

print("")
#b)

tN2 = [[t,N] for t, N in zip(t_list, n_list)]
for i in range(len(tN2)):
    print(f"{tN2[i][0]}h\t| {tN2[i][1]}")


# Kjøreeksempel fra terminalen:
"""
PS C:\Desktop\Python> python population_table2.py
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
