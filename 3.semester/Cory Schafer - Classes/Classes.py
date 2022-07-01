# Python OOP


class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@uio.no'

        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   # Øker med % og runder til heltall

    @classmethod    # Dekorator som gjør at instansen som sendes inn er klassen istedet for self
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod    # Alternativ konstruktør
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Anton', 'Brekke', 50000)
emp_2 = Employee('Johan', 'Carlsen', 50000)

# Disse to er det samme
print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
print()

# print(emp_1.__dict__)
# print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

Employee.raise_amount = 1.04
emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

print(Employee.num_of_employees)
emp_3 = Employee('Mads', 'Balto', 50000)
print(Employee.num_of_employees)
print()

Employee.set_raise_amount(1.06)
print(Employee.raise_amount)
print()

# Her bruker vi klassemetoden som alternativ konstruktør når vi har info i en string
emp_4_str = 'Torstein-Aasheim-50000'
emp_4 = Employee.from_string(emp_4_str)
print(emp_4.email)
print(emp_4.pay)

import datetime
my_date = datetime.date.today()
random_date = datetime.date(2016, 2, 14)
print(Employee.is_workday(my_date))
print(Employee.is_workday(random_date))
print()

dev_1 = Developer('Rebecca', 'Nguyen', 70000, 'Python')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_1.prog_lang)
print()

mgr_1 = Manager('Elias', 'Frimansson', 90000, [emp_3, dev_1])
mgr_1.print_emps()
print()
mgr_1.add_emp(emp_2)
print()
mgr_1.print_emps()
mgr_1.remove_emp(emp_3)
print()
mgr_1.print_emps()
print()

# Alt dette er det samme
print(emp_4)
print(str(emp_4))
print(emp_4.__str__())
print(repr(emp_4))
print(emp_4.__repr__())
print()

# Dette gjelder alle klasser i Python, som heltall, strings etc.
print(1 + 2)
print(int.__add__(1,2))
print('a' + 'b')
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)    # Legger sammen lønnen til begge
print()
print(len('test'))
print('test'.__len__())
print()
print(len(emp_2))   # Printer ut lengden på det fulle navnet
