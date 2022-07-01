def table(k):
    n = 5
    primelist = [2,3,5,7,11]
    print(primelist)
    d = primelist
    for i in range(1, k):
        for j in range(n-i):
            d[j] = abs(d[j+1] - d[j])
        print(d[:n-i])

print(table(2))
