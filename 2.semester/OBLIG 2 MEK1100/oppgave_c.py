from oppgave_b import *

N = 5
plt.quiver(x[::N, ::N], y[::N, ::N], u[::N, ::N], v[::N, ::N], width=0.002)
plt.plot(xit, yit, 'ro', markersize=3)

# plt.plot([x[0, 35], x[0,70]], [y[160, 0], y[170,0]], 'b')
plt.plot([x[0, 35], x[0,70]], [y[170, 0], y[170,0]], 'b')   # Øverst
plt.plot([x[0, 35], x[0,70]], [y[160, 0], y[160,0]], 'r')   # Nederst
plt.plot([x[0, 70], x[0,70]], [y[160, 0], y[170,0]], 'g')   # Høyre
plt.plot([x[0, 35], x[0,35]], [y[160, 0], y[170,0]], 'k')   # Venstre

# Rektangel 2
# plt.plot([x[0, 35], x[0,70]], [y[85, 0], y[100,0]], 'b')
plt.plot([x[0, 35], x[0,70]], [y[100, 0], y[100,0]], 'b')   # Øverst
plt.plot([x[0, 35], x[0,70]], [y[85, 0], y[85,0]], 'r')     # Nederst
plt.plot([x[0, 70], x[0,70]], [y[85, 0], y[100,0]], 'g')    # Høyre
plt.plot([x[0, 35], x[0,35]], [y[85, 0], y[100,0]], 'k')    # Venstre

#Rektangel 3
# plt.plot([x[0, 35], x[0,70]], [y[50, 0], y[60,0]], 'b')
plt.plot([x[0, 35], x[0,70]], [y[60, 0], y[60,0]], 'b')     # Øverst
plt.plot([x[0, 35], x[0,70]], [y[50, 0], y[50,0]], 'r')     # Nederst
plt.plot([x[0, 70], x[0,70]], [y[50, 0], y[60,0]], 'g')     # Høyre
plt.plot([x[0, 35], x[0,35]], [y[50, 0], y[60,0]], 'k')     # Venstre

plt.legend(['Separation line'], loc='lower right')
plt.show()

# Kjøretest fra terminal
