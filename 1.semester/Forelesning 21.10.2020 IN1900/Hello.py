# Exercise 7.10 Langtangen

class Hello:
    def __init__(self):
        self.greeting = "Hello, "

    def __call__(self, who):
        return self.greeting + who + "!"

    def __str__(self):
        return self.greeting + "World!"

a = Hello()
print(a('students'))
print(a)
