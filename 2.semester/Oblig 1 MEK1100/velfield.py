import numpy as np
import matplotlib.pyplot as plt

def velfield(n):
    I = np.linspace(-0.5*np.pi, 0.5*np.pi, n)
    x, y = np.meshgrid(I, I, indexing='xy')

    u = np.cos(x)*np.sin(y)
    v = -np.sin(x)*np.cos(y)
    return x, y, u, v
