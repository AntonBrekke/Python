def listadder(a,b):
    return [a_i + b_i for (a_i,b_i) in zip(a,b)]

x = [0,1,2]
y = [3,4,5]
c = listadder(x,y)
z = x + y
print(len(c)<len(z))
print(c == z)
print(c == zip(x,y))
print(c[0] == z[0] + z[len(c)])
print(z*len(c))
