
with open('passport_security.txt','r') as infile:
    passport = []
    valid = 0
    for line in infile:
        words = line.split(' ')

        if words != ['\n']:
            passport += words

        elif words == ['\n']:
            if len(passport) == 8:
                valid += 1
            if len(passport) == 7:
                count = 0
                for line in passport:
                    field = line.split(':')[0]
                    if field != 'cid':
                        count += 1
                        if count == 7:
                            valid += 1
            passport = []

    print(valid)
