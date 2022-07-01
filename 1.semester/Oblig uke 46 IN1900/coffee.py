# Exercise E.7 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

# a)
# Klasse for hvor fort temperaturen i en kaffekopp synker
class Cooling:
    def __init__(self, h, Ts):
        self.h = h
        self.Ts = Ts
    # Funksjon gitt i oppgave
    def __call__(self, T, t):
        h, Ts = self.h, self.Ts
        return -h*(T - Ts)

def estimate_h(t1, Ts, T0, T1):
    return (T1 - T0) / (t1*(Ts - T0))

# b)
# Testfunksjon for Cooling:
def test_Cooling():
    T1 = 10
    T0 = 30
    t1 = 1
    Ts = 20
    h = 2
    Comp = Cooling(h, Ts)
    computed = Comp(T1, t1)
    expected = 20
    success = computed == expected
    assert success
test_Cooling()

# c)
T0 = 95     # Initialbetingelse
T1 = 92     # T i t1
t1 = 15     # Første måling etter 15s
Ts1 = 20    # Temperatur omgivelser
Ts2 = 25    # Temperatur omgivelser 2

h1 = estimate_h(t1, Ts1, T0, T1)    # Estimerer h for tilfelle 1
h2 = estimate_h(t1, Ts2, T0, T1)    # Estimerer h for tilfelle 2
time_points = np.linspace(0, 2700, 2700)        # 45 min
Cooling1 = Cooling(h1, Ts1)     # Lager objekt for tilfelle 1
Cooling2 = Cooling(h2, Ts2)     # Lager objekt for tilfelle 2

# Plot
func1 = ForwardEuler(Cooling1)      # Sender inn klasse-funksjonen fra Cooling1
func1.set_initial_condition(T0)
T, t = func1.solve(time_points)
plt.plot(t, T, label ='$T_s=20C^o$')

func2 = ForwardEuler(Cooling2)      # Sender inn klasse-funksjonen fra Cooling2
func2.set_initial_condition(T0)
T, t = func2.solve(time_points)
plt.plot(t, T, 'r', label ='$T_s=25C^o$')

plt.xlabel('time / s')
plt.ylabel('degrees / $C^o$')
plt.title('Hot coffee over time')
plt.legend()
plt.show()

# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 46 IN1900> python coffee.py
PS C:\Python\Oblig uke 46 IN1900>
"""
