x0 = 0.1           # startverdi
n = 9              # antall steg

steg = (1 - x0)/n  # steglengde

i = 0              # teller hvilket steg vi er på
sum = x0
print()
print("Steg", i, ":", sum) # steg 0 er bare startverdien (vi har ikke tatt noen steg enda)
while sum < 1.0:
    i = i + 1
    sum = sum + steg # dette er en kumulativ sum (dvs. summen så langt)
    print("Steg", i, ": +", steg, "=", sum)

print()
print("Resultat: ", sum, "etter", i, "steg")
print("Forventet: 1.0 etter", n, "steg")
