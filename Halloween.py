Halloween = {'Anton': [0,1,1,0], 'Mads': [1,0,0,1], 'Magnus': [1,0,1,0], 'Maria': [1,1,0,0]}

print('\tV1\tV2\tV3\tV4')
for key in Halloween:
    numbers = Halloween[key]
    print('-------------------------------------')
    print(key)
    for i in numbers:
        if i == 1:
            print(f'\t{True}', end = '')
        else:
            print(f'\t{False}', end = '')
    print('\n')
