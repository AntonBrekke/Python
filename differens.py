

N = 10000
x = [0]*(N+1)
x[0] = 2
x[1] = 8/3

for n in range(N-1):
    x[n+2] = (7*x[n+1] - 2*x[n] - 6) / 3

for n in range(N):
    print(x[n])
