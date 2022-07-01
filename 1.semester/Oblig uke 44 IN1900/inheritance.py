# Exercise 9.4 oppgaveheftet

# a)
class Mammal:
    def info(self):
        return f"I have hair on my body."

    def identity_mammal(self):
        return f"I am a mammal."

# b)
class Primate(Mammal):
    def info(self):
        return Mammal.info(self) + f" I have a big brain."

    def identity_primal(self):
        return Mammal.identity_mammal(self)

# c)
class Human(Primate):
    def info(self):
        return Primate.info(self) + f" I am a primate."

    def identity_human(self):
        return Mammal.identity_mammal(self)

class Ape(Primate):
    def info(self):
        return Primate.info(self) + "I am a primate."

    def identity_ape(self):
        return Mammal.identity_mammal(self)

John = Human()
Julius = Ape()

John.info()
John.identity_mammal()
John.identity_primal()
John.identity_human()
# John.identity_ape()       # Kommenterer ut så koden kan kjøre videre

Julius.info()
Julius.identity_mammal()
Julius.identity_primal()
# Julius.identity_human()   # Kommenterer ut så koden kan kjøre videre
Julius.identity_ape()

# Kjøretest terminal a, b, c:
# Kommenenterte ut John.identity_ape for output 2:
"""
Desktop\Python\Oblig uke 44 IN1900> python inheritance.py
Traceback (most recent call last):
  File ".\inheritance.py", line 41, in <module>
    John.identity_ape()
AttributeError: 'Human' object has no attribute 'identity_ape'

': Output2 :'

PS C:\Desktop\Python\Oblig uke 44 IN1900> python inheritance.py
Traceback (most recent call last):
  File ".\inheritance.py", line 46, in <module>
    Julius.identity_human()
AttributeError: 'Ape' object has no attribute 'identity_human'
"""

# d)
d = {1: 'Mammal', 2: 'Primate', 3: 'Human', 4: 'Ape'}
for key in d:
    print(f"John is a {d[key]}: {isinstance(John, eval(d[key]))}")
    print(f"Julius is a {d[key]}: {isinstance(Julius, eval(d[key]))}")
    print("")


# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 44 IN1900> python inheritance.py
John is a Mammal: True
Julius is a Mammal: True

John is a Primate: True
Julius is a Primate: True

John is a Human: True
Julius is a Human: False

John is a Ape: False
Julius is a Ape: True
"""
