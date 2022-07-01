import time

# Funksjon for å slå sammen dictionaries
def merge(a, b):
    return {**a, **b}

def cache(f):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        infile = open('cache_log', 'r+')
        infile_dict = {}
        for line in infile:
            infile_dict = eval(line.strip('\n'))
            # print(infile_dict)
            # print(args in infile_dict)
        if args in infile_dict:
            print('Return from cache_log')
            return infile_dict[args]
        else:
            print('Calculate...')
            cache_dict[args] = f(*args, **kwargs)
            infile.write(f'{merge(infile_dict, cache_dict)}\n')
            return f(*args, **kwargs)

    return wrapper


@cache
def add(*args):
    time.sleep(2)
    return sum(args)

@cache
def multiply(*args):
    time.sleep(2)
    val = 1
    for n in args:
        val *= n
    return val

def make_cache_log_example():
    for i in range(1,11):
        for j in range(1,11):
            add(i,j)
            multiply(i,j)
