person = []
age = []
height = []

def read_file(filename):
    with open(filename) as file:
        for line in file:
            LINE = line.split()
            try:
                age.append(int(LINE[1]))
                height.append(float(LINE[2]))
                person.append(LINE[0])
            except:
                pass
    return person, age, height

person, age, height = read_file("les.txt")
print(person, age, height)


def read_file(filename):
    with open(filename) as file:
        file.readline()
        for line in file:
            LINE = line.split()

            age.append(int(LINE[1]))
            height.append(float(LINE[2]))
            person.append(LINE[0])

    return person, age, height

person, age, height = read_file("les.txt")
print(person, age, height)
