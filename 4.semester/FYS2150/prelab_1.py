import numpy as np
import matplotlib.pyplot as plt

data_array = np.loadtxt('data1.csv')

n = np.size(data_array)

mean_value = np.sum(data_array) / (n-1)
print(mean_value)

std_dev = np.sqrt(1/(n)*np.sum((data_array - mean_value)**2))
print(std_dev)
std_dev_mean = std_dev / np.sqrt(n)
print(std_dev_mean)

count = 0
N = 1
for i in data_array:
    if i < mean_value + N*std_dev and i > mean_value - N*std_dev:
        count += 1

data_inside_std = count / np.size(data_array) * 100
print(f'{data_inside_std}%')
