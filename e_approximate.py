import numpy as np

class e:
    def factorial(self, i):
        f = 1
        for j in range(2, i+1):     # i <= 1 returnerer ingenting, så f = 1 ( [j for j in range(2, i+1 <= 2)] ) -> [], f = 1 returneres
            f *= j
        return f

    def approx_e(self, n):
        s = 0
        for i in range(n + 1):
            s += 1/self.factorial(i)
        return s


e = e()
print(e.approx_e(10000))
print(np.exp(1))
