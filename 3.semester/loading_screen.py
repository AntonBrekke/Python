import time
from tqdm import tqdm, trange
from termcolor import colored

def illustrate():
    n = 50
    m = round(n / 7 + 0.4)
    pbar = trange(n, desc=colored('Loop 1', 'red'))
    clr = ['black']*m + ['red']*m + ['magenta']*m + ['blue']*m + ['cyan']*m + ['yellow']*m + ['green']*m
    for i in pbar:
        pbar.colour = clr[i]
        # print('')
        for j in trange(5, desc='Loop 2', leave=False):
            for k in trange(5, desc='Loop 3', leave=False, colour='white'):
                time.sleep(0.01)

def load():
    n = 10000
    p1 = 0.25
    p2 = 0.5
    m1 = round(n*p1)
    m2 = round(n*p2)
    m3 = round(n*(1-p1-p2))
    s = 0
    pbar = trange(n, desc=colored('Loop 1', 'red'))
    clr = ['red']*m1 + ['yellow']*m2 + ['green']*m3
    for i in pbar:
        pbar.colour = clr[i]
        for _ in range(n):
            pass

load()
