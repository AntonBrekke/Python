dic1 = {'A': 'eple', 'B': 'sitron'}
dic2 = {'C': 'appelsin', 'D': 'ananas'}

def merge(a, b):
    return {**a, **b}
dic3 = merge(dic1, dic2)
# print(dic3)
for n, key in enumerate(dic3, start=1):
    print(n, key, dic3[key])
