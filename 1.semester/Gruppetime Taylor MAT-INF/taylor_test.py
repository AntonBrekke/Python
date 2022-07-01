import matplotlib.pyplot as plt
from numpy import abs, linspace, exp
from taylorlog import taylor, errorterm

# Disse kan dere endre på
lna = 2
n = 10
xmin = 1
xmax = 14

# But don't change anything else
xs = linspace(xmin, xmax, 10000)

errterms = []
for x in xs:
    y_taylor = taylor(x, lna, n)
    errterm = errorterm(x, lna, n)
    errterms.append(errterm)

plt.plot(xs, errterms)
plt.axhline(10**-10, linestyle="--", color="black")
plt.xlabel(r"$x$")
plt.ylabel("Error term")
plt.yscale("log")
# plt.axis([xmin, xmax, min(errterms), 10**11])
plt.title(r"$n=$" + str(n) + r", $\ln{(a)}=$" + str(lna) + r", $a=$" + str(round(exp(lna), 2)))
plt.savefig("n" + str(n) + "_lna" + str(lna) + ".png")
plt.show()
