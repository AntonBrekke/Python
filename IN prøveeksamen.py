def count(dna, base):
    i = 0
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1
    return i


# print(count('GATA', ''))


# a = [[4,5], [0,1], 2, [2,0.5], 4, 3, [5,6,7]]
# b =[]
# for e in a:
#     s = 0
#     for number in e:
#         s += number
#     b.append(s)
#
# print(b)


def test(a,b,c, d=10):
    return a, b, c, d

# print(test(1, 2, 4, 11))

"""
# DEL A:

import sys
from math import *

try:
    formula = sys.argv[1]
    x = [float(x_) for x_ in sys.argv[2:]]
except IndexError:
    print('Missing command line argument')
    exit()



# DEL B:

code = f"""
"""
def f(x):
    return {formula}
"""
"""


#  DEL C:
try:
    exec(code)
except:
    print('Something wrong in formula')
    exit()



# DEL D:

for x_ in x:
    print(f(x_),end=' ')
"""

"""
stars_data = {}

with open('IN prøveeksamen.txt') as infile:
    infile.readline()

    for line in infile:
        w = line.split()
        data = {'dist':float(w[1]), 'bright':float(w[2]), 'lum':float(w[3])}
        stars_data[w[0]] = data



print(stars_data['Sirius_A'])
"""
"""
def f(x,y):
    answer = []
    for y in y:
        if y <= 0:
            ans = 4*x**3*y-2*x*y
            answer.append(ans)
        if y > 0:
            ans = 4*x**3*y+2*x*y
            answer.append(ans)
    return answer


print(f(1, [1,2,3]))


import numpy as np
def midpoint(f, x, h):
    derivative = (f(x+h) - f(x-h))/(2*h)
    return f(x), derivative

# print(midpoint(lambda x: np.cos(x), 0, 0.001))

import numpy as np
def cos_approx(x,n):
    s = 0
    for k in range(n+1):
        s += (-1)**k * (x**(2*k))/(np.math.factorial(2*k))
    return s

print(cos_approx(0,1))
"""


"""
constants = {}
with open('IN prøveeksamen.txt','r') as infile:
    infile.readline()
    infile.readline()
    for line in infile:
        words = line.split()
        constants[' '.join(words[0:2])] = [float(words[2]), words[3]]

print(constants)
"""

"""
def poly_eval(p, x):
    poly = 0
    for key in p:
       poly += p[key]*x**key
    return poly

print(poly_eval({0:1, 2:-2, 4:3, 5:1}, 1))

def poly_diff(p, x):
    derivative = 0
    for key in p:
        derivative += key*p[key]*x**(key-1)
    return derivative

print(poly_diff({0:1, 2:-2, 4:3, 5:1}, 0.5))
"""
"""
def min_max(a):
    min = max = a[0]
    for i in a[1:]:
        if i > max:
            max = i
        elif i < min:
            min = i

    return max, min

print(min_max([0,1,4,6,7,3,2,5,6,7,-1,-6,-18,-2,3,6,7,20,2]))


class F:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self,x):
       return self.a*x**2 + self.b*x + self.c

    def __str__(self):
        return f'{self.a}*x^2 + {self.b}*x + {self.c}'

f = F(a=1.0, b=2.0, c=3.0)
x = 2.0
print(f(x))
print(f)
"""

import sys
n = int(sys.argv[1])

def is_prime(n):
    prime_count = 0
    for b in range(2, n):
        if n % b == 0:
            prime_count += 1
    if prime_count == 0:
        return True
    else:
        return False

print(is_prime(n))
