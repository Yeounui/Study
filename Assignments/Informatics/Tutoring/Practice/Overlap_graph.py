'''
Created on 2017. 6. 22.

@author: korea
'''
def overlap(strand1, strand2, length):
    part1 = strand1[-length:]
    part2 = strand2[:length]
    #print(part1, part2)
    if part1 == part2:
        return True
    else:
        return False
    
def maximalOverlap(strand1, strand2):
    if len(strand1) >= len(strand2):
        prelength = len(strand2)
    else:
        prelength = len(strand1)
    length = prelength
    for order in range(prelength):
        if length != 1:
            if not overlap(strand1, strand2, prelength-order):
                length -= 1
            else:
                return length
        else:
            if strand1[-1] == strand2[0]:
                return length
            else:
                return 0
        
        
def overlapGraph(reads, length):
    box = list()
    resultdict = dict()
    for strand1 in reads:
        for strand2 in reads:
            if maximalOverlap(strand1, strand2) >= length and strand1 != strand2:
                box.append(strand2)
        if box != list():
            resultdict[strand1] = set(box)
            box = list()
    return resultdict
                
print(overlap('AAATTTT', 'TTTTCCC', 3))
print(overlap('AAATTTT', 'TTTTCCC', 5))
print(overlap('ATATATATAT', 'TATATATATA', 4))
print(overlap('ATATATATAT', 'TATATATATA', 5))

print(maximalOverlap('AAATTTT', 'TTTTCCC'))
print(maximalOverlap('ATATATATAT', 'TATATATATA'))
print(maximalOverlap('TAAGAC', 'CAGTAGC'))

reads = ['AAATAAA', 'AAATTTT', 'TTTTCCC', 'AAATCCC', 'GGGTGGG']
print(overlapGraph(reads, 3))
print(overlapGraph(reads, 4))

reads = ['GACCTACA', 'ACCTACAA', 'CCTACAAG', 'CTACAAGT', 'TACAAGTT', 'ACAAGTTA', 'CAAGTTAG', 'TACAAGTC', 'ACAAGTCC', 'CAAGTCCG']
print(overlapGraph(reads, 6))