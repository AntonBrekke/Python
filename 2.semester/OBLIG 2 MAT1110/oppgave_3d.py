import numpy as np

P = np.array([ [1, 0.3, 0, 0, 0],
               [0, 0.5, 0.5, 0,0],
               [0, 0.2, 0.3, 0.2, 0],
               [0, 0, 0.2, 0.4, 0],
               [0, 0, 0, 0.4, 1] ])

b = np.array([ [2.070],
               [2.055],
               [1.293],
               [0.942],
               [3.640] ])

P3 = np.dot(np.dot(P,P),P)
epsilon = 1e-14
eps_vec = epsilon*np.ones([5,1])

# Matrise P^n
def Pn(n):
    PN = P
    for i in range(n-1):
        PN = np.dot(P,PN)
    return PN

# Tester potenser av P
for n in range(4):
    # Tester alle kombinasjoner
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for q in range(11):
                    for m in range(11):
                        x = np.array([ [i],
                                       [j],
                                       [k],
                                       [q],
                                       [m] ])
                        test = np.dot(Pn(n), x)
                        comparison = abs(test - b)
                        bool = comparison < eps_vec
                        if bool.all():
                            print(f'x = {[x[t][0] for t in range(len(x))]}')
                            print(f'P^n = P^{n}')
# Fra terminalen:
"""
x = [0, 2, 3, 5, 0]
P^n = P^3
"""
