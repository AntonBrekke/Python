#Exercise 6.14
# a)
import numpy as np
import matplotlib.pyplot as plt

# Definerer p1 og p2 som punkter gitt i input fra terminal
p1 = (eval(input("Write x1,y1 here:")))     # (x1, y1)
p2 = (eval(input("Write x2,y2 here:")))     # (x2, y2)

# Definerer plot_line funksjon som sorterer x-verdier og y-verdier inn i plt.plot
def plot_line(p1, p2):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]])        # plt.plot([x1, x2], [y1, y2])
    plt.show()

plot_line(p1,p2)        # Kaller på funksjon med p1 og p2 gitt med input

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 40 IN2900> python graph1.py
Write x1,y1 here:0,1
Write x2,y2 here:1,1
PS C:\Desktop\Python\Oblig uke 40 IN2900> python graph1.py
Write x1,y1 here:0,1
Write x2,y2 here:0,0
PS C:\Desktop\Python\Oblig uke 40 IN2900>
"""
# b)

# Bruker funksjon fra forrige oppgave til å regne med ny funksjon
def plot_line(p1, p2):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]])

# Firkant
points = [(0,0),(1,0),(0.5,1),(1.5,1)]      # Lister inn punkter fra oppgave

def complete_graph(points):         # Funksjon som går igjennom alle punkter pr.punkt og tegner linjer med alle punkter utenom seg selv
    for i in range(len(points)):        # Løper gjennom alle punkter j i range len(points) for hver i
        for j in range(len(points)):
            if i != j:                  # Tegner punkt points[i] opp mot alle punkter points[j] som er er ulik seg selv
                plot_line(points[i], points[j])

    plt.show()
complete_graph(points)      # Kaller funksjon med argument "points"

# Oktagon
a = np.log(2)
points = [(1,0),(a,a),(0,1),(-a,a),(-1,0),(-a,-a),(0,-1),(a,-a)]    # Lister inn punkter fra oppgave

def complete_graph(points):         # Funksjon som går igjennom alle punkter pr.punkt og tegner linjer med alle punkter utenom seg selv
    for i in range(len(points)):        # Løper gjennom alle punkter j i range len(points) for hver i
        for j in range(len(points)):
            if i != j:                  # Tegner punkt points[i] opp mot alle punkter points[j] som er er ulik seg selv
                plot_line(points[i],points[j])

    plt.show()
complete_graph(points)      # Kaller funksjon med argument "points"

# Kjøretest fra terminal:
"""
PS \Desktop\Python\Oblig uke 40 IN2900> python graph1.py
PS \Desktop\Python\Oblig uke 40 IN2900>
"""
