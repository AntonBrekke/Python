"""
Oppgave 3.11, oppgavehefte
"""
M_C = 12.011     # g/mol Carbon
M_H = 1.0079     # g/mol Hydrogen

# Masse i g/mol pr. stoff:
for n in range(2,10):   # Fra 2 til 10 Carbon
    m = 2*n + 2         #
    M = n*M_C + m*M_H
    print(f"M(C{n}H{m}) = {M:.2f}g/mol")

# Kjøretest i terminal:
"""
PS C:\Desktop\Python> python alkane.py
M(C2H6) = 30.07g/mol
M(C3H8) = 44.10g/mol
M(C4H10) = 58.12g/mol
M(C5H12) = 72.15g/mol
M(C6H14) = 86.18g/mol
M(C7H16) = 100.20g/mol
M(C8H18) = 114.23g/mol
M(C9H20) = 128.26g/mol
"""
