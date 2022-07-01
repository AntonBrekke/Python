#Exercise 5.10
#a)
import numpy as np
import sys

# Lager snarvei så jeg slipper å skrive hele filnavnet hver gang jeg kjører(se også på funksjonskallet):
# Låser også programmet til å kun lese informajson fra temp_{data}.txt dokumenter(se også på funksjonskallet)
print("")
print("The .txt file in the folder has to be named: temp_month_year.txt,\nfor example temp_jan_2012, but in input you only need month_year.")
print("")
data = input("Write .txt file (Ex: month_year as feb_2009):")
if data == "":
    sys.exit()
data2 = input("Write .txt file (Ex: month_year as oct_2014):")
if data2 == "":
    sys.exit()

# Lister som lagrer informasjon fra .txt dokumenter fra oppgave(ville egt kalt noe mer generelt, men oppgave ber om disse listenavnene)
oct_1945 = []
oct_2014 = []

def extract_data(filename):
    # Åpner .txt fil:
    infile = open(filename, 'r')

    temp_list = []      # Tom liste for å oppbevare midertidig informajson til tabell
    print("")
    print(infile.readline()) # Printer ut og leser vekk første linje

    # Splitter verdier i tekstdokument fra argument og legger til i temp_list
    for line in infile:
        words = line.split()    # Splitter alle ord i line
        for i in range(len(words)):     # looper gjennom alle verdier i line og legger dem til i temp_list
            temp_list.append(float(words[i]))
            if filename == (f'temp_{data}.txt'):     # Lagrer .txt verdier fra data i oct_1945
                oct_1945.append(float(words[i]))
            elif filename == (f'temp_{data2}.txt'):  # Lagrer .txt verdier fra data2 i oct_2014
                oct_2014.append(float(words[i]))

    # Bruker numpy til å regne verdier fra temp_list til tabell
    mean = np.mean(temp_list)
    max_temp = np.max(temp_list)
    min_temp = np.min(temp_list)
    # Printer ut liste
    print("Average\t|\tHighest temperature\t|\tLowest temperature|")
    print(f"  {mean:.1f}\t|\t\t{max_temp}\t\t|\t\t{min_temp}\t  |")
    print("")
    infile.close()

extract_data(f"temp_{data}.txt")      # Kaller funksjon med argument (gir info fra input)
extract_data(f"temp_{data2}.txt")     # Kaller funksjon med argument (gir info fra input)

# Kjøreeksempel fra terminal:
"""
PS C:\Desktop\python\Oblig uke 39 IN1900> python temp_read_write.py

Year: 1945. Month: October. Location: Blindern(Oslo).

Average |       Highest temperature     |       Lowest temperature|
  6.5   |               11.6            |               2.1       |


Year: 2014. Month: October. Location: Blindern(Oslo).

Average |       Highest temperature     |       Lowest temperature|
  8.9   |               13.6            |               2.3       |
"""

#b)
import sys # Trenger ikke, men for oversikts skyld

# Lager input for å kunne bestemme filnavn i terminal:
write_file = input("Name new file containing values from oct_1945 and oct_2014\n(Ex: temp_formatted.txt):")

if write_file == "":
    sys.exit()

def write_formatting(filename, list1, list2):
    # Åpner fil gitt i argument i write-modus:
    outfile = open(filename,'w')
    for i in range(len(list1)):     # Loop som legger til verdier fra funksjonsargument list1 og list2 inn i filename-argument
        outfile.write(f'{list1[i]}      {list2[i]}\n')
    outfile.close()

write_formatting(write_file, oct_1945, oct_2014)

# Kjøretest i terminalen:
"""
PS C:\Desktop\python\Oblig uke 39 IN1900> python temp_read_write.py
PS C:\Desktop\python\Oblig uke 39 IN1900>
"""

# Utskrift fra temp_formatted.txt:
"""
7.2      9.8
8.1      11.6
8.9      11.5
11.6      13.3
7.7      12.6
8.7      10.3
6.9      7.5
5.4      9.3
8.8      10.3
8.9      10.3
3.7      8.4
3.3      8.8
5.2      5.0
9.6      5.8
10.8      6.8
5.0      2.3
5.4      3.5
9.5      7.9
5.3      11.8
5.8      10.7
2.3      9.0
4.1      5.8
6.6      6.8
8.2      11.7
6.1      10.6
8.9      11.7
6.6      13.1
4.1      13.6
2.8      8.0
2.1      3.5
4.1      3.2
"""
