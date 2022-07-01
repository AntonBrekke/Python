import numpy as np
import matplotlib.pyplot as plt

"""
Oppgave 1: Lager en funksjon som plotter egensirklene til en
n x n - matrise.
"""
def eigencircles(matrix):
    """
    Helt generell funksjon som plotter egensirklene
    til matrisen på det imaginære planet. Merk at koden
    er skrevet slik at matrisen som kommer inn i argumentet
    også kan ha komplekse verdier.
    """
    plt.style.use('seaborn-darkgrid')
    theta = np.linspace(0, 2*np.pi, 200)

    eigval, eigvec = np.linalg.eig(matrix)
    plt.scatter(eigval.real, eigval.imag, color='k', alpha=0.8, label='Eigenvalues', zorder=1)       # Plotter egenverdier
    print(f'\nMatrix of shape {np.shape(matrix)}\n')
    print(f'Eigenvalues: \n{eigval}\n')
    for i in range(len(matrix[:,0])):
        r = 0
        x0 = matrix[i,i].real
        y0 = matrix[i,i].imag
        for j in range(len(matrix[0,:])):
            if j != i:
                r += abs(matrix[i,j])
        x = r*np.cos(theta) + x0
        y = r*np.sin(theta) + y0
        plt.plot(x, y)       # Plotter sirkler
        print(f'circle with center {x0, y0} with radius {r}')
    plt.axis('equal')
    plt.xlabel('Re', weight='bold', fontsize=16)
    plt.ylabel('Im', weight='bold', fontsize=16)
    plt.legend(facecolor='white', frameon=True)
    plt.show()




"""
Oppgave 2: Tilpasser koden slik at den også plotter egenverdiene til matrisen.
Linjer lagt til:

eigval, eigvec = np.linalg.eig(matrix)
print(f'Eigenvalues: \n{eigval}\n')
plt.scatter(eigval.real, eigval.imag, color='k', alpha=0.8)
"""

"""
Oppgave 3:
"""
# a) Kjører matrisen A fra (1) i funksjonen fra oppgave 2
A = np.array([
[-2, 0, 0.5, 1],
[-0.25, 1, 0.25, 0],
[0, 0, 3, -1],
[0.125, 0.125, 0.25, 2]
])
eigencircles(A)

# b) Kjør matrisen B inn i funksjonen fra Oppgave 2
B = np.array([
[3, 1, 1],
[1, 0, 1],
[-1, 1, -2]
])
eigencircles(B)

# c) Kjør en selvvalgt 5 x 5 - matrise i funksjonen fra Oppgave 2
M = np.array([
[2+3j, 0.5, -0.5, 0.25, 1],
[-2, -5-3j, 0.125, -0.5, -0.1],
[-1, 0.2, 4, 0.1, -0.125],
[0.1, -0.3, 0.125, -3, 1],
[0.5, -2, 0.1, -0.5, 2-4j]
])
eigencircles(M)

# d) Bruk funksjonen fra Oppgave 2 på en 4 x 4 diagnoalmatrise
D = np.array([
[2+1j, 0, 0, 0],
[0,-3,0,0],
[0,0,-1+2j,0],
[0,0,0,4]
])
eigencircles(D)

"""
Oppgave 6: eksempel på 2 x 2-matrise som er
invertibel, men ikke diagonaldominant
"""
G = np.array([
[1,4],
[5,2]
])
eigencircles(G)

# Kjøreeksempel fra terminal:
"""

Matrix of shape (4, 4)

Eigenvalues:
[-2.03641594+0.j          0.99781164+0.j          2.51930215+0.20782755j
  2.51930215-0.20782755j]

circle with center (-2.0, 0.0) with radius 1.5
circle with center (1.0, 0.0) with radius 0.5
circle with center (3.0, 0.0) with radius 1.0
circle with center (2.0, 0.0) with radius 0.5

Matrix of shape (3, 3)

Eigenvalues:
[ 3.13263749 -2.27307286  0.14043537]

circle with center (3, 0) with radius 2
circle with center (0, 0) with radius 2
circle with center (-2, 0) with radius 2

Matrix of shape (5, 5)

Eigenvalues:
[ 1.78609231+2.83527814j  4.09263959+0.11530822j  1.97324101-3.87648964j
 -4.89509942-3.10776451j -2.95687349+0.03366779j]

circle with center (2.0, 3.0) with radius 2.25
circle with center (-5.0, -3.0) with radius 2.725
circle with center (4.0, 0.0) with radius 1.425
circle with center (-3.0, 0.0) with radius 1.525
circle with center (2.0, -4.0) with radius 3.1

Matrix of shape (4, 4)

Eigenvalues:
[ 2.+1.j -3.+0.j -1.+2.j  4.+0.j]

circle with center (2.0, 1.0) with radius 0.0
circle with center (-3.0, 0.0) with radius 0.0
circle with center (-1.0, 2.0) with radius 0.0
circle with center (4.0, 0.0) with radius 0.0

Matrix of shape (2, 2)

Eigenvalues:
[1.+4.j 1.-4.j]

circle with center (1, 0) with radius 2
circle with center (1, 0) with radius 8
"""
