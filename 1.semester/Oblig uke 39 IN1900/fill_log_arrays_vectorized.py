# Exercise 6.2
import numpy as np

x = np.linspace(1,10,101)       # Lager array med verdier mellom 1 og 10 i 101 intervaller med lik lengde med linspace
y = np.zeros(101)               # Lager array med 101 nuller som senere skal fylles med verdier

# Funksjonsuttrykk gitt i oppgave
def f(x):
    return np.log(x)

y = f(x)        # Fyller y-array med funksjonsverdier tilsvarende x-array-verdier
#print(y)

# Kjøretest fra terminal:
"""
PS C:\Desktop\python\Oblig uke 39 IN1900> python fill_log_arrays_vectorized.py
PS C:\Desktop\python\Oblig uke 39 IN1900>
"""
