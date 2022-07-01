import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd
from scipy import stats

g = 9.81

B1 = np.array([])
B2 = np.array([])

dBs = B1**2 - B2**2

# Faraday-effekten
L = 30e-3       # m
dL = 1e-3

thetaG_pos = np.array([0, 3.4, 3.4, 4.4, 5.4, 7.4])
thetaG_neg = -np.array([0, 2.0, 4.0, 4.8, 5.1, 6.2])
thetaG = np.concatenate((thetaG_neg[::-1], thetaG_pos))

thetaB_pos = np.array([0, 2.6, 5.2, 8.4, 9.0, 8.2])
thetaB_neg = -np.array([0, 0.4, 3.6, 6.0, 7.5, 6.3])
thetaB = np.concatenate((thetaB_neg[::-1], thetaB_pos))


thetaR_pos = np.array([0, 2.0, 2.8, 3.4, 4.4, 4.6])
thetaR_neg = -np.array([0, 1.2, 2.0, 2.2, 3.4, 4.6])
thetaR = np.concatenate((thetaR_neg[::-1], thetaR_pos))


I_pos = np.array([1, 1.5, 2, 2.5, 3])
I_neg = -I_pos.copy()
I = np.concatenate((I_neg[::-1], I_pos))

B_pos = np.array([0, 43, 63, 83, 102, 119]) * 1e-3      # T
B_neg = -B_pos.copy()
B = np.concatenate((B_neg[::-1], B_pos))


plt.plot(B, thetaG, 'limegreen', marker='X', label='data')
plt.plot(B, thetaB, 'cornflowerblue', marker='X', label='data')
plt.plot(B, thetaR, 'r', marker='X', label='data')

linregG = stats.linregress(B, thetaG)
linregB = stats.linregress(B, thetaB)
linregR = stats.linregress(B, thetaR)

VLG = linregG.slope; dVLG = linregG.stderr
VLB = linregB.slope; dVLB = linregB.stderr
VLR = linregR.slope; dVLR = linregR.stderr
print(f'V_G: {VLG / L}, std_G: {np.sqrt((dVLG/VLG)**2 + (VLG * dL / L**2)**2)}')
print(f'V_B: {VLB / L}, std_B: {np.sqrt((dVLB/VLB)**2 + (VLB * dL / L**2)**2)}')
print(f'V_R: {VLR / L}, std_R: {np.sqrt((dVLR/VLR)**2 + (VLR * dL / L**2)**2)}\n')

linefitG = np.poly1d(linregG[:2])
linefitB = np.poly1d(linregB[:2])
linefitR = np.poly1d(linregR[:2])

plt.plot(B, linefitG(B), 'darkgreen', label='linreg')
plt.plot(B, linefitB(B), 'blue', label='linreg')
plt.plot(B, linefitR(B), 'darkred', label='linreg')

plt.xlabel('B [mT]', weight='bold', fontsize=16)
plt.ylabel(r'$\theta$ [grader]', weight='bold', fontsize=16)
plt.legend(prop={'size': 14})
plt.show()
