
import numpy as np

A = np.array([[1,2,3], [6,5,4], [1,1,2]])
B = [[1,2,3], [6,5,4], [1,1,2]]
C = np.array([[1,2,3], [6,5,4], [1,1,2]])
print(A[2,:] == C[2])

if all(A[2] == C[0]):       # Any eller all fordi det returneres en liste ned boolske uttrykk
    print('all')
elif any(A[2] == C[0]):
    print('not all, but some')

# Triks: kan pakke inn en konstant som en funksjon
# slik at man kan bruke funksjonskall i koden selv
# om beta er en konstant.

class Beta:
    def __init__(self, beta):
        if callable(beta):
            self.beta = beta
        elif isinstance(beta, (float, int)):
            self.beta = lambda t: beta

f = lambda t: 2*t
function = Beta(f)
print(function.beta(2))

# Må ikke foregå i en klasse
a = lambda t: 0.5*t
if callable(a):
    f = a
elif isinstance(a, (float, int)):
    f = lambda t: a

print(f(2))     # Dette kallet funker alltid selv om f er en konstant, fordi den pakkes inn i en funksjon
