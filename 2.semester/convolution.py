import numpy as np
import matplotlib.pyplot as plt


f1 = input('input function in python format: ')
f2 = input('input function in python format: ')

# Trapesmetoden
def int(f, t):
    dx = np.diff(t, axis=0)
    s = 0
    for i in range(0, len(f)-1):
        s += (f[i] + f[i+1])*dx[i] / 2
        # plt.plot(x[i], s, 'ro', markersize=3)
    plt.show()
    return s

# Implementerer unit-step funksjonen
def u(t):
    d = t.copy()    # For å unngå at x-arrayen endres (skjedde om jeg brukte u(x) og ikke lagde kopi av t)
    for i in range(len(d)):
        if d[i] > 0:
            d[i] = 1
            # print(i, t[i])
        else:
            d[i] = 0
            # print(i, t[i])
    return d

def convolution(t, f_1, f_2):
    tau = t.copy()  # Kan bare bruke t, men enklere å se konvensjonen
    dtau = np.sum(np.diff(t, axis=0), axis=0) / (np.size(t) - 1)
    s = np.zeros(np.shape(t))
    for n, i in enumerate(t):
        # s[n] = int(f_1(tau) * f_2(i - tau), tau) # Kan også bruke egendefinert trapes-integral
        s[n] = np.sum(f_1(tau) * f_2(i - tau), axis=0)*dtau  # Kan bruke numpy om man ikke gidder noe annet

    return s

# Av en eller annen veldig rar grunn må jeg dele opp funksjonene for positiv og negativ side
def f(t):
    return eval(f1)*u(t)

def g(t):
    return eval(f2)*u(t)

def h(t):
    return eval(f1)*u(-t)

def k(t):
    return eval(f2)*u(-t)

x = np.linspace(-20, 20, 1000)

plt.plot(x, f(x), color='#1f77b4', linestyle='--')
plt.plot(x, g(x), color='#ff7f0e', linestyle='--')
plt.plot(x, h(x), color='#2ca02c', linestyle='--')
plt.plot(x, k(x), color='purple', linestyle='--')

plt.plot(x, convolution(x, f, g), 'r')
plt.plot(x, -convolution(x, h, k), 'b')     # Må plotte med - foran fordi dataen kommer tilbake feil vei (av en eller annen grunn)
plt.show()
