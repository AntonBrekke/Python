# Exercise 7.12 Langtangen
class Sum:
    def __init__(self, f, M, N):
        self.term = f
        self.M = M
        self.N = N

    def __call__(self, x):
        s = 0
        for k in range(self.M, self.N+1):
            s += self.term(k, x)
        return s

    # def term(self, k, x):
        # return self.f(k, x)

# a)
def term(k, x):
    return (-x)**k

S = Sum(term, M=0, N=3)

x = 0.5

print(S(x))
print(S.term(k=4, x=x))

# b)
def test_Sum():
    def f(k,x):
        return (-x)**k

    M = 0
    N = 3
    S = Sum(f, M, N)

    tol = 1e-10
    x = 0.5
    computed = S(x)
    expected = 1 - x + x**2 - x**3
    success = abs(computed - expected) < tol
    assert success

    computed = S.term(4,x)
    expected = (-x)**4
    success = abs(computed - expected) < tol
    assert success

test_Sum()
