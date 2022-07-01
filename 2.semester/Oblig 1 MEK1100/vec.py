from velfield import *

x, y, u, v = velfield(30)
plt.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])
plt.axis('equal')
plt.xlabel('x'); plt.ylabel('y')
plt.title('Vectorfield from exercise 3', weight='bold')

# plt.savefig('vec.png')
plt.show()
