import numpy as np


corners = [(35,160,70,170),(35,85,70,100),(35,50,70,60)]
for C in corners:
    x1, x2 = C[0], C[2]
    y1, y2 = C[1], C[3]
    C1 = (x1, x2, y1, y1)
    C2 = (x2, x2, y1, y2)
    C3 = (x2, x1, y2, y2)
    C4 = (x1, x1, y2, y1)


A = np.array([[C1, C2], [C3, C4]])
print(A)
