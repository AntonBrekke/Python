for i in range(2,5):
    print(i, end=' ')
    for j in range(i-1,i+1):
        if i != j:
            print(j, end=' ')

# Output: 2 1 3 2 4 3
