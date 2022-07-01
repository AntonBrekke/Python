import time

def timer(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = f(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{f.__name__} ran in {t2} seconds')
        return result

    return wrapper

def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            # print('Return from cache')
            return cache_dict[args]
        else:
            # print('Calculate...')
            cache_dict[args] = func(*args, **kwargs)
            return func(*args, **kwargs)

    return wrapper

@cache
def multiply(*args):
    time.sleep(2)
    val = 1
    for n in args:
        val *= n
    return val

@cache
def add(*args):
    time.sleep(2)
    return sum(args)

# Her er den veldig hjelpsom
@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@timer
def loop_fib():
    for i in range(100):
        print(i, fib(i))
    print('done')

loop_fib()
