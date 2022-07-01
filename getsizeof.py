import sys

n = int(input("Put n:"))
i = int(input("Put i:"))

def prod(i, n):
    p = 1
    for j in range(1, n - i + 1):
        p *= (i + j)/j
    return p

def prod1(i, n):
    p = 1
    for j in range(1, i + 1):
        p *= (n - j + 1)/j
    return p

x = prod(99940, 100000)
y = prod1(i, n)

print(sys.getsizeof(x))
print(sys.getsizeof(y))
