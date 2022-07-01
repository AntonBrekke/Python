import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd

"""
E approx I siden linsene er så nærme
I = I0*cos^2(theta)
=> I / I0 = cos^2(theta)
=> E / E0 = cos^2(theta)
"""


sigma_light = 2       # Lux

dtheta1 = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) * np.pi / 180        # rad
dtheta2 = np.array([0, 10, 20, 30, 40, 45, 50, 60, 70, 80, 90]) * np.pi / 180        # rad

E_measured1 = np.array([138, 135, 123, 105, 83, 59, 36, 18, 7, 4])       # Lux
E_measured2 = np.array([2, 3, 7, 13, 16, 18, 17, 14, 9, 5, 2])       # Lux

# E = E_measured - sigma_light
E1 = E_measured1 / E_measured1[0]
# E1 = E1 - E1[-1]
cos_dat1 = np.cos(dtheta1)**2

# E2 = E_measured2 - sigma_light
E2 = E_measured2 / E_measured2[0]
E2 = E2 - E2[-1]
cos_dat2 = np.cos(dtheta2)**2

dtheta = np.linspace(0, 90, 400) * np.pi / 180      # rad
cos_dat = np.cos(dtheta)
data = cos_dat**2

# Husk at E1 = E / E0 = cos^2(theta)
lab = vd.polarisasjon()
lab.compare_theoretical(dtheta*180/np.pi, cos_dat)
lab.regdata(dtheta1*180/np.pi, E1, xlabel=r'$\theta$ [deg]', ylabel='E [Lux]', deg=1, show=True)

lab.compare_theoretical(dtheta*180/np.pi, cos_dat)
lab.regdata(dtheta2*180/np.pi, E2, xlabel=r'$\theta$ [deg]', ylabel='E [Lux]', deg=2, show=True)
