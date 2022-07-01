from numpy import log, exp
from taylorlog import taylorlog, errorterm

# Feel free to change these
lna = 2
n = 10

# But don't change anything else
xs = [0.001, 0.1, 10, 1000]
for x in xs:
    logx = log(x)
    taylorlogx = taylorlog(x, lna, n)
    relerr = abs((taylorlogx - logx) / logx)
    print()
    print("x =", x)
    print("---")
    print("log:           ", logx)
    print("taylorlog:     ", taylorlogx)
    print("relative error:", relerr)
print()
print("ln(a) =", lna)
print("a     =", exp(lna))
print("n     =", n)
print(log(2))
