P = 500
r = 5.0
n = 0
while n <= 10:
    A = P * (1+r/100)**n
    print(n, A)
    n = n + 1

x = 0; y = 1.2
print(x >= 0 and y < 1)
print(x >= 0 or y < 1)
print(x > 0 or y > 1)
print(x > 0 or not y > 1)
print(-1 < x <= 0) # same as -1 < x and x <= 0
print(not (x > 0 or y > 0))
