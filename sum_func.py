# Exercise 3.7
#a)
def sum_1k(M):
    s = 0
    for k in range(1, M+1):
        s += 1/k

    return s

#print(sum_1k(3))

#b)

def test_sum_1k():
    expected = 11/6
    computed = sum_1k(3)

    tol = 1e-10
    success = abs(expected - computed) < tol
    msg = f'Expected {expected}, got {computed}'
    assert success, msg

test_sum_1k()

"""
Terminal> pyton sum_func.py
"""
