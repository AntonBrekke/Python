# Exercise 1.4 oppgaveprosjekt 2020
# Anton Brekke

import numpy as np
import matplotlib.pyplot as plt
from SEIR_interaction import *

# a)
# Function that reads file with county-data and stores as RegionInteractiojn-instances in list
def read_file(filename):
    with open(filename, 'r') as infile:     # ALternative: infile = open(filename, 'r')
        RegionInteraction_list = []
        for line in infile:
            words = line.split(';')
            m = 0
            for i in words:
                words[m] = words[m].replace('\t','').replace('\n','').lstrip(' ')       # Removes unneccesary spaces and marks
                m += 1
            # Example form: RegionInteraction('Norway',S_0=5e6, E2_0=100, lat=60.4, long=8.4 )
            area_name = words[1]; S_0 = float(words[2]); E2_0 = float(words[3]);
            lat = float(words[4]); long = float(words[5])
            RegionInteraction_list.append(RegionInteraction(area_name, S_0, E2_0, lat, long))

    return RegionInteraction_list           # List with instances of RegionInteraction

# print(read_file('fylker.txt'))            # Test to see if function works


# b)
# Function making subplots of all regions of instance RegionInteraction
def covid19_Norway(beta_19, filename, num_days, dt):
    # read file and create list of RegionInteraction instances
    region_list = read_file(filename)
    # create problem, an instance of ProblemInteraction
    problem = ProblemInteraction(region_list, 'Norway', beta=beta_19)
    # create the solver, an instance of SolverSEIR
    solver = SolverSEIR(problem, T=num_days, dt=dt)
    # call the method solve
    solver.solve()
    plt.figure(figsize=(9, 12)) # set figsize
    plt.suptitle(problem.area_name)
    index = 1
    # for each part in problem’s attribute region:
    for region in problem.region:
        plt.subplot(4,3,index)
        # Call plot method from current part
        region.plot()
        plt.title(f'{region.name}')
        index += 1
    plt.subplot(4,3, index)
    plt.subplots_adjust(hspace = 1.0, wspace=0.5)
    # Call plot method from problem
    problem.plot()
    plt.legend(loc='center right', prop={'size':10}, bbox_to_anchor=(1.4, 0.5))
    plt.show()

if __name__ == '__main__':

    covid19_Norway(beta_19=0.5, filename='fylker.txt', num_days=100, dt=1.0)


# c)
from datetime import date


date_list = [                         # Nested list containing intervals in lists, elements of date() instances from datetime-module
[date(2020, 2, 15), date(2020, 3, 14)],
[date(2020, 3, 15), date(2020, 4, 20)],
[date(2020, 4, 21), date(2020, 5, 10)],
[date(2020, 5, 11), date(2020, 6, 30)],
[date(2020, 7, 1), date(2020, 7, 31)],
[date(2020, 8, 1), date(2020, 8, 31)],
[date(2020, 9, 1), date.today()]
]
R_list = [4.0, 0.5, 0.4, 0.8, 0.9, 1.0, 1.1]        # R-list with R-values corresponding to intervals in date_list
# R_list = [1.0, 0.5, 1.4, 3.8, 0.9, 1.0, 1.1]      # Example-list for different plot
# R_list = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]      # Test list to compare result in b and c

# Function calculating difference in intervals and adding them up
def calculate_days(date_list):
    days_list = []     # t = 0 is the first date in the first intervsl
    delta = 0
    for i in range(len(date_list)):
        delta += abs(date_list[i][1] - date_list[i][0]).days + 1  # Module doesnt count end days, so + 1 (tested on website for calculating difference between dates)
        days_list.append(delta)
    return days_list

# print(calculate_days(date_list))          # Checking if list makes sense

class beta_fhi:
    def __init__(self, date_list, R_list):
        self.days_list = calculate_days(date_list)
        self.R_list = R_list
        self.i = 0      # Store index in constructor so it doesn't get lost in call, have to start on 0
        self.R = 0      # Just have to define R (so it exists), value means nothing since I re-define value in function and it can be made in constructor or __call__

    def __call__(self, t):
        r_ia = 0.1; r_e2 = 1.25; lmbda_1 = 0.33; lmbda_2 = 0.5; p_a = 0.4; mu = 0.2
        R_list = self.R_list; days = self.days_list;
        if t > days[self.i]:            # If t goes past interval, update index and move to next interval
            self.i += 1
        if t <= days[self.i]:           # If t is in interval of days, R is the corresponding value
            self.R = R_list[self.i]
        beta = self.R/(r_ia/mu + r_e2/lmbda_2 + 1/mu) # formula
        return beta

if __name__ == '__main__':

    beta_fhi = beta_fhi(date_list, R_list)
    days_total = beta_fhi.days_list[-1]
    covid19_Norway(beta_19=beta_fhi, filename='fylker.txt', num_days=days_total, dt=1.0)


# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oppgaveprosjekt IN1900> python covid19.py
PS C:\Desktop\Python\Oppgaveprosjekt IN1900>
"""
