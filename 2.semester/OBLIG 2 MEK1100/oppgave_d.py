from oppgave_b import *

# HUSK: Fulle hastighetsfeltet
# v = ui + vj + wk, vi regner ikke på k
# Vi ser på divergensen i xy-planet

dx = 0.5    # dx i x-grid er 0.5
dy = 0.5    # dy i y-grid er 0.5

# Regner ut divergens
"""
Pass på riktig akser. x og y er på indexing 'xy',
og u,v har samme form som x,y , så de er også på indexing 'xy'.
Da blir axis = 1 differansiering langs x, og axis = 0
differansiering langs y
"""
dudx = np.gradient(u, dx, axis=1)
dvdy = np.gradient(v, dy, axis=0)
div = dudx + dvdy

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)

    divergence = ax.contourf(x, y, div, 200, cmap='jet')
    ax.plot(xit, yit, 'ro', markersize=3)
    cbar_div = fig.colorbar(divergence, ax=ax)
    cbar_div.set_label(r'Divergence [1/s]', weight='bold')

    ax.set_xlabel(r'x [mm]', weight='bold')
    ax.set_ylabel(r'y [mm]', rotation=0, weight='bold', position=(0,0.52))

    # Rektangel 1
    # plt.plot([x[0, 35], x[0,70]], [y[160, 0], y[170,0]], 'b')
    ax.plot([x[0, 35], x[0,70]], [y[170, 0], y[170,0]], 'b')   # Øverst
    ax.plot([x[0, 35], x[0,70]], [y[160, 0], y[160,0]], 'r')   # Nederst
    ax.plot([x[0, 70], x[0,70]], [y[160, 0], y[170,0]], 'g')   # Høyre
    ax.plot([x[0, 35], x[0,35]], [y[160, 0], y[170,0]], 'k')   # Venstre

    # Rektangel 2
    # plt.plot([x[0, 35], x[0,70]], [y[85, 0], y[100,0]], 'b')
    ax.plot([x[0, 35], x[0,70]], [y[100, 0], y[100,0]], 'b')   # Øverst
    ax.plot([x[0, 35], x[0,70]], [y[85, 0], y[85,0]], 'r')     # Nederst
    ax.plot([x[0, 70], x[0,70]], [y[85, 0], y[100,0]], 'g')    # Høyre
    ax.plot([x[0, 35], x[0,35]], [y[85, 0], y[100,0]], 'k')    # Venstre

    #Rektangel 3
    # plt.plot([x[0, 35], x[0,70]], [y[50, 0], y[60,0]], 'b')
    ax.plot([x[0, 35], x[0,70]], [y[60, 0], y[60,0]], 'b')     # Øverst
    ax.plot([x[0, 35], x[0,70]], [y[50, 0], y[50,0]], 'r')     # Nederst
    ax.plot([x[0, 70], x[0,70]], [y[50, 0], y[60,0]], 'g')     # Høyre
    ax.plot([x[0, 35], x[0,35]], [y[50, 0], y[60,0]], 'k')     # Venstre

    ax.legend(['Separation line'], loc='lower right')
    plt.show()
