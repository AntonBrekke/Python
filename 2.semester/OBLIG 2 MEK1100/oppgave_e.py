from oppgave_d import *


dudy = np.gradient(u, dx, axis=0)
dvdx = np.gradient(v, dy, axis=1)

curl = dvdx - dudy

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)

    curlz = ax.contourf(x, y, curl, 200, cmap='hsv')
    curl_cbar = fig.colorbar(curlz, ax=ax)
    ax.plot(xit, yit, 'ko', markersize=3)

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

    fig = plt.figure()
    ax = fig.add_subplot(111)

    stream = ax.streamplot(x, y, u, v, color=l, cmap='jet')
    ax.plot(xit, yit, 'ko', markersize=3)
    stream_bar = fig.colorbar(stream.lines, ax=ax)
    ax.legend(['Separation line'])
    plt.show()
