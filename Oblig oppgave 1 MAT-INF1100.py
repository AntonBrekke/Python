# Oppgave 1
'''
Annen ordens differens-likning " x_n+2 - 4*x_n+1 - x_n = 0 ".
Skriver om x_n+2 - x_n+1 - x_n = 0 til x_n = 4*x_n-1 + x_n-2.
Starter index på 2 slik at: x_2 = 4*x_1 + x_0, der x_1 og x_0 er gitte verdier.
Regner så x_3 = 4*x_2 + x_1, som gir en "dominoeffekt" som kan løses med en løkke.
Skriver til n = 100 og x_n-2 som x_n2, x_n-1 som x_n1 og x_n som x_n.
'''
#a)
import numpy as np
list = [1, 1]
for i in range(2,100+1):
    x_n2 = list[i-2]
    x_n1 = list[i-1]
    x_n = 4*list[i-1] + list[i-2]
    list.append(x_n)
    #print(f'{i}\t|{x_n:6g}')

print("")
# Mindre "sofistikert"(enklere) kode:
"""
from math import sqrt
xpp = 1
xp = 2 - sqrt(5)
for i in range(100):
    x = 4*xp + xpp
    xpp = xp
    xp = x
    print(x)

"""

#b)
import numpy as np
list2 = [1, 2.0 - np.sqrt(5)]
for i in range(2,100+1):
    x_n2 = list2[i-2]
    x_n1 = list2[i-1]
    x_n = 4*x_n1 + x_n2
    list2.append(x_n)
    print(f'{i}\t|{x_n:6g}')
# d)
"""
x_n kan skrives som x_n = (2 - sqrt(5))**n for x_0 = 1 og x_1 = 2 - sqrt(5).
"""
#n = int(input("Input your n-value:"))
def x(n):
    return (2 - np.sqrt(5))**n

#print(f"Numpy:{x(n)}\tLoop:{list2[n]}")

# Sammenlikne verdier:
for n in range(2,101):
    x_n = (2 - np.sqrt(5))**n
    #print(f"{n}|{list2[n]}\t|{x_n}")
