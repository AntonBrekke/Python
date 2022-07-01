import numpy as np

n = 100
x = [0]*(n+1); x[0] = 0; x[1] = 1

for n in range(2,n+1):
    x[n] = x[n-1] + x[n-2]
print(f"{n}, {x[n]:.20g}")

def Fib(n):
    return (1/np.sqrt(5)) * ((1+np.sqrt(5))/(2))**n - (1/np.sqrt(5)) * ((1-np.sqrt(5))/(2))**n

print("")
y = Fib(n)
print(y)

print(abs(y-x[n]))
