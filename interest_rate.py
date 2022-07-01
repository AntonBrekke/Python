"""
Problem 2.2. Growth of a bank
deposit Let r be a bank’s interest
 rate in percent per year. An initial
 amount P will then grow to
"""

P = 1000
r = 5
n = 3

A = int(P*(1+r/100)**n)
print(f"After {n} years the amount have grown to {A} euros.")

#Kjøretest fra terminal:
"""
PS C:\Desktop\python> python interest_rate.py
After 3 years the amount have grown to 1157 euros.
"""
