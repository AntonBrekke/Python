import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd


def find_n(lmbda, B_list=[], C_list=[]):
    ns = 0
    for B, C in zip(B_list, C_list):
        ns += lmbda**2 * B / (lmbda**2 - C)
    n = np.sqrt(ns + 1)
    return n

# Konstanter gitt for bølgelengder i mikrom
B1 = 1.03961212
B2 = 0.231792344
B3 = 1.01046945
C1 = 0.00600069867
C2 = 0.0200179144
C3 = 103.560653

lmbda = 520e-3     # mikrom, 520nm

n = find_n(lmbda, [B1, B2, B3], [C1, C2, C3])
print(f'\nn: {n}')

x = 33 / 2      # mm
d = 0.4      # mm

def find_R(x, d):
    R = (x**2 + d**2) / (2*d)
    return R

R = find_R(x, d)
print(f'\nR: {R} mm')

R = 280     # mm
# Bruker n som jeg fant istad

def find_f(R, n):
    f = R / (2*(n-1))
    return f

f = find_f(R, n)
print(f'\nf: {f}')
