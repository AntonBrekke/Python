import numpy as np

P = np.array([[2/3, 1/np.sqrt(5), -4/np.sqrt(45)],
              [-1/3, 2/np.sqrt(5), 2/np.sqrt(45)],
              [2/3, 0, 5/np.sqrt(45)]])

D = np.array([[6,0,0],
              [0, -3, 0],
              [0, 0, -3]])

M = np.dot(P, np.dot(D, P.T))
print(M)
# var riktig!
