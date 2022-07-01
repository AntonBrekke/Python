# Definisjon
class MyClass:
    def __init__(self, p1, p2):
        self.attr1 = p1
        self.attr2 = p2

    def method1(self, arg):
        return self.attr1 + self.attr2 + arg

    def method2(self):
        print('Hello!')

m = MyClass(4, 10)
print(m.method1(-2))
m.method2()

# What is this self variable?
"""
For kode, se Klasser.py fra forelesning 12.10.2020
Flere detaljer finnes i seksjon 8.1 s.119 i boka.
Syntax: y = Y(3)
kan tenkes på som:
Y.__init__(y,3) , der klasse-prefiksen er Y.
Da skal argumentet y være seg selv i funksjonskallet.

v = y.value(2)
kan alternativt skrives som
v = Y.value(y, 2)
"""
# Et annet klasse-eksempel:

# A bank account
class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        s = f'{self.name}, {self.no}, balance: {self.balance}'
        print(s)
# Eksempel på bruk:
a1 = Account('Anton Brekke', '1937154951', 20000)
a2 = Account('Anton Brekke', '1927184961', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print("a1's balance:", a1.balance)
a1.dump()
a2.dump()

# Improved Class with attribute protection:
class AccountP:
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self. amount):
        self._balance -= amount

    def dump(self):
        s = f'{self.name}, {self.no}, balance: {self.balance}'
        print(s)
# Usage:
a1 = AccountP('Anton Brekke', '1937154951', 20000)
a1.withdraw(4000)

print(a1._balance)  # Works but a convention is broken
print(a1.get_balance()) # Correct way of viewing the _balance

a1._no = '19371554955' # Works but is a serious "crime"!
