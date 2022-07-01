import matplotlib.pyplot as plt
from streamfun import *

fig, ax = plt.subplots(1,2)
values = {0:(5, '(i)'), 1:(30, '(ii)')}
for key in values:
    x, y, psi = streamfun(values[key][0])
    ax[key].grid(True)
    ax[key].contour(x, y, psi)
    ax[key].axis('equal')
    ax[key].set_xlabel('x'); ax[key].set_ylabel('y');
    ax[key].set_title(f'{values[key][1]} n={values[key][0]}')

plt.suptitle(r'Contour of $\psi=cos(x)cos(y)$', weight='bold')
plt.tight_layout()
plt.savefig('strlin.png')
plt.show()
