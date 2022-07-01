# Exercise 6.7 Primer

humans = {}

with open('human_evolution.txt','r') as infile:
    for line in infile:
        if line[0] == 'H':
            name = line[:20].strip()
            when = line[21:35].strip()
            height = line[37:47].strip()
            mass = line[50:59].strip()
            brain = line[61:].strip()
            humans[name] = {'when':when, 'height':height, 'mass':mass, 'brain':brain}

for name in humans:     # Går gjennom keys i humans
    h = humans[name]
    print(f"{name:20}{h['when']:15}{h['height']:10}{h['mass']:10}{h['brain']:10}")
