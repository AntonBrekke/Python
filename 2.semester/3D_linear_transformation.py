import numpy as np
import matplotlib.pyplot as plt
# Lineær transformajson i 3D - en videreføring av koden jeg skrev
# for lineære transformasjoner i 2D

# Transformasjonsmatrise A:
A =  np.array([ [1, 0.2, 0.2],
                [-0.3, 1, 0.4],
                [0.5, 0, 1] ])
# Annet eksempel
# A =  np.array([ [1, 0, 0.2],
#                 [0, 1.2, 0.3],
#                 [0, 0, 1.1] ])

# Lager et meshgrid og en 3D-figur
I = np.linspace(-5, 5, 5)
J = np.linspace(-5, 5, 5)
K = np.linspace(-5, 5, 5)

x, y, z = np.meshgrid(I, J, K, indexing='xy')

# Lager figur og akser med gridspec
fig = plt.figure()
gs = fig.add_gridspec(2,3)
ax = fig.add_subplot(gs[0,0], projection='3d')
ax2 = fig.add_subplot(gs[1,0], projection='3d')
ax3 = fig.add_subplot(gs[0::,1::], projection='3d')

# Enkleste måten jeg fant å plotte et vanlig rettlinjet kartesisk 3D-grid
for i in range(len(x[0])):
    ax.plot_wireframe(x[i], y[i], z[i], color='k', alpha=0.4)
    ax.plot_wireframe(y[i], x[i], z[i], color='k', alpha=0.4)

    ax3.plot_wireframe(x[i], y[i], z[i], color='k', alpha=0.4)
    ax3.plot_wireframe(y[i], x[i], z[i], color='k', alpha=0.4)

# Gjør transformasjon og plotter
for i in range(len(x[0])):
    for j in range(len(x[0])):
        # Alle linjer langs x-aksen, løpende bortover y-aksen og z-aksen
        B = np.array([ [x[0,0,0], x[0,-1,0]],
                       [y[i,0,0], y[i,0,0]],
                       [z[0,0,j], z[0,0,j]] ])
        # Alle linjer langs y-aksen, løpende bortover x-aksen og z-aksen
        C = np.array([ [x[0,i,0], x[0,i,0]],
                       [y[0,0,0], y[-1,0,0]],
                       [z[0,0,j], z[0,0,j]] ])
        # Alle linjer langs z-aksen, løpende bortover x-aksen og y-aksen
        D = np.array([ [x[0,i,0], x[0,i,0]],
                       [y[j,0,0], y[j,0,0]],
                       [z[0,0,0], z[0,0,-1]] ])

        E = np.dot(A, B)
        F = np.dot(A, C)
        G = np.dot(A, D)
        ax2.plot(E[0], E[1], E[2], color='r', alpha=0.6); ax3.plot(E[0], E[1], E[2], color='r', alpha=0.8)
        ax2.plot(F[0], F[1], F[2], color='r', alpha=0.6); ax3.plot(F[0], F[1], F[2], color='r', alpha=0.8)
        ax2.plot(G[0], G[1], G[2], color='r', alpha=0.6); ax3.plot(G[0], G[1], G[2], color='r', alpha=0.8)

# ax.xaxis.pane.fill = False; ax2.xaxis.pane.fill = False; ax3.xaxis.pane.fill = False;
# ax.yaxis.pane.fill = False; ax2.yaxis.pane.fill = False; ax3.yaxis.pane.fill = False;
# ax.zaxis.pane.fill = False; ax2.zaxis.pane.fill = False; ax3.zaxis.pane.fill = False;

ax.xaxis.pane.set_color('forestgreen'); ax2.xaxis.pane.set_color('forestgreen'); ax3.xaxis.pane.set_color('forestgreen')
ax.yaxis.pane.set_color('forestgreen'); ax2.yaxis.pane.set_color('forestgreen'); ax3.yaxis.pane.set_color('forestgreen')
ax.zaxis.pane.set_color('forestgreen'); ax2.zaxis.pane.set_color('forestgreen'); ax3.zaxis.pane.set_color('forestgreen')

ax.xaxis.pane.set_edgecolor('k'); ax2.xaxis.pane.set_edgecolor('k'); ax3.xaxis.pane.set_edgecolor('k')
ax.yaxis.pane.set_edgecolor('k'); ax2.yaxis.pane.set_edgecolor('k'); ax3.yaxis.pane.set_edgecolor('k')
ax.zaxis.pane.set_edgecolor('k'); ax2.zaxis.pane.set_edgecolor('k'); ax3.zaxis.pane.set_edgecolor('k')

# Setter grenser så enhetskube ikke skvises av transformasjon
lims_ax3 = np.max([np.max(E), np.max(F), np.max(G)])
ax3.set_xlim(-lims_ax3, lims_ax3); ax3.set_ylim(-lims_ax3, lims_ax3); ax3.set_zlim(-lims_ax3, lims_ax3)

ax.grid(False); ax2.grid(False); ax3.grid(False)
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')


fig.suptitle(f'A = {A}\n det(A)={np.linalg.det(A):.3f}', fontsize=16)
fig.tight_layout()
plt.show()
