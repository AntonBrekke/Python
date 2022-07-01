import numpy as np

a = [[1,2,3],       # Kan bygge opp som matriser (strukturmessig)
     [2,3,4],
     [3,4,5]]

print(a[0][1])
b = np.array([[1,2,3],
              [2,3,4],
              [3,4,5]])

print(b[0,1])

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] == b[i,j])
