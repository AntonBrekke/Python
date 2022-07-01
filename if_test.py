# Code and if test
import umpy as np
def Hv(x):
    return np.where(x < 0, 0.0, 1.0)

# More generally:
"""
def f(x):
    if "condition":
        x = <expression>
    else:
        x = <expression2>
    return x

def f_vectorized(x):
    x1 = <expression1>
    x2 = <expression2>
    r = np.where(condiotion, x1, x2)
    return r
"""
