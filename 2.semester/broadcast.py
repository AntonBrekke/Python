import numpy as np
#
# x = np.linspace(-1, 1, 6)[:, None]
C = np.linspace(-1, 1, 5)[None, :]

A = np.array([1,2,3,4])[:,None]
#
# print(x)
# print(C)
# print(A)
#
print(A*C)
print(C*A)
#
# # Lage en nxn matrise
# n = 100
# X = np.linspace(1,n,n)[None,:]
# Y = np.ones((len(X[0,:]), 1))
# # Y = np.ones(np.shape(X.T))  # Funker også å transponere X
# prod = X*Y
# print(prod)
# # Snudd andre veien
# X = np.linspace(1,n,n)[:,None]
# Y = np.ones((1, len(X[:,0])))
# # Y = np.ones(np.shape(X.T))
# prod2 = X*Y
# print(prod2)
#
# # Eksempel: Jeg vil plotte sirkler med varierende radius
# import matplotlib.pyplot as plt
#
# theta = np.linspace(0, 2*np.pi, 300)[:,None]
# r = np.linspace(1, 5, 5)[None,:]    # På grunn av måten matplotlib plotter må vi legge på en akse langs x-retning der vi vil variere
#
# x = r*np.cos(theta)
# y = r*np.sin(theta)
#
# t = np.linspace(np.min([np.min(x), np.min(y)]), np.max([np.max(x), np.max(y)]), 100)
# zero = np.zeros_like(t)
#
# plt.plot(x, y)
# plt.plot(t, zero, 'k', zero, t, 'k', alpha=0.8)
# plt.axis('equal')
# plt.legend([f'r={i}' for i in r[0]], loc='upper right')
# plt.show()
#
#
# # Eksempel 2:
#
# f = lambda x, C: np.exp(-0.4*x)*np.sin(C*x)
#
# x = np.linspace(0, 10, 400)[:,None]
# C = np.linspace(1, 3, 3)[None,:]
#
# F = f(x,C)
#
# t = np.linspace(np.min(F), np.max(F), 100)
# zero_t = np.zeros_like(t)
# zero_x = np.zeros_like(x)
#
# plt.plot(x, F)
# plt.plot(x[:,0], zero_x, 'k', zero_t, t, 'k', alpha=0.8)
# plt.legend([f'C={c}' for c in C[0]], loc='upper right')
# plt.show()
