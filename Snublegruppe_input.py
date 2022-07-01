import sys
try:
    a = eval(sys.argv[1])
    b = eval(sys.argv[2])

except IndexError:
    print("Not enough values in Index")
    exit()

except:
    print("Arguments have to be numbers")
    exit()
print(a + b)
