# Oppgave 4.2 Primer
import sys

try:
    F = sys.argv[1]
    F = float(F)
except IndexError:
    print('You failed to provide a command line argument')
    exit()
except ValueError:
    print('Wrong format of argument')
    exit()
C = (F - 32)*5/9

print(f"{F} degrees Fahrenheit is {C} degrees Celcius")
