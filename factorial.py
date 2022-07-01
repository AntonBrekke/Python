from math import factorial
import random

# def myfactorial(n):
#     return factorial(n)
#
# k = random.randint(1, 10)
# # print(myfactorial(k))
#
#
# def ownFactorial(n):
#     p = 1
#     for j in range(2, n+1):
#         p *= j
#     return p
#
#
# # print(ownFactorial(6), myfactorial(6)
#
# def BinomialCoeff(n, i):
#     return ownFactorial(n) / (ownFactorial(i) * ownFactorial(n-i))
#
# # print(BinomialCoeff(7,3))


class BinomialTheroem:
    def ownFactorial(self, j):
        p = 1
        for i in range(2, j+1):
            p *= i
        return p

    def BinomialCoeff(self, n, i):
        return self.ownFactorial(n) / (self.ownFactorial(n - i) * self.ownFactorial(i))

    def orders(self, n):
        s = ''
        self.n = n
        for i in range(n+1):
            s += f'{self.BinomialCoeff(n, i)}*a^{n-i} * b^{i}'
            if i != n:
                s += ' + '
        return s

    def evaluate(self, a):
        s = ''
        for i in range(self.n+1):
            s += f'{self.BinomialCoeff(self.n, i)*a**i}*x^{self.n-i}'
            if i != self.n:
                s += ' + '
        return s

a = BinomialTheroem()
a.orders(4)
print(a.evaluate(1))
