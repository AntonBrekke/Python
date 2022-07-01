
input_list = input("Skriv en liste:")

# def input_to_list(argument):
#     list = []
#     for a in argument.strip('[]').strip('()').split(','):
#         list.append(float(a))
#     if len(list)==2:
#         return list
#     else:
#         print("list of wrong length")
#
# print(input_to_list(input_list))

# Putter alt det ovenfor inn her:
"""
def input_to_list(argument):
    list_func = list(map(float, argument.strip('[]').strip('()').split(',')))
    if len(list_func)==2:
        return list_func
    else:
        print("Gal lengde på listen")

print(input_to_list(input_list))
"""

import sys

printer = sys.argv[1:]
empty_string = ''
for i in range(len(printer)):
    empty_string += printer[i] + ' '
print(empty_string)
