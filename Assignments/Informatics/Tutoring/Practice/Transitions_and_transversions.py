'''
Created on 2017. 8. 11.

@author: korea
'''
def transition(base1, base2):
    switch = 0
    if base1.upper() == 'A':
        if base2.upper() == 'G':
            switch = 1
    elif base1.upper() == 'G':
        if base2.upper() == 'A':
            switch = 1
    elif base1.upper() == 'C':
        if base2.upper() == 'T':
            switch = 1
    elif base1.upper() == 'T':
        if base2.upper() == 'C':
            switch = 1
    
    if switch == 1:
        return True
    else:
        return False

def transversion(base1, base2):
    if transition(base1, base2) or base1.upper() == base2.upper():
        return False
    else:
        return True
    
def ratio(strand1, strand2):
    transitioncount = 0
    transversioncount = 0
    strand1 = list(strand1)
    strand2 = list(strand2)
    strandlist= list(zip(strand1, strand2))
    
    for order in strandlist:
        base1, base2 = order
        if transition(base1, base2):
            transitioncount += 1
        elif transversion(base1, base2):
            transversioncount += 1
    
    if transversioncount == 0:
        return float(0)
    else:
        return float(transitioncount/transversioncount)

print(transition('G', 'A'))
print(transition('t', 'g'))
print(transition('C', 'c'))
print(transversion('G', 'A'))
print(transversion('t', 'g'))
print(transversion('C', 'c'))
print(ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG'))
seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
seq2 = 'ttatctgacaaagaaagccgtcaacggctggataatttcgcgatcgtgctggttactggcggtacgagtgttcctttgggt'
print(ratio(seq1, seq2))