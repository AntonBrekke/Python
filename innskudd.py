## Les Verdier fra bruker
x0 = float(input("Startbeløp i banken:"))
p = float(input("Rente (%):"))
N = int(input("Antall år:"))

x = [0]*(N + 1)
x[0] = x0

for n in range(1, N + 1):
    x[n] = (1 + (p/100))*x[n-1]

print("")
print("År   Beløp")

for n in range(N+1):
    print(f"{n:3d}  {x[n]:7.2f}")
