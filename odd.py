"""
Write a program that generates all odd numbers from 1 to n. Set n in the beginning
of the program and use a while loop to compute the numbers. (Make sure that if n
is an even number, the largest generated odd number is n-1.)
"""
a = []
b = []
n = 1
while n <= 20:
    s = 2*n - 1
    a.append(s)
    b.append(n)
    n += 1

for i in range(len(b)):
    print(f"{b[i]}  -->   {a[i]}")

    # Mer effektiv metode:

k = 20
e = 1
while e <= k:
    print(e)
    e += 2
