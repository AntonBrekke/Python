import numpy as np
import matplotlib.pyplot as plt
import FYS2150_VizDat as vd

data = np.loadtxt('faraday.csv')
B = data[:,0]
theta = data[:,1]

def sort():
    for i in range(len(theta)):
        for j in range(i+1, len(theta)):
            if theta[i] > theta[j]:
                theta[i], theta[j] = theta[j], theta[i]
                B[i], B[j] = B[j], B[i]
# sort()
B = np.sort(B) * 30e-3          # B*L, Tm
theta = np.sort(theta)      # grader

print(theta, B)

lab = vd.magnetisme()
lab.findDparnorm(a_par=20, a_norm=2)

lab.regdata(theta, B, show=True)
