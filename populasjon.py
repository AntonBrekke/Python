import sys
import matplotlib.pyplot as plt

# Les parametere fra kommandolinjen
x0 = int(sys.argv[1])   # Startpopulajson
M = int(sys.argv[2])    # Bærekapasitet
a = float(sys.argv[3])  # Vekstfaktor (0 = konstant populasjon)
N = 200 # Tidssteg

# Initier x
x = [0]*(N + 1)
x[0] = x0

# Beregn x[n] for n=1,2,...,N
for n in range(1, N + 1):
    x[n] = x[n-1] + a*x[n-1]*(1-x[n-1]/M)

# Plott x[n] vs N

plt.plot(range(N+1),x,"r:", label = "Populasjonsvekst")
plt.xlabel("År")
plt.ylabel("Populasjon")
plt.legend()
plt.show()

# Eksempel på kjøring:
# python populasjon.py 50 200 0.3
