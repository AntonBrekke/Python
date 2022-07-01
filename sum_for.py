"""
Problem 3.4. Errors in summation
The following code is supposed to compute the sum s =
PM
k=1
1
(2k)
2 , for M = 3.
s = 0
M = 3
for i in range(M):
s += 1/2*k**2
print(s)
The program has three errors and therefore does not work. Find the three errors
and write a correct program. Put comments in your program to indicate what
the mistakes were.
"""

# Original kode:
"""
s = 0
M = 3
for i in range(M):
s += 1/2*k**2
print(s)
"""


# Redigert og fikset kode:
s = 0
M = 3
for k in range(1, M + 1):   # Definert k i range, definert range fra 1 til 3
    s += 1/(2*k)**2     #Fikset formel fra 2*k**2 til (2*k)**2
    print(k, s)     #Printer med verdi k og korresponderende sum

#Kjøretest fra terminal sum_for.py:
"""
PS C:Desktop\python> python .\sum_for.py
1 0.25
2 0.3125
3 0.3402777777777778
"""
