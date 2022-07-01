import numpy as np

I = np.linspace(0, 1, 5)
x, y = np.meshgrid(I, I, indexing='xy')
print(f'{x}\n\n{y}\n\n\n\n')

I = np.linspace(0, 1, 5)
x, y = np.meshgrid(I, I, indexing='ij')
print(f'{x}\n\n{y}')
