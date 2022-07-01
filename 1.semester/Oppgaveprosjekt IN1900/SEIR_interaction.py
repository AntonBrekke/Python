# Exercise 1.3 oppgaveprosjekt 2020
# Anton Brekke

import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *
from SEIR import *

# a)
class RegionInteraction(Region):
    def __init__(self, name, S_0, E2_0, lat, long):
        Region.__init__(self, name, S_0, E2_0)
        self.lat = lat*np.pi / 180        # Convert from degrees to radians
        self.long = long*np.pi / 180
    # Method calculating distance between two regions
    def distance(self, other):      # self = i, other = j
        R_earth = 64        # Of order 10^5
        phi_i = self.lat; phi_j = other.lat
        lambda_i = self.long; lambda_j = other.long
        arg = np.sin(phi_i)*np.sin(phi_j) + np.cos(phi_i)*np.cos(phi_j)*np.cos(abs(lambda_i - lambda_j))
        if arg < 1:
            dt_sigma = np.arccos(arg)
            d_ij = R_earth*dt_sigma
            return d_ij
        else:           # ex. if phi_i = phi_j and lambda_i = lambda_j gives arg = 1, the distance from a place to itself is 0
            return 0


if __name__ == '__main__':
    innlandet = RegionInteraction('Innlandet', S_0=371385, E2_0=0, lat=60.7945,long=11.0680)
    oslo = RegionInteraction('Oslo', S_0=693494, E2_0=100, lat=59.9,long=10.8)
    print(oslo.distance(innlandet), "\n")   # Answer is reasonable since the distance from Oslo to Hamar is 100km


# b)
# Class calculating values for and between every regions i given list
class ProblemInteraction(ProblemSEIR):  #  region should be a list of regions, all instances of class RegionInteraction
    def __init__(self, region, area_name, beta, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
        self.area_name = area_name
        ProblemSEIR.__init__(self, region, beta, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2)

    def get_population(self):
        tot = 0         # Sums population of all elements in region
        for n in self.region:
            tot += n.population
        return tot

    def set_initial_condition(self):    # Creating a list with initial conditions from all regions
        self.initial_condition = []
        for n in self.region:
            self.initial_condition += n.S_0, n.E1_0, n.E2_0, n.I_0, n.Ia_0, n.R_0

    def __call__(self, u, t):
        beta = self.beta; r_ia = self.r_ia; r_e2 = self.r_e2;
        lmbda_1 = self.lmbda_1; lmbda_2 = self.lmbda_2; p_a = self.p_a; mu = self.mu;
        n = len(self.region)
        # create a nested list:
        # SEIR_list[i] = [S_i, E1_i, E2_i, I_i, Ia_i, R_i]:
        SEIR_list = [u[i:i+6] for i in range(0, len(u), 6)]
        # Create separate lists containing E2 and Ia values:
        E2_list = [u[i] for i in range(2, len(u), 6)]
        Ia_list = [u[i] for i in range(4, len(u), 6)]
        derivative = []
        for i in range(n):
            S, E1, E2, I, Ia, R = SEIR_list[i]
            dS = 0; dE1 = 0; dE2 = 0;
            dI = 0; dIa = 0; dR = 0;
            for j in range(n):
                N_i = sum(SEIR_list[i])
                N_j = sum(SEIR_list[j])
                d_ij = self.region[i].distance(self.region[j])
                E2_other = E2_list[j]
                Ia_other = Ia_list[j]
                # Keep in mind: beta is a function according to ProblemSEIR
                dS += -r_ia*beta(t)*S * Ia_other/N_j*np.exp(-d_ij) - r_e2*beta(t)*S * E2_other/N_j*np.exp(-d_ij)
            dS += -beta(t)*S*I/N_i      # Needs to sum up dS and add first part of the equation
            dE1 = -dS - lmbda_1*E1
            dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
            dI = lmbda_2*E2 - mu*I
            dIa = lmbda_1*p_a*E1 - mu*Ia
            dR = mu*(I + Ia)
            gamma = 0       #Example 1/10, just an extension to experiment with immunity

            # put the values in the end of derivative (gamma*R for more exciting curves, immunity doesn't last forever)
            derivative.append(dS + gamma*R)
            derivative.append(dE1)
            derivative.append(dE2)
            derivative.append(dI)
            derivative.append(dIa)
            derivative.append(dR - gamma*R)
            # print(sum(derivative), "\n")          # Sum of derivatives should be zero (No loss or gain in population)
        return derivative

    def solution(self, u, t):
        n = len(t)
        n_reg = len(self.region)
        self.t = t
        self.S = np.zeros(n)
        self.E1 = np.zeros(n)
        self.E2 = np.zeros(n)
        self.I = np.zeros(n)
        self.Ia = np.zeros(n)
        self.R = np.zeros(n)
        SEIR_list = [u[:, i:i+6] for i in range(0, n_reg*6, 6)]
        for part, SEIR in zip(self.region, SEIR_list):
            part.set_SEIR_values(SEIR, t)
            self.S += part.S
            self.E1 += part.E1
            self.E2 += part.E2
            self.I += part.I
            self.Ia += part.Ia
            self.R += part.R

    def plot(self):
        plt.plot(self.t, self.S, '#1f77b4', label='S')      # matplotlib standard colors for blue, yellow, green and red
        plt.plot(self.t, self.I, '#ff7f0e', label='I')
        plt.plot(self.t, self.Ia, '#2ca02c', label='Ia')
        plt.plot(self.t, self.R, '#d62728', label='R')
        plt.xlabel('Time(days)')
        plt.ylabel('Population')
        plt.title(self.area_name)

if __name__ == '__main__':
    nor = RegionInteraction('Norway', S_0=5e6, E2_0=100, lat=60.4, long=8.4)        # Test for same plot in SEIR.py

    problem = ProblemInteraction([oslo,innlandet], 'Norway_east', beta=0.5)
    print(problem.get_population(), "\n")
    problem.set_initial_condition()
    print(problem.initial_condition, "\n") #non-nested list of length 12
    u = problem.initial_condition
    print(problem(u,0)) #list of length 12. Check that values make sense


    solver = SolverSEIR(problem,T=100,dt=1.0)
    solver.solve()
    problem.plot()
    plt.legend()
    plt.show()


# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oppgaveprosjekt IN1900> python SEIR_interaction.py
1.0100809386280782

1064979

[693494, 0, 100, 0, 0, 0, 371385, 0, 0, 0, 0, 0]

[-62.49098896472576, 62.49098896472576, -50.0, 50.0, 0.0, 0.0, -12.187832324277785, 12.187832324277785, 0.0, 0.0, 0.0, 0.0]
PS C:\Desktop\Python\Oppgaveprosjekt IN1900>
"""
