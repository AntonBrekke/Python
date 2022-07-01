# Exercise 6.4
import numpy as np

k = 4       # Fjærkonstant
gamma = 0.15    # Friksjonkonstant
m = 9       # Masse i kg
A = -0.3     # Høyde som dras ned. Setter negativ fordi oppgaven sier "Pull down", som insinuerer at lengden er negativ.

#a)
b = 25      # Max verdi x
a = 0       # Min verdi x
n = 101     # Antall intervaller
h = (b-a)/n # Lengde på intervaller

# Funksjon for høyde av stein i fjære gitt i oppgave
def y(t):
    return A*np.exp(-gamma*t)*np.cos(np.sqrt((k/m))*t)

# Arrays med 101 nuller
t_array = np.zeros(101)
y_array = np.zeros(101)

# Plotter inn verdier for t og tilsvarende y(t) verdi i t_array og y_array
for i in range(0, 101):
    t_array[i] = i*h
    y_array[i] = y(t_array[i])
#print(y_array)

# b)
# Funksjon for høyde av stein i fjære gitt i oppgave
def y(t):
    return A*np.exp(-gamma*t)*np.cos(np.sqrt((k/m))*t)

# Lager t_array med linspace, 101 intervaller fra 0 til 25 i like lengder og y_array2 med 101 nuller
t_array2 = np.linspace(0, 25, 101)
y_array2 = np.zeros(101)

# Lager y_array2 med tilsvarende y(t_array2) verdier
y_array2 = y(t_array2)
#print(y_array2)

#c)
# Importerer modul og plotter funkjsoner med verdier fra oppgave a) og b)
import matplotlib.pyplot as plt

plt.plot(t_array, y_array, "b", label = "zeros")
plt.plot(t_array2, y_array2, "r-.", label = "linspace")
plt.xlabel('time [s]')
plt.ylabel('height [m]')
plt.title('Oscillating spring')
plt.axis([0,25,-0.3,0.3])   # Justerer aksen av estetiske grunner
plt.legend()

plt.show()

# Kjøretest fra terminal:
"""
PS C:\Desktop\python\Oblig uke 39 IN1900> python oscillating_spring.py
PS C:\Desktop\python\Oblig uke 39 IN1900>
"""
