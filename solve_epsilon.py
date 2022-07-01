from sympy import symbols, solve
import numpy as np

list = [1, 2.0 - np.sqrt(5)]
for i in range(2,100+1):
    x_n2 = list[i-2]
    x_n1 = list[i-1]
    x_n = 4*x_n1 + x_n2
    list.append(x_n)

epsilon = symbols('epsilon')
# For n = 13:
for i in range(2,101):
    expr = (epsilon/(2*np.sqrt(5)))*(2 + np.sqrt(5))**i + ((2*np.sqrt(5) - epsilon)/(2*np.sqrt(5)))*(2 - np.sqrt(5))**i - list[i]
    sol = solve(expr)

    print(sol)
# n = 100 -> epsilon = -1.08642304073650e-16
