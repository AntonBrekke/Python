import numpy as np


def dR(R, I, V, dI, dV):
    dS = R*np.sqrt((dV / V)**2 + (dI / I)**2)
    return dS

# 1Mohm
V = 15.07       # V
I = 0.0149      # mA

# datablad: dV = 0.4% + 1: 0.07
# datablad: dI = 1.5% + 2: 0.0004

dV = 0.07       # V
dI = 0.0015     # mA
R = 1.01        # Mohm
print(dR(R, I, V, dI, dV))      # Mohm
