# Med for løkke
for F in range(0, 101, 10):
    C = (9/5)*(F - 32)
    print(f"{F:10.0f}\t|\t{C:10.2f}")

# Med while løkke
print("")
F = 0
while F <= 100:
    C = (9/5)*(F - 32)
    print(f"{F:10.0f}\t|\t{C:10.2f}")
    F += 10     # F = F + 10
    
