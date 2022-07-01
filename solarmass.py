"""
Oppgave 1.2 Fysikkheftet, beregne solmasse utifra gitt formel
"""
import math

AU = 1.58 * 10**-5 * 9.5 * 10**15
G = 6.674 * 10**-11
pi = 3.1415
amount = (4 * (math.pi)**2 * (AU)**3)/(G * (365 * 24 * 60**2)**2)
print("M_sol =" , amount)
