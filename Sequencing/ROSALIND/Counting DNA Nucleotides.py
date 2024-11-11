strand = input()

countBase = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for base in strand:
    countBase[base] += 1
    
print("{}, {}, {}, {}".format(countBase['A'], countBase['C'],
                            countBase['G'], countBase['T']))