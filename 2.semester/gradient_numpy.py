import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5,5,11)
x, y = np.meshgrid(I, I, indexing='xy')
f = x
dfdx = np.gradient(f, axis=1)
dfdy = np.gradient(f, axis=0)
print(f)
print(dfdx)
print(dfdy)
"""
Med indexing='xy' differansierer axis=1
langs x-retning i arrayen og axis=0
langs y-retning i arrayen. Med indexing = 'ij'
blir det motsatt.
"""
# L = np.sqrt(grad[0]**2 + grad[1]**2)
# plt.contourf(x, y, L, 200)
# plt.show()
