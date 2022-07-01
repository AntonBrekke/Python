# 1
"""
a = 3*0.1 - 0.3
print(f'{a:.40e}')
b = 2**-54
print(f'{b:.40e}')
"""
# 2
a = 3602879701896397/2**55
b = 0.1
print("{:.60f}".format(a))
print("{:0.60f}".format(b))


p=0
for i in range(10):
    p += 0.01
    print(p)

rel_error = abs(1-0.09)*10
print(f'{rel_error:.60f}')
