# Exercise 7.4 oppgaveheftet

def atm_moon(filename):
    dict = {}       # Lager tom dictionary
    infile = open(filename,'r')
    infile.readline()       # Leser vekk første linje
    for line in infile:     # Går gjennom hver linje i infile
        words = line.split(' ; ')   # Splitter hver linje på ' ; '
        for i in words:             # For hvert element jeg splittet i forrige linje kjører jeg kode i loop
            s = i.split(' - ')      # Splitter elementer på ' - '
            s[0] = s[0].upper()     # Gjør element 0 til uppercase
            s[1] = float(s[1].replace(',', '')) # Fjerner komma og gjør til float (bytter ut komma med ingenting)
            dict[s[0]] = s[1]       # Setter key s[0] med value s[1] i dict
    return dict

print(atm_moon('atm_moon.txt'))

# Kjøreeksempel fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 42 IN1900> python atm_moon.py
{'HELIUM 4': 40000.0, 'NEON 20': 40000.0, 'HYDROGEN': 35000.0, 'ARGON 40': 30000.0, 'NEON 22': 5000.0, 'ARGON 36': 2000.0, 'METHANE': 1000.0, 'AMMONIA': 1000.0, 'CARBON DIO
XIDE': 1000.0}
"""
