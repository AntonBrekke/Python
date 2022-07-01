import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-1,1,101)
J = np.linspace(-2,2,101)
x, y = np.meshgrid(I,J, indexing='xy')

l = np.sqrt(x**2 + y**2)
b = I**2
y_1 = y.copy(); y_2 = y.copy()
# Kode som regner nye y-verdier for konturet på en skillelinje b
for n in range(len(y[0])):
    for m in range(len(y[:,0])):
        if y[m,n] < b[n]:
            y_1[m,n] = b[n]
        elif y[m,n] > b[n]:
            y_2[m,n] = b[n]
# Kan være vrient å se hvorfor det funker, men print disse og se
"""
print(y)
print()
print(b)
print()
print(y_1)
print()
print(y_2)
"""
plt.contourf(x, y_1, l, 100, cmap='viridis')
plt.contourf(x, y_2, l, 100, cmap='jet')
plt.plot(I, b, 'w')
plt.ylim()
plt.show()
