# Exercise 6.1
import numpy as np

# Setter opp x-array og y-array med 101 nuller (fordi jeg får 101 x-verder og tilsvarende f(x)-verdier)
x = np.zeros(101)
y = np.zeros(101)

# Deler opp tallene mellom 1 og 10 i 100 intervaller med lik lengde (100 intervaller fordi det gir 101 x-verdier i [1,10])
b = 10      # Max-verdi i intervall
a = 1       # Min-verdi intervall
n = 100     # Antall intervaller - 1 fordi det er 101 nuller
h = (b-a)/n

# Funksjonsuttrykk gitt i oppgave
def f(x):
    return np.log(x)

# Loop som regner ut x-verdier og tilsvarende f(x)-verdier og legger til i x-array og y-array
for i in range(0, 101):
    x[i] = 1 + h*i
    y[i] = f(x[i])
    #print(f"{x[i]:10.16f}\t|\t{y[i]}")

# Kjøretest fra terminal:
"""
PS C:\Desktop\python\Oblig uke 39 IN1900> python fill_log_arrays_loop.py
PS C:\Desktop\python\Oblig uke 39 IN1900>
"""
