import sys

a = True

while a:
    text = input("Commands:\n\nmomentum table\npopulation table\nalkane\nrandom fac (from 1-10)\n\n")
    if text == (""):
        sys.exit()

    elif text == ("momentum table"):
        print("")
        from math import sqrt
        a = []              # Liste for bevegelsesmengde
        b = []              # Liste for prosent lyshastighet
        r = []              # Liste for relativistisk bevegelsesmengde
        c = 3.0*10.0**8     #Lyshastigheten
        v = 0.1*c
        m = 1200.0
        l = 1/sqrt(1 - (v/c)**2)    #Lorentzfaktoren

        print("__________________________________________")
        print("|Speed  |   Momentum    |   Relativistic |\n|       |\t\t|   momentum\t |")
        print("|_______|_______________|________________|")

        for i in range(1, 10):
            p = m*v           # Momentum
            p_r = m*v*l     # Relativistic momentum
            b.append(0.1*i)
            a.append(p)
            r.append(p_r)
            #input()
            print(f"| {b[i-1]:.1f}c  |   {a[i-1]:.4e}  |   {r[i-1]:.4e}   |") # Bare pynting for å få fin print
            v = (i + 1)*v
        print("------------------------------------------")

    elif text == ("population table"):
        from math import exp
        t_list = []     #list for time
        n_list = []     # List for amount N

        B = 50000
        k = 0.2
        C = 9.0
        t = 0

        for t in range(0, 49, 12):
            N = B/(1 + C*exp(-k*t))
            n_list.append(N)
            t_list.append(t)

        tN2 = [[], []]      # Lager nested list
        for t, N in zip(t_list, n_list): # Zip t løper gjennom t_list, N løper gjennom n_list
            tN2[0].append(t)
            tN2[1].append(N)

        for a in range(len(t_list)):
            print(f"{tN2[0][a]}\t| {tN2[1][a]:.2f}")

    elif text == ("alkane"):
        M_C = 12.011     # g/mol
        M_H = 1.0079     # g/mol

        for n in range(2,10):
            m = 2*n + 2
            M = n*M_C + m*M_H
            print(f"M(C{n}H{m}) = {M}")

    elif text == ("random fac"):
        from math import factorial
        import random

        def myfactorial(n):
            return factorial(n)

        k = random.randint(1, 10)
        print(myfactorial(k))
