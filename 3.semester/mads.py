import random
alphabet = "abcdefghijklmnopqrstuvwxyz.,:;!?"
k = str()
for i in range(10000):
    j =random.randint(0,len(alphabet)-1)
    k += alphabet[j]
print(k)
