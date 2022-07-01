import FYS2150_VizDat as vd
import numpy as np

x = np.linspace(1, 10, 50)
y = 0.5*x**2 + np.random.uniform(0, 10, x.shape)
p = vd.Visualize(x, y, color='r')
p.logreg(show=True)


# Tester med labdata
r = 0.5e-3 * np.array([10, 15, 29, 31.65, 38, 26.5, 25.05, 23.05, 20.3, 17.1, 18.1, 17.9])   # m
vt = 1e-3 * np.array([732, 1098, 1830, 1985, 2730, 1996, 1830, 1996, 1689.2, 1425, 1568.6, 1568.6])  # m

dat = vd.Visualize(r, vt)
dat1 = vd.Visualize(r[:6], vt[:6], color='r')
dat2 = vd.Visualize(r[6:], vt[6:], color='g')

dat.logreg()
dat1.logreg()
dat2.logreg()
# vd.show()

lab = vd.gammastraling([1], [1])
lab.logreg()
vd.show()
