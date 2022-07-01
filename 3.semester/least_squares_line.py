import numpy as np
import matplotlib.pyplot as plt

def least_squares_line(x, y, N):
    """
    La x og y være to arrays med
    korresponderende punkter i xy-planet,
    og N være graden på polynomet.
    Kan bytte ut x.T**n og x**i med andre
    generelle funskjoner som np.sin(n*x.T)
    og np.sin(i*x)
    """
    X = np.ones((len(x), N+1))
    for n in range(1, N+1):
        X[:,n] = x.T**n
    XT = X.T
    b = y.T.copy()
    beta = np.dot(np.linalg.inv(np.dot(XT, X)), np.dot(XT, b))
    plt.scatter(x, y, label='Datapoints with noise')
    f = 0
    for i in range(len(beta)):
        f += beta[i]*x**i
    plt.plot(x, f, 'r', label=f'Fitted line polynomial deg {N}')
    plt.legend()
    plt.show()

M = 150
np.random.seed(2021)
sigma = np.random.normal(0, 0.1, M)
x = np.linspace(0, 10, M)
# y = x**3 - 8*x**2 + sigma         # Annet eksempel, kan gjøres eksakt med polynomer som har høyere eller lik grad
y = np.exp(-0.3*x)*np.sin(2*x) + sigma

plt.plot(x, y-sigma, 'k', label='Exact curve')

least_squares_line(x, y, 10)
