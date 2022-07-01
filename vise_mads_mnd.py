import numpy as np
import matplotlib.pyplot as plt
import random

months = ['Jan', 'Feb', 'Mar',
          'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep',
          'Oct', 'Nov', 'Des']

t = np.linspace(1, 12, 12)

mat = [random.randrange(2000, 4000) for i in range(0, 12)]
hus = [random.randrange(2000, 4000) for i in range(0, 12)]
forsikring = [random.randrange(2000, 4000) for i in range(0, 12)]

plt.plot(t, mat)
plt.plot(t, hus)
plt.plot(t, forsikring)

ticks = *range(1,13),
plt.xticks(ticks, labels=months)
plt.show()
