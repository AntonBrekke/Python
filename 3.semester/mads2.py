import numpy as np
import time
from termcolor import cprint

def write_mads(t):
    print('')
    name = 'Mads Balto'
    a = ''
    color = ['red', 'magenta', 'blue', 'green', 'white', 'yellow', 'cyan', 'red', 'blue', 'white']
    for n, i in enumerate(name):
        a += i
        cprint(a, color[n], end='\r', attrs=['bold'])
        if not i == ' ':
            time.sleep(t)
    print(name)

write_mads(0.3)
