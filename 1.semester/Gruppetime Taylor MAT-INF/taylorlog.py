from numpy import exp
from math import frexp

# Calculates one Taylor expansion term
def taylorterm(x, lna, i):
    if i == 0:
        return lna
    else:
        a = exp(lna)
        return -(1/i)*(1 - x/a)**i

# This function simply adds all the Taylor terms together (also returns the error term)
def taylor(x, lna, n):
    sum = 0.0
    for i in range(n + 1):
        sum += taylorterm(x, lna, i)
    return sum

# Calculates the error term of the Taylor polynomial
def errorterm(x, lna, n):
    a = exp(lna)
    xi = min(a,x)
    Rn = abs(((x-a)**(n+1) / (n+1)) * (1 / xi**(n+1)))
    return Rn

# Your own logarithm function, using Taylor polynomials
def taylorlog(x, lna, n):
    m, e = frexp(x)
    log2 = 0.6931471805599453 # ln(2) with machine accuracy
    lnx = e*log2 - taylor(m, lna, n)
    return lnx
