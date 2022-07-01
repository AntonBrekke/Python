# Exercise 7.2 oppgaveheftet
# a)
elements_10 = {1: '-', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon',
7: 'Nitrogen', 8: '-', 9: 'Fluorine', 10: 'Neon'}

elements_10[1] = 'Hydrogen'
elements_10[8] = 'Oxygen'

# b)
elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Sodium'})
print(elements_10)
print('\n')
elements_11 = elements_10
elements_11.update({11: 'Sodium'})
print(elements_10)

"""
Elements_10_copy er en direkte kopi av elements_10.
Vi kopierer dictionaryen, og lager en helt ny, selvstendig dictionary.
Derfor vil ikke elements_10 ha forandret seg når vi oppdaterer elements_10_copy.

elements_11 derimot sier vi er lik elements_10. Vi sier at det er samme dictionary, og når
den ene da oppdateres, oppdateres den andre også, som om de er linka opp mot hverandre.
Da ser vi at elements_10 har endret seg i print når vi oppdaterer elements_11.
"""

# Kjøretest fra terminal (a og b):
"""
PS C: \Python\Oblig uke 42 IN1900> python chemical_elements_dict.py
{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}


{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon', 11: 'Sodium'}
"""
