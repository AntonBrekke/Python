import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

q = 1.0
Q1 = 1.0
Q2 = 1.0
a = 1.0
epsilon_0 = sc.epsilon_0
R1 = np.array([-a,0,0])
R2 = np.array([a,0,0])

F1 = q*Q1 / (4*np.pi*epsilon_0) * R1 / np.linalg.norm(R1)**3
F2 = q*Q2 / (4*np.pi*epsilon_0) * R2 / np.linalg.norm(R2)**3
print(F1)
print(F2)
print(F1 + F2)
