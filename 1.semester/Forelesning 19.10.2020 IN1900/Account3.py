# Exercise 7.3 Langtangen
from datetime import datetime

class AccountP:
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        t = {'amount':initial_amount, 'time': datetime.now()}
        self._transactions = [t]

    def deposit(self, amount):
        t = {'amount':amount, 'time': datetime.now()}
        self._transactions.append(t)

    def withdraw(self, amount):
        self.deposit(-amount)

    def get_balance(self):
        balance = 0
        for t in self._transactions:
            balance += t['amount']
        return balance

    def print_transactions(self):
        for t in self._transactions:
            print(f"{t['time']}      {t['amount']}")

    def dump(self):
        s = f'{self._name}, {self._no}, transactions: {self._transactions}, balance: {self.get_balance}'
        print(s)

a1 = AccountP('AB', 12345, 100)
a1.deposit(1000)
a1.withdraw(50)
a1.deposit(950)
a1.print_transactions()

# a1.dump()
