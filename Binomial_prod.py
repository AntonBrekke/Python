def prod1(i, n):
    p = 1
    for j in range(1, n - i + 1):
        p *= (i + j)/j
    return p

print(prod1(99940, 100000))
