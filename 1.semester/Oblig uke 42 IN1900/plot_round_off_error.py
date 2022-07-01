# Exercise 7.5 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt

def return_array(filename):
    with open(filename, 'r') as infile:
        N = 0
        for line in infile: # Leser av antall linjer i filen for å bestemme en n-verdi (generalisering)
            N += 1
        delta_x = np.zeros(N)   # Lager null-arrays med størrelse N = n fra approx_derivate_sine.txt
        abs_error = np.zeros(N)
        n = np.zeros(N)

        infile.seek(0)  # Setter posisjonen i filen tilbake til start
        i = 0   # Indekstall
        for line in infile: # Går igjennom linjer i infile på nytt og legger verdir i tilsvarende arrays:
            words = line.split(',')
            delta_x[i] = float(words[0].split(':')[-1])
            abs_error[i] = float(words[3].split(':')[-1])
            n[i] = float(words[5].split('=')[-1])
            i += 1
        plt.semilogy(n, delta_x, 'r.', label = 'delta_x')   # Plotter verdiene i et logaritmisk plan
        plt.semilogy(n, abs_error, 'b.', label = 'abs_error')
        plt.legend()
        plt.xlabel('n')
        plt.axis([n[0]-1, n[-1]+1, delta_x[-1], delta_x[0]*10]) # Tilpasser akse
    return plt.show()

return_array('approx_derivative_sine.txt')

# Hvorfor blir den absolutte feilen større etter n = 8?
"""
Om vi ser på leddet der vi definerer den deriverte funksjonen og delta_x i
approx_derivate_sine.py:

delta_x = 10**(-n)
...
def df_approx(f, x, delta_x):
	return (f(x+delta_x)-f(x))/delta_x

ser vi at når n blir større blir delta_x mindre. Da blir f(x + delta_x) mer lik f(x),
og vi får etterhvert tilfeller der f(x + delta_x) - f(x) fører til kansellering,
som gir store avrundingsfeil, spesielt når vi deler dette på delta_x, som er et lite tall.
df_approx blir større, og når vi trekker fra den eksakte løsningen får vi en større absolutt feil.
"""

# Kjøretest fra terminal:
"""
PS C:\Desktop\Python\Oblig uke 42 IN1900> python plot_round_off_error.py
PS C:\Desktop\Python\Oblig uke 42 IN1900>
"""
