from numba import njit
import numpy as np
import matplotlib.pyplot as plt
import time
"""
Dette er en liten kode, men her ser vi at numba kjører denne omtrent 5x
fortere. På større koder sparer man enda mer, bare tenk deg det!
"""


start = time.time()
@njit(cache=True)
def f():
    a = []
    for i in range(10000000):
        a.append(i**2)
    return a

f()
end = time.time()
print(end-start)
