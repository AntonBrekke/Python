import sys
from math import exp

h = float(sys.argv[1])  # Første argument i terminal gjelder

p0 = 100
h0 = 8400

p = p0*exp(-h/h0)
print(p)

# Gjør at man kan skrive python "filnavn" "verdi for h" i terminalen
