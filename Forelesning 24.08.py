C = -20
while C <= 40:
    F = (9.0/5)*C + 32
    print(f"{C:3.1f}    {F:3.1}")
    C = C + 5

x = 0; y = 0
while x < 10 or y < 10:
    print(f"x+y = {x+y:d}")
    x = x + 1
    y = 2*y + x

x = 1; y = 2
print(x > y)
print(x != y and y <= x)
print(not(x < y and y <= x))
print(x < y and x > y or x != y)

a = 0
while a <= 10:
    print(f"{a}")
    a = a + 1

CListe = [-20, -15, -10, 5, 0]
for C in CListe:
    F = (9.0/5) * C + 32
    print(f"{C:3.1f}  {F:3.1f}")

    """
    NB: Øv på lister (for, while) og loops 
    """                                                                                                                                                                                           
