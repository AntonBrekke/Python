"""
Problem 2.3. Population growth
"""
from math import e

B = 50000  #Bæreevne
k = 0.2
N_0 = 5000 #N når t = 0

C = (B/N_0) - 1
print(f"When t = 0, C = {C}")

t = 24 #gitt i timer
N = B/(1 + C*e**(-k*t))
print(f"When t = 24 hours, N = {N:g}")

#Kjøretest population.py
"""
PS C:\Desktop\python> python population.py
When t = 0, C = 9.0
When t = 24 hours, N = 46552
"""
