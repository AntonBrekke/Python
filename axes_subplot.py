import matplotlib.pyplot as plt
import numpy as np

"""
Eksempel:
"""
n_list = [20, 25, 50, 150]
fig, axes = plt.subplots(2, 2, sharex='all', sharey = 'all')
fig.suptitle('Compare methods')
m = 0
n = 0
for i in range(len(n_list)):
    time_points = np.linspace(0, 8*np.pi, n_list[i])
    if n > 1:
        n = 0
        m += 1
    x,t = MP.solve(time_points)
    axes[m,n].plot(t,x,'r--', label = 'Euler Midpoint')
    x,t = Heun.solve(time_points)
    axes[m,n].plot(t,x,'b--', label = 'Heuns method')
    x,t = RK4.solve(time_points)
    axes[m,n].plot(t,x,'g--', label = 'RungeKutta4')
    axes[m,n].set_title(f'n = {n_list[i]}', fontsize=10)
    axes[m,n].legend(loc=3, prop={'size': 6})
    n += 1
    
plt.show()

"""
Eksempel 2 for kjappe plots:
"""
n_list = [20, 25, 50, 150]
for i in range(len(n_list)):
    plt.subplot(221+i )
    time_points = np.linspace(0, 8*np.pi, n_list[i])
    x,t = MP.solve(time_points)
    plt.plot(t,x,'r--', label = 'Euler Midpoint')
    x,t = Heun.solve(time_points)
    plt.plot(t,x,'b--', label = 'Heuns method')
    x,t = RK4.solve(time_points)
    plt.plot(t,x,'g--', label = 'RungeKutta4')
    plt.title(f'n = {n_list[i]}', fontsize=10)
    plt.legend(loc=3, prop={'size': 6})
plt.show()
