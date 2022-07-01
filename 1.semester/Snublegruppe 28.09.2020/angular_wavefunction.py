# Exercise 5.10 Fysikkheftet
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 1000)

def p_0_2(theta):
    return 0.5*(3*np.cos(theta)**2-1)
def p_1_2(theta):
    return 3*np.sin(theta)*np.cos(theta)
def p_2_2(theta):
    return 3*np.sin(theta)**2

def Ri(P, theta):
    return np.abs(P(theta))

P_list = [p_0_2, p_1_2, p_2_2]
P_title = [r"$P_{2}^0$", r"$P_{2}^1$", r"$P_{2}^2$"]        # Man kan bruke Latex-kode i matplotlib (!!!)
for title, P in zip(P_title, P_list):
    a = Ri(P, theta)*np.sin(theta)
    b = Ri(P, theta)*np.cos(theta)

    plt.title(title)
    plt.plot(a, b, 'b')
    plt.plot(-a, b, 'b')
    plt.axis()
    # plt.legend()
    plt.show()
