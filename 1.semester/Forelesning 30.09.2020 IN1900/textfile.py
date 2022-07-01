infile = open("text.txt",'r')
pairs = []      # Lagrer data fra fil i pairs
for line in infile:
    words = line.split()    # Splitter ord i line ved " "
    for w in words:         # Går gjennom alle ord i words i line
        w = w[1:-1] # Fjerner element 0 og -1 fra listen
        numbers = w.split(",")  # Splitter ved , siden vi kun vil ha tallet
        pair = (float(numbers[0]), float(numbers[1])) # Henter ut tall i par
        pairs.append(pair)
print(pairs)
