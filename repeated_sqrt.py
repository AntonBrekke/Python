# Exercise 2.19 from A primer:

from math import sqrt

for n in range(1, 60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
    print(f'{i} times sqrt and **2 {r}')
