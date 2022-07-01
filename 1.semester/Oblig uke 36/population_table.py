"""
Problem 3.7. Table showing population growth
Consider again the bacterial colony from Problem 2.2. We now want to study
how the population grows with time, by calculating the number of individuals
for n + 1 uniformly spaced t values throughout the interval [0, 48]. Set n = 12
and write a for loop which computes and stores t and N values in two lists t
and N. Thereafter, traverse the two lists with a separate for loop and write out
a nicely formatted table of t and N values
"""

from math import exp

t_list = []
n_list = []

B = 50000   # Systemets bæreevne
k = 0.2
C = 9.0
a = 0
b = 48      # Total lengde på intervall
n = 12      # Antall intervaller ønsket
h = round((b-a)/n)     # Lengde på vært intervall

# Fyller lister med verdier:
for t in range(a, b+1, h):
    N = B/(1 + C*exp(-k*t))
    n_list.append(N)
    t_list.append(t)
#print("___________________")
for k in range(len(t_list)):
    print(f"|{t_list[k]}h\t| {round(n_list[k])}\t|")
    #print("|_______|_________|")
# Kjøretest fra terminal for population_table.py
"""
PS C:\Desktop\python> python .\population_table.py
|0h     |  5000.00|
|4h     |  9912.84|
|8h     | 17748.95|
|12h    | 27526.04|
|16h    | 36580.20|
|20h    | 42924.32|
|24h    | 46552.00|
|28h    | 48389.56|
|32h    | 49263.32|
|36h    | 49666.28|
|40h    | 49849.50|
|44h    | 49932.26|
|48h    | 49969.54|
"""
