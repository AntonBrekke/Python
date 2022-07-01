# Exercise 1.1 Oppgaveprosjekt 2020
# Anton Brekke

import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

# Code copied from exercise, right-side of ODE
def SEIR(u,t):
    beta = 0.5; r_ia = 0.1; r_e2=1.25;
    lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2;

    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS  = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI  = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR  = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]

S_0 = 5e6
E1_0 = 0
E2_0 = 100
I_0 = 0
Ia_0 = 0
R_0 = 0
U0 = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]

solver = RungeKutta4(SEIR)
solver.set_initial_condition(U0)
time_points = np.linspace(0, 100, 101)
u, t = solver.solve(time_points)
S = u[:,0]; E1 = u[:,1]; E2 = u[:,2];
I = u[:,3]; Ia = u[:,4]; R = u[:,5]

plt.plot(t,S,label='S')
#plt.plot(t,E1,label='E1')
#plt.plot(t,E2,label='E2')
plt.plot(t,I,label='I')
plt.plot(t,Ia,label='Ia')
plt.plot(t,R,label='R')
plt.legend()
plt.savefig('seir_fig0.pdf')
plt.show()


# a)
# Test-function testing if SEIR returns correct values
def test_SEIR():
    t = 0; u = [1,1,1,1,1,1]
    tol = 1e-10
    computed = SEIR(u,t)
    expected = [-0.19583333333333333, -0.13416666666666668, -0.302, 0.3, -0.068, 0.4]
    msg = 'Something wrong'
    for i in range(len(u)):
        success = abs(computed[i] - expected[i]) < tol
        assert success, msg
test_SEIR()


# b)
# Function for solving ODE in top of
def solve_SEIR(T, dt, S_0, E2_0):
    U0 = [S_0, 0, E2_0, 0, 0, 0]; h = T/dt
    solver = RungeKutta4(SEIR)
    solver.set_initial_condition(U0)
    time_points = np.linspace(0, T, int(h)+1)
    u, t = solver.solve(time_points)
    return u, t


# c)
# Function for plotting solution
def plot_SEIR(u, t):
    S = u[:,0]; E1 = u[:,1]; E2 = u[:,2];
    I = u[:,3]; Ia = u[:,4]; R = u[:,5]
    plt.plot(t,S,label='S')
    plt.plot(t,I,label='I')
    plt.plot(t,Ia,label='Ia')
    plt.plot(t,R,label='R')
    plt.legend()
    plt.show()


# d)
# Creating problem, solving and plotting solution
S_0 = 5e6; E2_0 = 100; T = 100; dt = 1.0
u, t = solve_SEIR(T, dt, S_0, E2_0)
plot_SEIR(u, t)


# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oppgaveprosjekt IN1900> python seir_func.py
PS C:\Desktop\Python\Oppgaveprosjekt IN1900>
"""
