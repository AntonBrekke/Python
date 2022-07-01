from math import *

formula = input('Type a formula involving x: ')

formulacode = f'''
def f(x):
    return {formula}
'''
exec(formulacode)

x = float(input('Type x:'))

result = f(x)
print(f'{formula} for {x} is {result}')
