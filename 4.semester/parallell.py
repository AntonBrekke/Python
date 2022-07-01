import multiprocessing as mp
import numpy as np
import time
import os

def square(x):
    time.sleep(1)
    return x**2

foo = np.linspace(0, 1, 10)

if __name__ == '__main__':
    print(os.cpu_count())
    # Parallellisert
    t1 = time.time()
    with mp.Pool(5) as pool:
        pool.map(square, foo)
    t2 = time.time()
    print(t2 - t1)

    # Ikke parallellisert
    t1 = time.time()
    result = []
    for n in foo:
        result.append(square(n))
    # print(result)
    t2 = time.time()
    print(t2 - t1)
