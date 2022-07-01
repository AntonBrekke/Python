import numpy as np

"""
u = np.zeros((3,6))

a = [1,2,3,4,5,6]
b = [6,5,4,3,2,1]
u[0,:] = a
u[1,:] = b

print(u,"\n")


u = [1,2,3,4,5,6,7,8,9]
a = [u[i:i+3] for i in range(0, len(u), 3)]
b = [u[i] for i in range(2, len(u), 2)]
print(a,"\n")
print(b,"\n")

u = [[1,2,3],[4,5,6],[7,8,9]]
a = [u[i:i+3] for i in range(0,len(u), 3)]
print(a, '\n\n')


S_0 = 1; E1_0 = 2; E2_0 = 3; I_0 = 4; Ia_0 = 5; R_0 = 6
u = np.zeros((2,6))
u[0,:] = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]

print(u)


words = ['Hei', 'på', 'deg', 'du']
words_list = words[:]
words_list[2] = 4
print(words_list[2])
print(words)


a = [1]
if type(a) == list:
    print('true')


N_list = *range(2,202,5),
print(type(N_list))


if True == False:
    print('1')
elif True == False:
    print('2')
elif True == True:
    print('3\n')


class Test:
    def __init__(self):
        self.i = 0

    def __call__(self):
        self.i += 1


object = Test()
print(object.i)     # 1st
object()
print(object.i)     # 2nd
object()
print(object.i)     # 3rd


class super:
    def __init__(self, a):
        self.a = a

class Test_super(super):
    def __init__(self, a):
        super.__init__(self, a)

test_super = Test_super(6)
print(test_super.a)
"""

print('\nOriginal A')
u = np.zeros((5, 4))
for i in range(1, 6):
    a = i
    b = i+1
    c = i+3
    d = i+5
    u[i-1,:] = [a, b, c, d]

print(u, '\n')
print('Transposed A')
A = np.zeros((4,5))
for i in range(5):
    a, b, c, d = u[i,:]
    A[:,i] = a, b, c, d
print(A,'\n')


list = []
for i in range(5):
    list += 1, 2, 3
print(list)
