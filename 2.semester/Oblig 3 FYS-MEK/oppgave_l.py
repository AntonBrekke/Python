from oppgave_k import *


KE = 0.5*method.m*v**2
if __name__ == '__main__':
    plt.plot(r[:,0], KE[:,0], label='Kinetisk energi')
    plt.xlabel(r'$x\;[m]$')
    plt.ylabel(r'$K_e\;[J]$')
    # plt.savefig('oppgave_l.png')
    plt.legend()
    plt.show()
