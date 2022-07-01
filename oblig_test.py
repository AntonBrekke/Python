import numpy as np
list2 = [1, 2]
for i in range(2,100+1):
    x_n2 = list2[i-2]
    x_n1 = list2[i-1]
    x_n = 4*x_n1 + x_n2
    list2.append(x_n)
    print(f'{i}\t|{x_n:6g}')
