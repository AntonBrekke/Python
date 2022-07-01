d = {-2:6, 6:3, 3:7}
for i in d:
    print(i, d[i]) # i er indexverdi, d[i] er tilhørende verdi

"""
Kan ikke skrive d = {2:1, 2:3}.
Python vet ikke hva den skal mappe
i regel 2 når den har 2 forskjellige
nøkler. Dictionaries kommer ikke i rekkefølge,
men er heller som en sekk med nøkkelverdier.
"""
# Alternativ måte:
d = dict(a = 3, b = 7, c = 1)
"""
Ulempe: Kan ikke bruke tall på venstreside
dvs. dict(1 = 2, 5 = 9) er ikke lov.
"""
# Legg til et nytt par til d:
d["Tall"] = 5
# Legg til en hel dictionary til d:
d.update(d2)
# Fjerne et par (a,b) fra dictionary:
del d["Tall"]
"""
Trenger kun å oppgi regel-verdi
"""
# Teste om en nøkkel finnes i en dictionary:
key in d # En boolsk verdi
verdi = d[key] # Dersom key ikke finnes kommer feilmelding
verdi = d.get(key)  # Returnerer "none" dersom key ikke finnes

a = {"Berkeley": "US", "Cambridge": "UK"}
key = "Berkeley"
if key in a:
    print(f"Regelen {key} finnes i a")

# Løpe over elementenei sortert rekkefølge:
for key in sorted(d):
    .
# Løpe over elementene i usortert rekkefølge:
for key in d:
    .

d = {"Paris":2, "London":6, "Madrid":8}
list(d.keys()) -> ["Paris", "London", "Madrid"]
list(d.values()) -> [2, 6, 8]



# Vanlig eksamensoppgave
# Datafil:
MB.0000     0.00096
MB.0002     0.24787
MB.0005     0.2779
MB.0006     0.29428
MB.0010     0.61225
# Program
bloodtest = {}
infile = open("blood_test.txt", 'r')
for line in infile:
    words = line.split()
    bloodtest[words[0]] = float(words[1])
infile.close()
print(bloodtest["MB.0005"])     # 0.2779

# Datafil:
Oslo        21.8    "Norway"
Bergen      17.6    "Norway"
London      18.1    "UK"
Berlin      19      "Germany"
Paris       23      "France"
Roma        26    " "Italy"
Helsinki    17.8    "Finland"
# Program:
infile = open("cityinfo.txt",'r')
data = {}
for line in infile:
    words = line.split()
    data[words[0]] = [float(words[1]), words[2]]
infile.close()
print(data["Paris"])        # [23.0, ""France""]
print(data["Paris"][0])     # 23.0
print(data["Paris"][1])     # "France"
