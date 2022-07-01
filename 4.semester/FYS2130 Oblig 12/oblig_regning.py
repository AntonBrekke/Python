import numpy as np
import matplotlib.pyplot as plt

# 3)
def get_sightpoint(dioptre):
    """
    Vi bruker linsemakerformelen
    1/f = 1/s + 1/s' = X dioptre
    der X = 50 er ideellt syn. Vi får
    s = 1 / (X - 1/s') der 1 / s' = 1 / 0.02 = 50 (s' = 2cm vanlig for et øye). Dermed får vi formelen
    s = 1 / (X - 50), der X dioptre er synet til personen en avstand s' unna. Dvs. at vi må korrigere
    synet til personen med 54 - X dioptre for nærsyn (54 ideellt nærsyn) og 50 - dioptre for langsyn.
    F.eks en person får utskrevet briller med +3 dioptre korrigert for langsyn. Dvs. at
    1/s + 1/s' = 51 (54 - 3)  =>  s = 1 / (51 - 50) = 1, og dermed er s = 1 / ((54 - styrke) - 50) = 1 / (4-styrke)
    """
    return 1 / (dioptre - 50)

print(f'\nclosest distance: {get_sightpoint(54 - 3)}')      # Ideelt nærsyn er 54 dioptre
print(f'\nfurthest distance: {get_sightpoint(50 - (-0.75))}')   # Ideellt langsyn er 50 dioptre

# 4)
# Mikroskop

f1 = 9       # mm, objektiv
f2 = 19       # mm, okular
L = 199         # mm, avstand mellom objektiv og okular, s1' + s2'
# Vi lar s2 gå mot undelig, og dermed er s2' = f2
s2p = f2
s1p = L - s2p
# Fra linsemakerformelen:
s1 = f1*s1p / (s1p - f1)
print(f'\ns1: {s1} mm')
# Finner forstørrelsesfaktorer
M_objektiv = s1p / s1
M_okular = 250 / f2         # Se boka
M_tot = M_objektiv * M_okular
print(f'\nM_objektiv: {M_objektiv}, M_okular: {M_okular}, M_tot: {M_tot}')
