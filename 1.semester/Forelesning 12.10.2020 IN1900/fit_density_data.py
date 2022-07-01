#Exercise 5.18 Langtangen
import numpy as np
import matplotlib.pyplot as plt
from read_density_data import read_data

# a)
def fit(x, y, deg):
    plt.plot(x,y,'ro')
    for d in deg:
        coeff = np.polyfit(x,y,d)
        poly = np.poly1d(coeff)
        y_fitted = poly(x)
        plt.plot(x, y_fitted)
    # plt.show()

# b)
for i, filename in enumerate(['density_water.txt','density_air.txt']):
    temp, dens = read_data(filename)
    plt.subplot(2, 1, i+1)
    fit(temp, dens, [1,2])

plt.show()
