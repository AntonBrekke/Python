import numpy as np

"""
Kode for Gram-Schmidt prossessen som lager
en ortogonal basis ut av en basis
"""

def gram_scmidt(basis):
    ort_basis = []
    v = basis[0]
    ort_basis.append(v)
    for i in range(len(basis)-1):
        dotprods = 0    # <x3, v1> / <v1, v1>*v1 osv,
        for j in range(len(ort_basis)):
            dotprods += np.dot(basis[i+1], ort_basis[j]) / np.dot(ort_basis[j], ort_basis[j]) * ort_basis[j]
        v = basis[i+1] - dotprods
        ort_basis.append(v)

    return ort_basis

# Eksempel
x1 = np.array([2, -1, 2])
x2 = np.array([1, 2, 0])
x3 = np.array([-1, 0, 1])
basis = [x1, x2, x3]

[print(i) for i in gram_scmidt(basis)]      # Triks
