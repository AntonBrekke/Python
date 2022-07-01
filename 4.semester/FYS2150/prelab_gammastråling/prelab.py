import FYS2150_VizDat as vd
import numpy as np
import matplotlib.pyplot as plt


lab = vd.gammastraling()
lab.Poisson(k=10000, dt=0.1, percentage=1)

k_data = np.loadtxt('poisson.csv')
# print(k_data)

lab.Poisson(k_arr=k_data[1:])
print(lab.m, lab.sigma)

lab.GeigerMuller(nr=23, nb=2, A=1e6, r=2, d=20)

z = np.array([0, 4, 8, 12, 16, 20, 24]) * 1e-3      # m
n = np.array([13.7, 12.4, 11.0, 9.7, 8.9, 7.9, 7.1])        # 1/s

lab.n_and_z_expreg(z, n, color='r')
lab.find_z_from_absorbed(mu=253, perc_absorbed=95)

lab.estimate_dispersion(E1=662, E2=1275, I1=410, I2=773)

spectrum = np.loadtxt('spektrum.csv')       # I
lab.plot_spectrum(spectrum, dE=2, start_stop_top=[650, 975], show=True)
