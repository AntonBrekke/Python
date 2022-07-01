# Exercise 7.2 Primer
class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 1

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1

    def dump(self):
        s = f'{self.name}, {self.no}, transactions: {self.transactions}, balance: {self.balance}'
        print(s)

def test_Account():
    a1 = Account('AB', 12345, 1000)
    a1.deposit(100)
    a1.withdraw(50)
    expected = (1050,3)
    assert (a1.balance, a1.transactions) == expected

test_Account()

a1 = Account('AB', 12345, 1000)
a1.deposit(100)
a1.dump()
