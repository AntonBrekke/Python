import time
import multiprocessing as mp
import numpy as np

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{func.__name__} ran in {t2} seconds')
        return result
    return wrapper

# @timer
def do_something(t=1):
    time.sleep(t)

if __name__ == '__main__':
    start = time.time()
    # Gammel metode
    """
    processes = []
    for _ in range(10):
        p = mp.Process(target=do_something, args=[2])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    """
    # Ny metode med pool, gjør det samme
    with mp.Pool(6) as pool:
        pool.map(do_something, np.ones(10))

    end = time.time()
    print(end - start)
