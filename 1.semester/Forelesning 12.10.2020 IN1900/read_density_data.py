# Excercise 5.16 Langtangen
import matplotlib.pyplot as plt
import sys

def read_data(filename):
    temp = []
    density = []
    with open(filename,'r') as infile:
        for line in infile:
            if line[0] == '#' or line.isspace():
                continue
            words = line.split()
            temp.append(float(words[0]))
            density.append(float(words[-1]))
    return temp, density

if __name__ == '__main__':
    temp, dens = read_data(sys.argv[1])
    plt.plot(temp, dens, 'ro')
    plt.show()
