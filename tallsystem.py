a = 2      # Tallverdi som oversetter
beta = 2        # Tallsystem

while a > 0:
    d = a % beta
    a = a // beta
    print(d)

# For desmialtall:
k = 100
b = 1
c = 10
for i in range(0, k):
    n = (b*beta)//c
    b = (b*beta) % c
    #print(n)
