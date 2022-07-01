# Exercise A.4
import numpy as np

N = 2       # Bestemmer en N verdi for antall n
x = [0]*(N+1)       # Setter opp liste med lengde N+1 og sluttindex N
x[0] = 3.14     # Initialbetingelse

print(f"Index\t|\tNewton\t\t|\tNumpy")
print("--------|-----------------------|----------------------")

# Setter opp Newtons metode for pi, der f(x) = sin(x[n-1]) og f'(x) = cos(x[n-1])
for n in range(1, N+1):
    x[n] = x[n-1] - (np.sin(x[n-1])/np.cos(x[n-1]))

# Printer ut resultat
for n in range(len(x)):
    print(f"{n}\t|\t{x[n]:.13f}\t|\t{np.pi:.13f}")

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 40 IN2900> python finding_pi.py
Index   |       Newton          |       Numpy
--------|-----------------------|----------------------
0       |       3.1400000000000 |       3.1415926535898
1       |       3.1415926549364 |       3.1415926535898
2       |       3.1415926535898 |       3.1415926535898
"""
