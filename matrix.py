import numpy as np
"""
A = [[1,2,3],
    [2,3,4],
    [5,6,7]]
print(A)

A = np.array([[2,3,4], [3,4,5]])
print(A)
print(A[1,:]) # [3 4 5]
print(A[:,1]) # [2 3]
print(A[1,:][1]) # 4
"""
"""
B = np.array([[1,2], [3,4]])
C = np.array([[1], [2]])
D = np.array([[1,2]])
print(f'{B}\n\n{C}\n\n{D}\n\n')
print(B.dot(C),'\n') # Matrisemultiplikasjon
print(np.dot(B,C),'\n') # Annen måte å multiplisere
print(B*C,'\n') # Ganger elementene i matrisen sammen, ikke matrisemultiplikasjon
print(B.transpose(),'\n') # transponerer matrise
print(np.linalg.inv(B),'\n') # Inverserer matrise
print(B.dot(np.linalg.inv(B)),'\n') # Sjekk avrundingsfeil i identitetsmatrise
print(np.linalg.norm(B))
"""

# løse likningsystem:

"""
x + 2y + 3z = 6
y + 2z = 2
x + 6y + 2z = 5
"""
"""
M1 = np.array([[1,2,3], [0,1,2], [1,6,2]])
M2 = np.array([['x'], ['y'], ['z']])
M3 = np.array([[6], [2], [5]])
ans = np.linalg.inv(M1).dot(M3)
print(ans)
"""
"""vx = np.array([(1,1),(1,2)])
vy = np.array([(2,3),(4,3)])
print(vx*vy)        # Når man regner skalarprodukter komponentshvis og sorterer dem i en array (summen av elementene i radene er skalarproduktet)
print(np.dot(vx,vy))    # For matrisemultiplikasjon
# Kan finne direkte skalarprodukt ved matrisemultiplikasjon:
vx = np.array((1,1))
vy = np.array((2,3))
print(np.dot(vx,vy))

vx = np.array([(1,1),(1,2)])
vy = np.array([(2,3),(4,3)])
scalar_sum = []
a = vx*vy
for i in range(len(vx)):
    scalar_sum.append(sum(a[i]))

print(scalar_sum)
"""

u = np.array([[1,2,3], [1,2,3]])
v = np.array([3,2,1])
print(np.shape(u))
print(u)
print(u*v)
print(np.dot(u,v))
print('\n')
u = np.array([[1],[2],[3]])
v = np.array([[3],[2],[1]])
print(u*v)
print(np.dot(u,v.T))
