# Exercise A.2
N = 14              # Bestemmer en N
x = [0]*(N+1)       # Liste med lengde N+1 og sluttindex N
x[0] = 1; x[1] = 1      # Initialbetingelser

# Løser differenslikning gitt i oppgave
for n in range(2,N+1):
    x[n] = x[n-1] + x[n-2]

# Printer ut verdier
index = [0]*len(x)
for i in range(len(index)):
    index[i] = i
    print(f"{index[i]}\t|\t{x[i]}")

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 40 IN2900> python fibonacci.py
0       |       1
1       |       1
2       |       2
3       |       3
4       |       5
5       |       8
6       |       13
7       |       21
8       |       34
9       |       55
10      |       89
11      |       144
12      |       233
13      |       377
14      |       610
"""
