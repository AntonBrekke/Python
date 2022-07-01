infile = open('Fdeg.txt', 'r')

infile.readline()
infile.readline()
infile.readline()

Fdegrees = []
Cdegrees = []
for line in infile:
    words = line.split()
    F = float(words[-1])
    C = (F - 32)*5/9
    Fdegrees.append(F)
    Cdegrees.append(C)

infile.close()

outfile = open('outfile.txt','w')

for F, C in zip(Fdegrees, Cdegrees):
    outfile.write(f'{F}\t|{C:7.2f}\n')

outfile.close()

# Lese tekstfil i terminal: more <Filnavn>
