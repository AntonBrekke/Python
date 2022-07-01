import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

np.random.seed(0)
x = np.linspace(0, 10, 11)
y = np.array(np.random.normal(0, 5, 11))

f1 = interpolate.interp1d(x, y, kind='cubic')
f2 = interpolate.interp1d(x, y, kind='linear')

xnew = np.linspace(0, 10, 100)

fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle('Scipy interpolation 1d', weight='bold')
ax1.plot(x, y, 'ko')
ax2.plot(x, y, 'ko')
ax1.plot(xnew, f1(xnew), '--', color='r', label='cubic')
ax2.plot(xnew, f2(xnew), '--', color='royalblue', label='linear')
ax1.legend(); ax2.legend()
plt.show()
