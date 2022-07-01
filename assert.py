"""
Use of assert to check argumennts
"""

def some(numbers):

    assert len(numbers) > 0, 'Length of list must be > 0'

    s = 0
    for n in numbers:
        s = s + n
    return s/len(numbers)

    mylist = 3
    print(mean(mylist))
