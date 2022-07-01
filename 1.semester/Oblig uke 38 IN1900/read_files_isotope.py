# Exercise 5.7
infile = open('Oxygen.txt','r')     # Åpner fil
infile.readline()       # Leser gjennom første linje fordi den er irrelevant

m_i = []     # Vekt av isotop
w_i = []     # Natural abundance

for line in infile:     # For hver line i infile:
    words = line.split()        # Splitter hvert ord i textfile ved space så jeg får hele nummeret med gitt index i en linje
    m_i.append(float(words[1]))     # Appender verdi i text-document med index 1
    w_i.append(float(words[-1]))    # Appender verdi i text-document med index -1

M = 0
for n in range(len(m_i)):       # Summerer vekt av isotop multiplisert med abundancy
    M += m_i[n]*w_i[n]
print("")
print(f'The mass of Oxygen is {M:.4f}g/mol')        # Printer resultat

infile.close()      # Closes file

# Kjøretest i terminal:
"""
Terminal> python read_files_isotope.py
The mass of Oxygen is 15.9994g/mol
"""
