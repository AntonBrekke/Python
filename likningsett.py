import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,0,-3,2,4], [5,6,7,8,-9],[1,1,1,1,1],[0,0,0,1,0],[2,-3,2,-3,4]])
ANS = np.array([[14], [51], [10], [4], [-13]])
V = ['x', 'y', 'z', 'w', 'q']
Solve = np.linalg.inv(A).dot(ANS)
for i in range(len(V)):
    print(f'{V[i]} = {Solve[i][0]:.10f}\n')


A = np.array([[2,1],[3,4]])
print('A^-1\n', np.linalg.inv(A))

# Tegner et smileyfjes med tåre for å symbolisere smerten gjemt på innsiden
t = np.linspace(0,2*np.pi, 100)
x = 10*np.cos(t) - 3    # Hvorfor jeg valgte å forskyve med -3 er godt spørsmål
y = 10*np.sin(t)
plt.plot(x,y,'k')
t1 = np.linspace(np.pi, 2*np.pi, 100)
x1 = 5.5*np.cos(t1) - 3
y1 = 4.5*np.sin(t1) - 3
plt.plot(x1, y1,'k')
plt.plot([5.5*np.cos(np.pi)-3, 5.5*np.cos(2*np.pi)-3],[4.5*np.sin(np.pi)-3, 4.5*np.sin(2*np.pi)-3], 'k')
j_list = np.linspace(0, 2*np.pi,700)
for i in j_list:
    plt.plot([1,0.8*np.cos(i)+1],[1,0.8*np.sin(i)-1], 'royalblue')
    plt.plot([0.8,np.cos(i)+0.8],[2.5,np.sin(i)+2.5], 'k')
    plt.plot([-7,np.cos(i)-7],[2.5,np.sin(i)+2.5], 'k')
plt.axis("equal")
plt.show()
