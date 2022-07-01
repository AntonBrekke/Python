

a = ['Hei', 'jeg', 'tester', 'skrivefunksjon', 'i', 'Python']


with open('write_test', 'r+') as f_object:
    for i in range(10):
        f_object.write(f'{i} ')
    x = f_object.readlines()
    print(x)
