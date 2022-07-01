import sys

ans = True

while ans:
    command = input("Run code or press enter to quit:")

    if command == "":
        sys.exit()

    if command == "Run 1":
        print(1)

    if command == "Run 2":
        print(2)

    if command == "c":
        ans = False

print('Du gikk videre')
