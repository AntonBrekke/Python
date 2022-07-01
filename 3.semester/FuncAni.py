import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
Eksempel for deg Rebecca :)
"""
# Lag figur
fig = plt.figure()
ax = fig.add_subplot()

# Lager bare et vilkårolig plot av en funksjon
x = np.linspace(-10, 10, 600)     # Høy ppløsning på array gir fin animasjon, men blir litt tregere
y = np.cos(2*x)* + np.sin(0.5*x) / (x**2 + 1)
ax.plot(x,y)

# Lager datalister som skal oppdateres og brukes i update-funksjonen
xdata, ydata = [], []
ball, = ax.plot([], [], 'ro', markersize=20)    # Lagrer objektet som skal animeres som et plot

"""
Funksjon som skal gjøre selve animeringen. Tar inn
frames som argument (se frames i FuncAnimation-funksjonen)
"""
def update(frame):
    xdata.append(x[frame])
    ydata.append(y[frame])
    ball.set_data(xdata[-1], ydata[-1])
    return ball,        # Må returneres som en iterabel fordi Blit=True. Dvs det må returneres som liste, tuppel etc.

"""
1 argument: figur som skal animeres i
2 argument: update-funksjonen
3 argument: hvor mange frames du skal ha
4 argument: intervall mellom hvert avspilte frame (kan justere ned dersom x er en stor array for å spille av fortere)
5 argument: Blit brukes bare til å optimalisere tegning.
"""
ani = FuncAnimation(fig, update, frames=[i for i in range(len(x))], interval=5, blit=True)

plt.show()
