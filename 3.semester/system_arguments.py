import sys
a = sys.argv[1:]
try: b = map(float, a); print(*b)
except: print(a)
