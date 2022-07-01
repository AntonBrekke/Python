# Exercise 8.4 oppgaveheftet

class AccountP:
    # Konstruktør som tar argument fra objekt og lagrer i attributer
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance
        self._transfer = 0
        self._transfer_balance = 0

    # Metoder fra oppgave:
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance, self._transfer_balance

    # Metode oppgave ber meg sette opp:
    def transfer(self, amount, transfer_account):
        self._balance -= amount
        self._transfer = transfer_account
        self._transfer_balance += amount    # Lager en ny attribut for denne i konstruktøren da jeg kan få bruk for å regne med den senere

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; balance = self._balance
        s = f'{first} {last}, {number}, balance: {balance}'
        print(s)

a = AccountP('Anton', 'Brekke', 1234, 1000) # Objekt med argumenter

# Testfunksjon for å sjekke om tranksaksjonen stemmer:
def test_AccountP():
    amount = 100
    a.deposit(amount)
    a.withdraw(amount)
    a.transfer(amount, 100)
    computed = a.get_balance()
    expected = 900, amount         # Tester for både self._balance og self._transfer_balance
    success = computed == expected
    msg = 'Some fuzzy business in transactions!'
    assert success, msg
    # a.print_info()

test_AccountP()

# Kjøreekesempel fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 43 IN1900> python AccountP.py
PS C:\Desktop\Python\Oblig uke 43 IN1900>
"""
