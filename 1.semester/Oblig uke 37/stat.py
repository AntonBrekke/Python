import numpy as np
# a)
def mean(x_list):       # Funksjon for gjennomsnittsverdien av en liste
    s = 0
    for i in range(len(x_list)):
        s += x_list[i]/len(x_list)
    return s
# b)
x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
def test_mean():        # Testfunksjon som vurderer om verdien fra forrige def stemmer
    expected = np.mean(x_test_values)       # Forventet verdi utregnet av numpy
    computed = mean(x_test_values)          # Verdi fra funksjon
    tol = 1e-12                             # Toleranseverdi
    success = abs(expected - computed) < tol
    msg = 'Something is wrong!'
    assert success, msg         # Dersom success er usann returneres msg

test_mean()

# c)
from math import sqrt
def standard_deviation(x_list):     # Funksjon som beskriver gjennomsnittlig avvik fra gjennomsnittet (deviation)
    s = 0
    s_n = 0
    for i in range(len(x_list)):
        s += (x_list[i]-mean(x_list))**2/len(x_list)
        s_n = sqrt(s)
    return s_n

# d)
def test_standard_deviation():          # Testfunksjon for standard_deviation
    expected = np.std(x_test_values)    # Forventet verdi (basert på numpy)
    computed = standard_deviation(x_test_values)    # Beregnet verdi
    tol = 1e-12                         # Toleranseverdi
    success = abs(expected - computed) < tol
    msg = 'Something is really wrong!'
    assert success, msg         # # Dersom success er usann returneres msg

test_standard_deviation()

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 37> python stat.py
PS C:\Desktop\Python\Oblig uke 37>
"""
