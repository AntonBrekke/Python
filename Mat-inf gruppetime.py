import numpy as np
list = [2, 0, 2, -4, 10]
for i in range(5,100+1):
    x_n2 = list[i-2]
    x_n1 = list[i-1]
    x_n = -2*list[i-1] + list[i-2]
    list.append(x_n)
    #print(f'{i}\t|{x_n:6g}')

n = int(input("Input your n-value:"))
def x(n):
    return 

print(f"Numpy:{x(n)}\tLoop:{list[n]}")
