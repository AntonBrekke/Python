print("")
from math import sqrt
a = []              # Liste for bevegelsesmengde
b = []              # Liste for prosent lyshastighet
r = []              # Liste for relativistisk bevegelsesmengde
c = 3.0*10.0**8     #Lyshastigheten
v = 0.1*c
m = 1200.0
l = 1/sqrt(1 - (v/c)**2)    #Lorentzfaktoren

print("__________________________________________")
print("|Speed  |   Momentum    |   Relativistic |\n|       |\t\t|   momentum\t |")
print("|_______|_______________|________________|")

for i in range(1, 10):
    p = m*v           # Momentum
    p_r = m*v*l     # Relativistic momentum
    b.append(0.1*i)
    a.append(p)
    r.append(p_r)
    #input()
    print(f"| {b[i-1]:.1f}c  |   {a[i-1]:.4e}  |   {r[i-1]:.4e}   |") # Bare pynting for å få fin print
    v = (i + 1)*v
print("------------------------------------------")
#Kjøreeksempel fra terminal:
"""
PS C:\Desktop\Python> python relativistic_momentum.py

__________________________________________
|Speed  |   Momentum    |   Relativistic |
|       |               |   momentum     |
|_______|_______________|________________|
| 0.1c  |   3.6000e+10  |   3.6181e+10   |
| 0.2c  |   7.2000e+10  |   7.2363e+10   |
| 0.3c  |   2.1600e+11  |   2.1709e+11   |
| 0.4c  |   8.6400e+11  |   8.6835e+11   |
| 0.5c  |   4.3200e+12  |   4.3418e+12   |
| 0.6c  |   2.5920e+13  |   2.6051e+13   |
| 0.7c  |   1.8144e+14  |   1.8235e+14   |
| 0.8c  |   1.4515e+15  |   1.4588e+15   |
| 0.9c  |   1.3064e+16  |   1.3129e+16   |
------------------------------------------
"""
