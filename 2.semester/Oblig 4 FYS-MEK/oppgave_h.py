import numpy as np
import matplotlib.pyplot as plt

class EulerCromer:
    def __init__(self, U0, x0, alpha, m, T, N):
        self.U0 = U0
        self.x0 = x0
        self.alpha = alpha
        self.m = m
        self.T = T

        self.N = N      # Antall tidssteg

        self.a = np.zeros(N+1)
        self.v = np.zeros(N+1)
        self.x = np.zeros(N+1)
        self.t = np.linspace(0, T, N+1)

    def acceleration(self, x, v):
        U0 = self.U0; alpha = self.alpha; m = self.m; x0 = self.x0
        if abs(x) < x0 and x != 0:
            return (-U0*abs(x) - alpha*v*x0*x) / (x0*x*m)
        else:
            return 0

    def set_initial_condition(self, v_0, x_0): # Setter initialbetingelser
        self.x_0 = x_0
        self.v_0 = v_0
        self.a_0 = self.acceleration(x_0, v_0)


    def solve(self):    # Løser differensiallikninger med E-C
        t = self.t; a = self.a; v = self.v; x = self.x
        a[0] = self.a_0
        v[0] = self.v_0
        x[0] = self.x_0
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1] = v[n] + dt*a[n]
            x[n+1] = x[n] + dt*v[n+1]
            a[n+1] = self.acceleration(x[n+1], v[n+1])

        return a, v, x, t


method = EulerCromer(U0=150, x0=2, alpha=39.48, m=23, T=10, N=10000)

if __name__ == '__main__':
    method.set_initial_condition(v_0=8.0, x_0=-5)
    a, v, x, t = method.solve()
    plt.plot(t, x, label= f'v_0 = {method.v_0}' )
    plt.xlabel(r'$t\;[-]$'); plt.ylabel(r'$x\;[-]$')
    plt.title('Atom gjennom felt', weight='bold')
    plt.legend()
    # plt.savefig('oppgave_i.png')
    plt.show()
