# Exercise A.14
import numpy as np

def sin_Taylor(x,n):
    a = [0]*(n+2); a[0] = x
    s = [0]*(n+2)
    for n in range(1, n+1):
        s[n] = s[n-1] + a[n-1]
        a[n] = -(x**2)*(a[n-1])/((2*n+1)*2*n)
    print(s)
    return s[n+1], abs(a[n+1])

a = sin_Taylor(np.pi/2, 2)
print(a)
