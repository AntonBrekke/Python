"""
Problem 3.5. Sum as a while loop Write the (corrected) for loop from the
previous exercise as a a while loop. Check that the two loops compute the same
answer.
"""

# For-kode fra forrige oppgave:
"""
s = 0
M = 3
for k in range(1, M + 1):
    s += 1/(2*k)**2
    print(k, s)
"""

# Omformoulert kode fra for til while:
k = 1       # Startverdi k
s = 0       # Definert s og startverdi
while k <= 3:       # While-loop og sluttverdi k 
    s += 1/(2*k)**2
    print(k, s)
    k += 1

# Kjøretest fra terminal for sum_while.py:
"""
PS C:\Desktop\python> python .\sum_while.py
1 0.25
2 0.3125
3 0.3402777777777778
"""
