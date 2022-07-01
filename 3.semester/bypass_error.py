import numpy as np

def div_zero(a):
    try:
        s = a/0
    except (RuntimeWarning, ZeroDivisionError):
        pass
    return s

a = np.linspace(0, 100, 100)
a = 3
div_zero(a)
