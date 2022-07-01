import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m = 0.2
v_T = 20
D = m*g/(v_T**2)
Fnet = 0
F_D = 0
F_G = 0
alpha_grader = 35


t = np.zeros(n)
r = np.zeros((n,2))
v = np.zeros((n,2))
a = np.zeros((n,2))
