# a)
d = {3:5, 6:7}
e = {4:6, 7:8}
d.update(e)
print(d)

# b)
d = {3:5, 6:7}
e = {4:6, 7:8}
d.update(e)
d.update(e)
print(d)

# c)
d = {6:100}
e = {6:6, 7:8}
d.update(e)
print(d)
