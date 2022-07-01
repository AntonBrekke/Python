# Forelesning 09.09.2020

"""
Eval evaluerer et uttrykk 's'
eval(r = 1 + 1) er ulovlig, fordi argumentet
her er en setning, ikke et uttrykk.
Men man kan bruke 'exec' til å omgjøre en eller flere
setninger til et uttrykk
"""

from math import *

formula = input('Type a formula involving x: ')
# formula = "utrykket fra terminalen"

formulacode = f'''
def f(x):
    return {formula}
'''
exec(formulacode)

x = float(input('Type x:'))

result = f(x)
print(f'{formula} for {x} is {result}')

"""
Input printer en melding ut i terminalen,
og returnerer teksten du skriver i terminalen
tilbake som en streng. Derfor er exec kritisk
for at dette programmet skal kjøre.
"""

# File example:
"""
Average rainfall (in mm) in Rome: 1188
months between 1782 and 1970
Jan 81.2
Feb 63.2
Mar 70.3
Apr 55.7
May 53.0
Jun 36.4
Jul 17.5
Aug 27.5
Sep 60.9
Oct 117.7
Nov 111.0
Dec 97.9
Year 792.9

How do we read such a file?
"""
# Basic file-reading:
infile = open('data.txt', 'r')  # Open file, r means read
for line in infile:
    # do something with line
infile.close()                  # Close file


# Modern with statement

# Read all lines at once into a list of strings:
lines = infile.readlines()
infile.close()

for line in lines:
    # process line

"""
All the code for processing the file is an
indented block.
The file is automatically closed.
"""

# Processing line with split:
months = []
values = []
for line in lines:
    words = line.split() # Split splitter setninger til enkelt ord
    if words[] != 'Year':
        months.append(words[0])
        values.append(values[0])

# Writing data to a file
outfile = open(filename, 'w')

for data in somelist:
    outfie.write(sometekst + '\n')

outfile.close()
