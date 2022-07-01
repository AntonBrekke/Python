import time
def load():
    s = ''
    for i in range(100):
        time.sleep(0.1)
        if len(s) < 10:
            s += '>'
        print(f'{i}{s}', end='\r')

from tqdm import tqdm, trange
for _ in trange(100):
    time.sleep(0.1)

from termcolor import colored

for i in range(100):
    time.sleep(0.1)
    if i % 2 == 0:
        print(colored('PARTY', 'red'), colored('WORLD', 'blue'), end='\r')
    else:
        print(colored('PARTY', 'blue'), colored('WORLD', 'red'), end='\r')
