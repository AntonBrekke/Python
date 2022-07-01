# Stern-følgen (Skriver ut alle positive rasjonale tall uten at de gjentar seg)
def stern(N):
    x = [0]*(2*N)   # x[0], x[1], ..., x[2N-1]
    x[0] = 0
    x[1] = 1
    for n in range(1,N):
        x[2*n] = x[n]
        x[2*n+1] = x[n] + x[n-1]
    # n = 1: x[2], x[3]
    # n = N-1: x[2*(N-1)] = x[2*N-2]
    return x

def printRationals(N):
    x = stern(N)
    for n in range(2*N-1):
        print(f"{x[n]} / {x[n+1]}")
    # n = 0: x[0] / x[1]
    # n = 2*N-2: x[2*N-2] / x[2*N-1]

N = int(input("Skriv N:"))
printRationals(N)
