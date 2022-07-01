# Definere en funksjon:
def skrivut():
    print("Pi is approximately 3.1415926")

skrivut()

def f(x):
    return x**2

x = 2
y = f(x)
print(y)

# Mer konkrete eksempler:
def printsnitt(a):
    # Vi regner først ut summen av alle elementene i a:
    total = 0
    for e in a:
        total = total + e
    # Vi deler på antall elementer:
    snittverdi = total/len(a)
    # Skriver ut svaret:
    print(f"Gjennomsnittsverdien er {snittverdi:g}")

# Funksjon som skriver ut en melding:
def skrivMelding(navn, melding):
    s = f"Gratulerer {navn}, du har {melding}!"
    print(s)

# Bruk funksjonen:
skrivMelding("Mia", "vunnet 100 kroner")
skrivMelding("Jon", "bestått eksamen")

# Funksjon som regner ut indre produkt:
def innerprod(x, y):
    verdi = 0
    for i in range(len(x)):
        verdi += x[i]*y[i]
    return verdi
x = [1, 2, 3, 4]
y = [0, 1, 4, 2]
svar = innerprod(x, y)
print(f"Indreproduktet av x og y er {svar:5.2f}")

# Funksjon som regner n!:
def factorial(n):
    v = 1
    for i in range(1, n + 1):
        v = v*i
    return v
# Prøv funksjonen:
for n in range(1, 8):
    print(f"Fakultet av {n} er {factorial(n)}")

"""
Globale og lokale variabler:
Variabler definert utenfor funksjoner
kalles globale variabler, og er synlige
inni funksjoner.
"""
def skrivut():
    print(f"aplha = { alpha:g}")

alpha = 10          # Global variabel

"""
Variabler definert inni funksjoner
kalles lokale variabler. De er kun synlige
inne i funksjonen. Disse eksisterer kun
når funksjonen utføres, og ikke på utsiden.
"""
def skrivut():
    alpha = 0.6323      # Lokal variabel
    print(alpha)
skrivut()       # Utskrift: 0.6323

"""
Vær varsom hvis en global og lokal
variabel har samme navn. Bare den lokale
vaiabelen blir da synlig i funksjonen.
"""
def g(t):
    alpha = 1.0
    return alpha*t
alpha = 100000      # Global variabel
print(g(2))         # Utskrift: 2.0

# Et litt større eksempel
def x(n):
    s = 0
    for i in range(1, n + 1):
        s += (1/i)*(5/6)**i     # Sum mot ln(6)
    return s
print(x(10))

# Utvidelse av x(n):
from math import log

def x(n):
    s = 0
    for i in range(1, n + 1):
        s += (1/i)/(5/6)**i
    feil1 = log(6) - s
    feil2 = (1/(n + 1))/(5/6)**(n + 1)
    return s, feil1, feil2
# Typisk kall:
value, feil1, feil2 = x(100)

"""
Når vi definerer funksjner kan
vi oopgi default-verdier
for argumentene
"""
def skrivut(x, y, z=0, t=99):
    print(x, y, z, t)
# Benytt default-verdiene for z og t:
skrivut("Hei", 3)
# Benytt defualt-verdien for t:
skrivut("Hei", 3, 2)

# Hva skrives ut her?:
def skrivut(k):
    x = 2*k
    print(f"x = {x:g}")
x = 5   # Global
print(f"x = {x:g}") # Bruker global
skrivut(5)          # Bruker lokal def
print(f"x = {x:g}") # Bruker fortsatt global

"""
I Python kan argumenter til en funksjon
selv være funksjoner.
"""
# Eksempel:
def diff2(f, x, h=1E-6):
    r = (f(x-h) - 2*f(x) + f(x+h))/h*h
    return r
"""
Første argument til diff2(.) er her den
funksjonen vi skal finne den annenderiverte
til.
"""

def diff2(f, x, h=1E-6):
    r = (f(x-h) - 2*f(x) + f(x+h))/h*h
    return r

def g(t):
    return t**(-6)

# Beregn g''(t) for mindre og mindre verdier av h:
for k in range(1, 14):
    h = 10**(-k)
    print(f"h = {h:.0e}: {diff2(g, 1, h):.5f}")
# Når vi regner numerisk må man være obs på avrundingsfeil ved store eller små verdier:

"""
Noen ganger trenger vi å lage funksjoner
som bare beregner enkle uttrykk. Da er
lambda-funksjoner ofte et nyttig alternativ
til vanklige funksjonsdefinisjoner.
"""
# Eksempel:
def f(x, y):
    return x**2 - y**2
# Kan defineres på én linje med lambda-konstruksjonen:
f = lambda x, y: x**2 - y**2
"""
Lambdafunksjoner kan brukes direkte som
argumenter i funksjoner:
"""
z = g(lambda x, y: x**2 - y**2, 4)


"""
If-tester:
If-tester gjør det mulig å lage forgreninger
i programkjøringen, dvs at ulike handlinger utføres
under ulike betingelser. Eksempel:
"""
from math import sin, pi

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0

# Funksjon som teller hvor mange ganger s forekommer i a:
def count(s, a):
    cnt = 0
    for e in a:
        if e == s:
            cnt += 1
    return cnt
# Eksempel på bruk:
count([5.3], [2.2, 6.6, 2.5, 5.3, 8.9, 5.2])
count('Anna', ['Anna','Ola','Jens','Karianne'])
count([1, 2], [1, 5, [1, 2], [1,2], 3])
