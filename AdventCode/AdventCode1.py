


with open('expense.txt', 'r') as infile:
    numberlist =  []
    for line in infile:
        numberlist.append(int(line.replace('\n','')))
    for i in range(len(numberlist)):
        for k in range(len(numberlist)):
            for j in range(len(numberlist)):
                if numberlist[i] + numberlist[j] + numberlist [k] == 2020:
                    print(numberlist[i], numberlist[j], numberlist[k])
                    print(numberlist[i]*numberlist[j]*numberlist[k])
