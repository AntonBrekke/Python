# Exercise 6.11 Langtangen
# p: -3 + 2*x**3 - x**5
p = {0: -3, 3: 2, 5: -1}

def diff(p):
    dp = {}
    for power in p:
        if power != 0:
            dp[power - 1] = p[power]*power
    return dp

print(diff(p))
