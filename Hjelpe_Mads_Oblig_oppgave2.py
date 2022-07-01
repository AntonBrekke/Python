import numpy as np

N = int(input("Put integer here:"))
print("")
x = [0]*(N + 1)
x[0] = 1
x[1] = (2 - np.sqrt(5))

print("n-values\tLoop\t\t\tFormula")
for n in range(2, N + 1):
    x[n] = 4*x[n-1] + x[n-2]
    x_n = (2 - np.sqrt(5))**n
    print(f'{n}\t|\t{x[n]:10.6g}\t|\t{x_n:6g}')
