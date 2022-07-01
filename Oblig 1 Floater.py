from math import sqrt
xpp = 1
xp = 2 - sqrt(5)
for i in range(19):
    x = 4*xp + xpp
    xpp = xp
    xp = x
    print(x)
import numpy as np
ans = (2-np.sqrt(5))**20
print(ans)
