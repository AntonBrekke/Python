#Gjenta lister
a = [1, 0, 1, 1, 0]*3
print(a)

# Angi en regel for å generere verdier:
a = [i*i for i in range(0, 5)] # [0 , 5>
print(a)
b = [e**2 for e in a]
print(b)
c = [e**2 for e in a if e%2==0] #Kun de som kan deles på 2
print(c)

# Skrive summasjon med while-løkke:
s = 0 # Startverdi
i = 1 # Nedre grense
while i <= 100: #Øvre grense
    s += 1.0/i # Formel som skal summeres
    i += 1 # Indeks skal øke med 1
print("s = %g" % s)

# Skrive summasjon i for løkke:
s = 0 # Startverdi
for i in range(1, 101): # Øvre og nedre grense
    s += 1.0/i # Formel som skal summeres
print("s = %g" % s)


# Skrive summasjon med implisitt løkke:
s = sum(1.0/i for i in range(1, 101))
print("s = %g" % s)


# Fibonacci-følgen:
F = [1]*100
for k in range(2, 100):
    F[k] = F[k-1] + F[k-2]
print(F)

# Alternativ løsning:
F = [1, 1]
for k in range(2, 100):
    F.append(F[k-1] + F[k-2])
print(F)
"""
Ulempen med denne løsningen
er at det tar lenger tid og
det er vanskeligere å lese
lengden ut av koden.
"""

#Plukke ut av lister
a = [5, 10, 15, 20, 25, 30]
b = a[:4] #Plukker 4 første
c = a[3:] #Plukker fra 3 til slutt
d = a[3:5] #Plukker 3 og 4, ikke 5
e = a[:] # Kopierer listen

# Konvertere matriser, lister i lister:
A = [[1, 3, 5], [2, 4, 6]]
# Metode 1
B = []
for x, y in zip(A[0], A[1]):
    B.append()
