

a = range(0, 10)
print(a)

numbers = [1,2,3,4]
more_numbers = [*numbers, 5,6,7]

print(more_numbers)


def adder1(a,b,c):
    return f'sum:{a+b+c}'

print(adder1(1,2,3))
# print(adder1(1,2,3,4,5)) # Dette gir feilmelding

def adder2(*num):
    return f'sum:{sum(num)}'

print(adder2(1,2,3,4,5,6,7,8,9))
print(adder2(*range(101),))
