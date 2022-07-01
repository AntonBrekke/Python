# Halveringsmetoden nullpunkter

f = lambda x: (x-1)*(x-0.5)*(x-2)*(x-3)*(x-4)
# f = lambda x: x**2 - 1

a = 0
b = 5

N = 100


for i in range(N):
    M = (a + b)/2
    if f(M) < 0:
        a = M

    if f(M) > 0:
        b = M

    print(M)
