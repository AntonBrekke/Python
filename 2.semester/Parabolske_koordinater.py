import sympy as sp
import numpy as np

u, v = psi = sp.symbols('u, v', real=True)
rv = (2*u*v, u**2-v**2)

def basisvektorer(psi, rv):
    b = np.zeros([len(psi), len(rv)], dtype=object)
    for i, ui in enumerate(psi):
        for j, rj in enumerate(rv):
            b[i, j] = sp.simplify(rj.diff(ui, 1))
    return b

def skaleringsfaktorer(b):
    h = np.zeros([b.shape[0]], dtype=object)
    for i, s in enumerate(np.sum(b**2, axis=1)):
        h[i] = sp.simplify(sp.sqrt(s))
    return h

def enhetsvektorer(psi, rv):
    b = basisvektorer(psi, rv)
    hi = skaleringsfaktorer(b)
    return b / hi[None,:], hi

e, hi = enhetsvektorer(psi, rv)

print(e); print(hi)

# Lager skalarfelt f
f = (1-u**2)*(1-v**2)

N = 20
ui = np.broadcast_to(np.linspace(0, 1, N)[:, None], (N, N))
vi = np.broadcast_to(np.linspace(-1, 1, N)[None, :], (N, N))
fj = sp.lambdify((u, v), f)(ui, vi)

import matplotlib.pyplot as plt
plt.contourf(ui, vi, fj)
plt.show()

# Mer interessant å se på det i kartesiske koordinater
mesh = []
for rj in rv:
    mesh.append(sp.lambdify((u,v), rj)(ui, vi))
x, y = mesh
plt.contourf(x, y, fj)
plt.show()

df = np.array((1/hi[0]*f.diff(u, 1), 1/hi[1]*f.diff(v, 1)))
print(df)

gradf = e[0]*df[0] + e[1]*df[1]
print(gradf)

dfdxi = sp.lambdify((u,v), gradf[0])(ui, vi)
dfdyi = sp.lambdify((u,v), gradf[1])(ui, vi)
plt.contourf(x, y, fj)
plt.quiver(x, y, dfdxi, dfdyi, scale=20)
plt.show()
