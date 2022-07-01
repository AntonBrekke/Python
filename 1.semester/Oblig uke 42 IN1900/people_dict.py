# Exercise 7.6 oppgaveheftet

# a)
def read_person_data(filename):
    person_data = {}    # Lager tom dictionary for å lagre data
    with open(filename,'r') as infile:
        for line in infile:     # Går gjennom linjer i infile
            words = line.split(',')
            words[2] = words[2].strip('\n')    # Stripper \n fra words[2]
            # Legger til data med dict[key] = value, stripper whitespace foran og bak words[1] og words[2]
            person_data[words[0]] = {'Age': int(words[1].strip()), 'Gender': words[2].strip()}
    return person_data

read_person_data('people_dict.txt')

# b)

def write_person_data(data_dict, filename):
    with open(filename,'w') as outfile:     # Åpner nytt dokument
        for key in data_dict:           # Går gjennom keys i argument data_dict (er en dictionary)
            Age = data_dict[key]['Age']     # Lagrer tallverdi til 'Age' pr. key i data_dict i Age
            Gender = data_dict[key]['Gender']       # Lagrer streng til 'Gender' pr. key i data_dict i Gender
            outfile.write(f'{key}, {Age}, {Gender}\n')  # Skriver inn key, verdi og streng i outfile

write_person_data(read_person_data('people_dict.txt'), 'write_person_data.txt')

# Kjøreeksempel fra terminal (a og b):
"""
PS C:\Desktop\Python\Oblig uke 42 IN1900> python people_dict.py
PS C:\Desktop\Python\Oblig uke 42 IN1900>
"""
