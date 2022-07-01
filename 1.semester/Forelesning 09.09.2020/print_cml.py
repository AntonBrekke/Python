import sys

print(sys.argv)

# Kommando eksempel:
"""
python .\print_cml.py [1,2,3]
"""

arg1 = list(sys.argv[1])
print(arg1, type(arg1))
