
# Eksempelverdier for a, b, n:
a = 0.0
b = 5.0
n = 10

# a) bruke en for løkke:
x = []
h = (b - a)/n
for i in range(n + 1):
    x.append(a + i*h)
print(x)

# b) Bruke implisitt løkke:
x = [a + i*h for i in range(n + 1)]
