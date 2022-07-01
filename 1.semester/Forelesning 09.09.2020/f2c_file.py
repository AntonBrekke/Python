infile = open('Fdeg1.txt', 'r')

infile.readline()
infile.readline()
infile.readline()

line = infile.readline()
words = line.split()

F = float(words[-1])

C = (F - 32)*5/9

print(f'{F} degrees Fahrenheit is {C} degrees Celcius')
