import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5, 5, 101)
x, y = np.meshgrid(I, I, indexing='xy')

fig = plt.figure()
ax = fig.add_subplot(111)

dx = 0.1; dy = 0.1

corners = [(50,50,100,100)] #(35,85,70,100),(35,50,70,60)]
for C in corners:
    x1, x2 = C[0], C[2]
    y1, y2 = C[1], C[3]

    ax.plot([x[0, x1], x[0, x2]], [y[y1, 0], y[y1, 0]], 'r')   # Nederst 1
    ax.plot([x[0, x2], x[0, x2]], [y[y1, 0], y[y2, 0]], 'g')   # Høyre 2
    ax.plot([x[0, x2], x[0, x1]], [y[y2, 0], y[y2, 0]], 'b')   # Øverst 3
    ax.plot([x[0, x1], x[0, x1]], [y[y2, 0], y[y1, 0]], 'k')   # Venstre 4

    C1 = x[y1, x1:x2+1]
    C2 = y[y1:y2+1, x2]
    C3 = x[y2, x2:x1-1:-1]
    C4 = y[y2:y1-1:-1, x1]

    dC1 = np.diff(C1)
    dC2 = np.diff(C2)
    K = int(sum(dC2))
    int = sum(dC1)*sum(dC2)

print(int)
plt.show()
