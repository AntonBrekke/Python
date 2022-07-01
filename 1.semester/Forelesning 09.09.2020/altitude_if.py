import sys
from math import exp
try:
    h = float(sys.argv[1])
except:
    print('You failed to provide a command-line arg.!')
    exit()
p0 = 100.0; h0 = 8400
print(p0 * exp(-h/h0))
