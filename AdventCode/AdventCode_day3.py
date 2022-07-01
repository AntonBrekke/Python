

with open('Tree_slope.txt','r') as infile:
    # 3 Right 1 Down
    i = 0
    count1 = 0
    for line in infile:
        if line[i] == '#':
            count1 += 1

        if i == 30:
            i = -1
        elif i == 29:
            i = -2
        elif i == 28:
            i = -3
        i += 3
    print(count1)

    # 1 Right 1 Down
    infile.seek(0,0)
    i = 0
    count2 = 0
    for line in infile:
        if line[i] == '#':
            count2 += 1

        if i == 30:
            i = -1
        i += 1
    print(count2)

    # 5 Right 1 Down
    infile.seek(0,0)
    i = 0
    count3 = 0
    for line in infile:
        if line[i] == '#':
            count3 += 1

        if i == 30:
            i = -1
        elif i == 29:
            i = -2
        elif i == 28:
            i = -3
        elif i == 27:
            i = -4
        elif i == 26:
            i = -5
        i += 5
    print(count3)

    # 7 Right 1 Down
    infile.seek(0,0)
    i = 0
    count4 = 0
    for line in infile:
        if line[i] == '#':
            count4 += 1

        if i == 30:
            i = -1
        elif i == 29:
            i = -2
        elif i == 28:
            i = -3
        elif i == 27:
            i = -4
        elif i == 26:
            i = -5
        elif i == 25:
            i = -6
        elif i == 24:
            i = -7
        i += 7
    print(count4)

    # Right 1 Down 2
    infile.seek(0,0)
    i = 0
    count5 = 0
    for line in infile:
        if line[i] == '#':
            count5 += 1

        if i == 30:
            i = -1

        i += 1
        infile.readline()
    print(count5)
print(count1*count2*count3*count4*count5)

# Prøve å generalisere:
infile = open('Tree_slope.txt','r')
# 3 Right 1 Down
R = 1
D = 2
i = 0
count1 = 0
for line in infile:
    if line[i] == '#':
        count1 += 1

    for m in range(R):
        if i == 30-m:
            i = -(m+1)
    i += R
    for a in range(D-1):
        infile.readline()
print(count1)

# Funksjon:
def tree_slope(R, D):
    infile = open('Tree_slope.txt','r')

    R = R
    D = D
    i = 0
    count1 = 0
    for line in infile:
        if line[i] == '#':
            count1 += 1

        for m in range(R):
            if i == 30-m:
                i = -(m+1)
        i += R
        for a in range(D-1):
            infile.readline()
    return count1

print(tree_slope(3,1))
