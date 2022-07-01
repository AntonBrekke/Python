""""
Eksempel på hvordan å definere metoder utenfor klassen
""""

class nomethods():
    def __init__(self):
        pass

def printstring(self, string):
    print(string)

nomethods.method_name = printstring

a = nomethods()
a.method_name('Slik definerer man metoder utenfor klassen')
