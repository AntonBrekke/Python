# Exercise 4.13
import sys
v0 = float(sys.argv[1])
t = float(sys.argv[2])
g = 9.81

t_stop = 2*v0/g

if t < 0 or t > t_stop:
    raise ValueError(f't must be between 0 and {t_stop}')

y = v0*t - 0.5*g*t**2
print(y)
