### 3.23 i Langtangen
from math import log, pi
def egg(M, T0=20, Ty=70):
    rho = 1.038
    K = 5.4e-3
    Tw = 100
    c = 3.7
    t = (M**(2/3)* c * rho**(1/3) / (K*(pi**2)*((4*pi)/3))**(2/3))*log(0.76*(T0-Tw)/(Ty-Tw))
    return t

# Lite egg + fra kjøleskap + bløtkokt
print(egg(47, T0=4, Ty=65)/60)

# Stort egg + varmt rom + hardkokt:
print(egg(67, T0=25, Ty=80)/60)
