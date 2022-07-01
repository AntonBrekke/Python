import numpy as np
import matplotlib.pyplot as plt

"Med 'ij' indexing"
I = np.linspace(-10, 10, 101)
x, y = np.meshgrid(I, I, indexing='ij')

A = np.array([ [1,0],
               [0,-2] ])

fig, ax = plt.subplots(1,1)
ax.set_facecolor('k')   # Setter bakgrunnsfarge på plott til svart
# Plotter x og y-akse i hvitt
plt.plot([-10,10],[0,0], 'w', alpha=0.4)
plt.plot([0,0], [-10,10], 'w', alpha=0.4)

plt.plot(x, y, 'slategrey', alpha=0.2)
plt.plot(y, x, 'slategrey', alpha=0.2)
# plt.plot(x, y, 'slategrey', y, x, 'slategrey', alpha=0.2)    # Kan forenkle til én linje
for i in range(len(x)):
    # plt.plot([x[i,0], x[i,0]],[y[0,0],y[0,-1]], 'k', alpha=0.5)
    # plt.plot([x[0,0], x[-1,0]],[y[0,i], y[0,i]], 'k', alpha=0.5)
    # B er array gridlines langs x-aksen
    B = np.array([ [x[i,0], x[i,0]],
                   [y[0,0], y[0,-1]] ])
    # C er array med gridlines langs y-aksen
    C = np.array([ [x[0,0], x[-1,0]],
                   [y[0,i], y[0,i]] ])
    # Transformerer gridlines langs x-aksen og y-aksen Ax = b
    D = np.dot(A,B)
    E = np.dot(A,C)
    plt.plot(D[0,:], D[1,:], 'lightseagreen', alpha=0.4)
    plt.plot(E[0,:], E[1,:], 'lightseagreen', alpha=0.4)
    # plt.plot(D[0,:], D[1,:], 'lightseagreen', E[0,:], E[1,:], 'lightseagreen', alpha=0.4)   # Kan samle 2 plots på 1 linje

# Lager origo
plt.plot(0, 0, 'gold', marker='o')
# Definerer enhetsvektorer og plotter tilsvarende enhetsvektorer
def vectors():
    unit_x = plt.arrow(0, 0, 1, 0, width=0.05, head_width=0.15, color='darkred', length_includes_head=True)
    unit_y = plt.arrow(0, 0, 0, 1, width=0.05, head_width=0.15, color='forestgreen', length_includes_head=True)
    basis_x = np.array([[1],[0]])       # Kolonne-vektor
    basis_y = np.array([[0], [1]])      # Kolonne-vektor
    # Bruker transformasjon på basisvektorer
    basis_trans_x = np.dot(A, basis_x)
    basis_trans_y = np.dot(A, basis_y)
    basis_trans_x_arrow = plt.arrow(0, 0, basis_trans_x[0,0], basis_trans_x[1,0], width=0.05, head_width=0.15, color='red', length_includes_head=True)
    basis_trans_y_arrow = plt.arrow(0, 0, basis_trans_y[0,0], basis_trans_y[1,0], width=0.05, head_width=0.15, color='limegreen', length_includes_head=True)
    # Plotter outline til determinanten
    line1 = plt.plot([basis_trans_y[0,0], basis_trans_x[0,0] + basis_trans_y[0,0]], [basis_trans_y[1,0], basis_trans_x[1,0] + basis_trans_y[1,0]], 'yellow', alpha=0.4)
    line2 = plt.plot([basis_trans_x[0,0], basis_trans_x[0,0] + basis_trans_y[0,0]], [basis_trans_x[1,0], basis_trans_x[1,0] + basis_trans_y[1,0]], 'yellow', alpha=0.4)
vectors()
# Begrenser og justerer plottet for synets skyld
plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.suptitle(r'Linear transformation, $\mathbb{R}^2 \rightarrow \mathbb{R}^2$', fontweight='bold')
plt.show()



"""
"Med 'xy' indexing"
I = np.linspace(-5,5, 30)
x,y = np.meshgrid(I, I, indexing='xy')

for i in range(len(x)):
    # plt.plot([x[i,0], x[i,0]],[y[0,0],y[0,-1]], 'k', alpha=0.5)
    # plt.plot([x[0,0], x[-1,0]],[y[0,i], y[0,i]], 'k', alpha=0.5)
    "Indekseringen her blir liltt annerledes, men resten blir likt som med 'ij'"
    B = np.array([ [x[0,i], x[0,i]],
                   [y[0,0], y[-1,0]] ])
    C = np.array([ [x[0,0], x[0,-1]],
                   [y[i,0], y[i,0]] ])
    D = np.dot(A,B)
    E = np.dot(A,C)
    plt.plot(D[0,:], D[1,:], 'royalblue')
    plt.plot(E[0,:], E[1,:], 'royalblue')
plt.plot(0, 0, 'ro')

plt.plot(x, y, 'k', alpha=0.5)
plt.plot(y, x, 'k', alpha=0.5)
plt.axis('equal')
# plt.show()
"""
