# Exercise A.6 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt
# Definerer variabler gitt i oppgave:
a = 0.04
b = 0.1
c = 0.005
e = 0.2
n = 500

R = np.zeros(n+2)  # Array med 502 elementer pga jeg skal regne ut frem til n = 500 som senere gir R[501]
F = np.zeros(n+2)  # Array med 502 elementer pga jeg skal regne ut frem til n = 500 som senere gir F[501]
R[0] = 100; F[0] = 20   # Initialbetingelser

for n in range(n+1):    # Looper gjennom n = 0 til n = 500 og legger verdier inn i R og F
    R[n+1] = R[n] + a*R[n] - c*R[n]*F[n]
    F[n+1] = F[n] + e*c*R[n]*F[n] - b*F[n]

n = np.linspace(0,n,n+2)    # Gjør n om til en array med lik lengde som R og F

# Plotter R og F på akse 'n':
plt.plot(n,R, 'g', label = "Rabbits")
plt.plot(n,F, 'r', label = "Foxes")
plt.axis([0, n[-1]+1, 0, np.max(R)+20])    # Notat til self: ([xmin,xmax,ymin,ymax]), ikke (xmin,xmax,ymin,ymax)
plt.xlabel("Week 'n'")
plt.legend()
plt.show()

# Kjøreeksempel fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 42 IN1900> python Lotka_Volterra.py
PS C:\Desktop\Python\Oblig uke 42 IN1900>
"""
