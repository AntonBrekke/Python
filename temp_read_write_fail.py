#Exercise 5.10
import numpy as np

def extract(filename):
    infile = open('temp_oct_1945.txt', 'r')
    infile1 = open('temp_oct_2014.txt', 'r')
    infile.readline()
    infile1.readline()
    oct_1945_e = []
    oct_2014_e = []
    for line in infile:
        words = line.split()
        oct_1945_e.append(words[0:]) # Lager nested list
    oct_1945 = []
    def reemovNestings(oct_1945_e):
        for i in oct_1945_e:
            if type(i) == list:
                reemovNestings(i)
            else:
                oct_1945.append(i)
        for i in range(len(oct_1945)):
            oct_1945[i] = float(oct_1945[i])
    reemovNestings(oct_1945_e)
    print(oct_1945)


    for line in infile1:
        words = line.split()
        oct_2014_e.append(words[0:]) # Lager nested list
    oct_2014 = []
    def reemovNestings(oct_2014_e):
        for i in oct_2014_e:
            if type(i) == list:
                reemovNestings(i)
            else:
                oct_2014.append(i)
        for i in range(len(oct_2014)):
            oct_2014[i] = float(oct_2014[i])
    reemovNestings(oct_2014_e)
    print(oct_2014)
extract(1)
