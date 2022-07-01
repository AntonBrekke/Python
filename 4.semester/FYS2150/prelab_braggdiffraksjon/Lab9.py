import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc


"""
A Røntgenspektrometri på LiF-krystall (bremsestråling)
"""
# Konstanter:
h = 4.135e-16           #eVs
c = 3e8                 #m/s
m_e = 511/c**2          #keV/c^2

d_LiF = 200.5e-12       #m
d_KCl = (629e-12) /2    #m
U_R = 20                #kV


_2theta = np.arange(12, 22.5, 0.5)
I = np.array([92, 108, 136, 103, 140, 136, 162, 240, 272, 332, 444, 536,
              578, 664, 754, 814, 861, 894, 926, 946, 954])    #antall målinger
#print(_2theta)

plt.scatter(_2theta, I)
plt.plot(_2theta, I)
plt.show()

def U(theta_min, d):
    return 1.241e-6/ (2*d*np.sin(theta_min))

_2theta_min = 15*np.pi/180

U_eksp = U(_2theta_min/2, d_LiF)
print(U_eksp)


def _lambda(d,theta):
    return 2*d*np.sin(theta)

def lambda_min(E):
    E_max = np.max(E)
    lambda_min = h*c/E_max
    return lambda_min

"""
B Røntgenspektrometri på KCl-krystall (karakteristisk stråling)
"""
d_KCl = 629e-12/2   #m
lambda_alfa = 154.2e-12 #m
lambda_beta = 138.6e-12 #m

def _2theta(_lambda, d, n):
    return 2*np.arcsin(n*_lambda/(2*d))

_2theta_alfa1 = _2theta(lambda_alfa, d_KCl, 1)/np.pi*180
_2theta_alfa2 = _2theta(lambda_alfa, d_KCl, 2)/np.pi*180

_2theta_beta1 = _2theta(lambda_beta, d_KCl, 1)/np.pi*180
_2theta_beta2 = _2theta(lambda_beta, d_KCl, 2)/np.pi*180

print(_2theta_alfa1, _2theta_alfa2)
print(_2theta_beta1, _2theta_beta2)

U_R = 30e3          #V

step = 0.5
_2theta_1 = np.arange(22, 31.5 + step, step)
I1 = np.array([260 ,229 ,713, 802, 1051, 1271, 1888, 2029, 1552, 2033, 2635,
               3572, 4414, 3898, 2023, 305, 219, 171, 145, 129])

print(len(_2theta_1), len(I1))

_2theta_2 = np.arange(48.5, 61.5 + step, step)
I2 = np.array([72 ,91 ,86 ,112, 153, 192, 209, 227, 218, 164, 122, 108, 110, 88, 94, 114,
               195, 498, 595, 647, 619, 528, 270, 94, 90, 74, 81])
print(len(_2theta_2), len(I2))

plt.plot(_2theta_1, I1)
plt.plot(_2theta_2, I2)
plt.show()
exit()

"""
C Elektrondiffraksjon
"""
# Konstanter:
h = 4.135e-16           #eVs
c = 3e8
m_e = 511/c**2          #keV/c^2
lambda_c = 2.426e-12    #m

U = np.array([1,5,20,50,100]) #kV

def f(U, e=1):           #U er en vektor med enhet kV
    f = 1/np.sqrt(1 + (e*U)/(2*m_e*c**2))
    return f

def _lambda(U):                             #Uten relativistisk faktor, U i kV
    l = lambda_c * np.sqrt(511/(2*U))       #både 511 og U er i kV
    return l

#print(f(U))

indre_innerst = np.array([270, 268, 265, 254, 231, 245, 235, 230, 229, 216, 207]) * 1e-2 * 1e-2     # m
indre_ytterst = np.array([345, 320, 335, 315, 305, 294, 301, 294, 281, 275, 264]) * 1e-2 * 1e-2     # m

ytre_innerst = np.array([496, 484, 480, 456, 431, 435, 421, 426, 411, 400, 386]) * 1e-2 *1e-2       # m
ytre_ytterst = np.array([583, 551, 550, 541, 539, 507, 503, 496, 478, 470, 463]) * 1e-2 * 1e-2      # m

D_indre = (indre_innerst + indre_ytterst)/2
D_ytre = (ytre_innerst + ytre_ytterst)/2


# Finne lambda fra spenningen
R = 10e6 #Ohm
I = np.array([27, 29, 30, 32, 34, 36, 38, 39, 41, 43, 45]) * 1e-3 * 1e-3        # A
U = np.arange(3, 5 + 0.2, 0.2) - I * R *10**(-3)#keV
_lambda = _lambda(U)

print(_lambda/D_indre, _lambda/D_ytre)



#3)
L = 125e-3              #m
delta_L = 2e-3

phi_indre = _lambda/D_indre
phi_ytre = _lambda/D_ytre

delta_phi_indre = np.std(phi_indre)/np.sqrt(len(phi_indre))
delta_phi_ytre = np.std(phi_ytre)/np.sqrt(len(phi_ytre))


def d(phi):
    return 2*L*phi

def delta_d(d, phi, delta_phi, L=L, delta_L=delta_L):
    delta_d = d * np.sqrt((delta_phi/phi)**2 + (delta_L/L)**2)
    return delta_d

d10 = d(np.mean(phi_indre))
delta_d10 = delta_d(d10, np.mean(phi_indre), delta_phi_indre)

d11 = d(np.mean(phi_ytre))
delta_d11 = delta_d(d11, np.mean(phi_ytre), delta_phi_ytre)

print('d10 = ',d10, 'pm', delta_d10)
print('d11 = ', d11, 'pm', delta_d11)
print(d10/d11, np.sqrt(3))














































#
