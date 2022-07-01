import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.colors import ListedColormap
# Dette virker med versjon 7 MAT-filer
data = sio.loadmat('data.mat')
x = data.get('x')
y = data.get('y')
u = data.get('u')       # i-komponent av hastighet
v = data.get('v')       # j-komponent av hastighet
xit = data.get('xit')
yit = data.get('yit')

l = np.sqrt(u**2 + v**2)    # Størrelse på hastighetsfelt

# Lager nytt fargekart som passer plottet bedre
"""
Til gammel kode. Fortsatt kult, kan snu cmap og kombinere osv.
top = cm.get_cmap('CMRmap', 256)
bottom = cm.get_cmap('YlOrRd', 256)

newcolors = np.vstack((top(np.linspace(0, 1, 40)),
                       bottom(np.linspace(0, 1, 200))))
newcmp = ListedColormap(newcolors, name='CustomCMAP')
"""

# Kode som regner nye y-verdier for konturet på en skillelinje b
y_gas = y.copy(); y_fluid = y.copy()
l_gas = l.copy(); l_fluid = l.copy()
u_gas = u.copy(); v_gas = v.copy()
u_fluid = u.copy(); v_fluid = v.copy()
for m in range(len(y[:,0])):
    for n in range(len(y[0])):
        if y[m,n] > yit[0,n]:
            y_fluid[m,n] = yit[0,n]
            l_fluid[m,n] = 0
            u_fluid[m,n] = 0; v_fluid[m,n] = 0
        elif y[m,n] < yit[0,n]:
            y_gas[m,n] = yit[0,n]
            l_gas[m,n] = 0
            u_gas[m,n] = 0; v_gas[m,n] = 0

"""
Begge deler er overkill, man kunne brukt kun en av disse.
Men med begge kombinert får jeg kontur stoppet på linja
og lokal hastighet for hvert kontur.
# Flytter linjen opp
y_gas = y.copy(); y_fluid = y.copy()
for m in range(len(y[:,0])):
    for n in range(len(y[0])):
        if y[m,n] > yit[0,n]:
            y_fluid[m,n] = yit[0,n]
        elif y[m,n] < yit[0,n]:
            y_gas[m,n] = yit[0,n]

# Setter verdier over/under linjen lik 0. Kunne også brukt np.nan
l_gas = l.copy(); l_fluid = l.copy()
for m in range(len(y[:,0])):
    for n in range(len(y[0])):
        if y[m,n] > yit[0,n]:
            l_fluid[m,n] = 0
        elif y[m,n] < yit[0,n]:
            l_gas[m,n] = 0
"""

# Plotter
if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(xit, yit, 'wo', markersize=3)
    ax.set_xlabel(r'x [mm]', weight='bold')
    ax.set_ylabel(r'y [mm]', rotation=0, weight='bold', position=(0,0.52))
    gas = ax.contourf(x, y_gas, l_gas, 200, cmap='viridis')
    fluid = ax.contourf(x, y_fluid, l_fluid, 200, cmap='inferno')
    cbar_gas = fig.colorbar(gas, ax=ax)
    cbar_fluid = fig.colorbar(fluid, ax=ax)
    cbar_gas.set_label(r'Gas speed [mm/s]', weight='bold')
    cbar_fluid.set_label(r'Fluid speed [mm/s]', weight='bold')
    ax.legend(['Separation line'])
    fig.tight_layout()
    plt.show()

    fig2 = plt.figure()
    gs = fig2.add_gridspec(2,1)
    ax2 = fig2.add_subplot(gs[1,0])
    ax3 = fig2.add_subplot(gs[0,0])

    ax2.set_title('Fluid', weight='bold')
    ax2.plot(xit, yit, 'ko', markersize=3)
    ax2.set_xlabel(r'x [mm]', weight='bold')
    ax2.set_ylabel(r'y [mm]', rotation=0, weight='bold', position=(0,0.52))
    fluid2 = ax2.contourf(x, y_fluid, l_fluid, 200, cmap='jet')
    cbar_fluid2 = fig2.colorbar(fluid2, ax=ax2)
    cbar_fluid2.set_label(r'Fluid speed [mm/s]', weight='bold')

    ax3.set_title('Gas', weight='bold')
    ax3.plot(xit, yit, 'ko', markersize=3)
    ax3.set_xlabel(r'x [mm]', weight='bold')
    ax3.set_ylabel(r'y [mm]', rotation=0, weight='bold', position=(0,0.58))
    gas3 = ax3.contourf(x, y_gas, l_gas, 200, cmap='jet')
    cbar_gas3 = fig2.colorbar(gas3, ax=ax3)
    cbar_gas3.set_label(r'Gas speed [mm/s]', weight='bold')
    ax2.legend(['Separation line']); ax3.legend(['Separation line'])
    fig2.tight_layout()
    plt.show()
# Kjøretest fra terminal:
"""
PS C:Desktop\Python\2.semester\OBLIG 2 MEK1100> python .\oppgave_b.py
PS C:Desktop\Python\2.semester\OBLIG 2 MEK1100>
"""
