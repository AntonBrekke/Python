# Exerecise 8.1 oppgaveheftet

class People:
    # Konstruktør som lagrer arguementer som attributer
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self,name):     # Metode for å endre navn og lagre i attribut
        self.name = name

    def change_age(self,age):       # Metode for å endre alder og lagre i attribut
        self.age = age

    def change_gender(self,gender): # Metode for å endre kjønn og lagre i attribut
        self.gender = gender

    def __str__(self):              # Metode for å printe ut lagrede attributer
        s = f'{self.name}, {self.age}, {self.gender}'
        return s

a = People('John', 55, 'Male')    # Lager object med argumenter
a.change_name('Louise')         # Kaller på metode for å endre navn
a.change_gender('Female')       # Kaller på metode for å endre kjønn
print(a)                        # Printer ut metode

# Kjøretest i terminal:
"""
PS C:\Desktop\Python\Oblig uke 43 IN1900> python class_people.py
Louise, 55, Female
"""
