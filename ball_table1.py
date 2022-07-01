
v0 = 18.5   # Starthastighet
g = 9.81    # Tyngdeakselerasjon
n = 10      # Ønsket antall t-intervaller

a = 0       # Nedre grense for t
b = 2*v0/g # Øvre grense for t
h = (b - a)/n   # Lengde på hvert delintervall

# a) Løsning basert på for-løkke:
print("  t     |   y(t)")
print("________________")
for i in range(n + 1):
    t = a + i*h
    y = v0*t - 0.5*g*t**2
    print(f"{t:6.2f}\t|{y:6.2f}")

# b) Løsning basert på while-løkke:
print("")
print("  t     |   y(t)")
print("________________")
t = 0
eps = 1e-6
while t <= b + eps:
    y = v0*t - 0.5*g*t**2
    print(f"{t:6.2f}\t|{y:6.2f}")
    t += h  # t = t + h
