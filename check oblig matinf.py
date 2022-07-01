import sys

i = int(sys.argv[1])
n = int(sys.argv[2])

from math import factorial
def prod2(i, n):
    p = factorial(n)/(factorial(i)*factorial(n-i))
    return p

def prod1(i, n):
    p = 1
    for j in range(1, i + 1):
        p *= (n - j + 1)/j
    return p

print(f"{prod1(i,n):10.20e}\t{prod2(i,n):10.20e}")
