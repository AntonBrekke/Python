

with open('passwords.txt','r') as infile:
    count = 0
    for line in infile:
        words = line.split(' ')
        numblist = words[0].split('-')
        number = [int(numblist[0]), int(numblist[1])]
        letter = words[1].replace(':','')
        password = words[2].replace('\n','')
        a = 0
        for i in password:
            if letter == i:
                a += 1
        if a <= number[1] and a >= number[0]:
            count += 1
    print(count)


with open('passwords.txt','r') as infile:
    count = 0
    for line in infile:
        words = line.split(' ')
        numblist = words[0].split('-')
        number = [int(numblist[0]), int(numblist[1])]
        letter = words[1].replace(':','')
        password = words[2].replace('\n','')


        if password[number[0]-1] != letter and password[number[1]-1] == letter:
                    count += 1

        if password[number[0]-1] == letter and password[number[1]-1] != letter:
                    count += 1

    print(count)
