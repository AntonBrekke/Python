import numpy as np

# Genererer random tall mellom 0 - 9
def random(seed, N):
    rand = np.zeros(N)
    rand[0] = seed
    for i in range(N-1):
        rand[i+1] = (rand[i]*1243 + 432) % 732
    str = [f'{u}'.replace('.', '') for u in rand]
    str = ''.join(str)
    rand2 = np.zeros(N)
    for i in range(N):
        rand2[i] = str[-i]
    return rand2


x = random(101, 100)
print(x)
