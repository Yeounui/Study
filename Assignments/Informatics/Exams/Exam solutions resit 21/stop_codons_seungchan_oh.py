'''
Created on 2017. 8. 18.

@author: Seungchan Oh 01603277
'''
def isStopCodon(triplet):
    
    """
    >>> isStopCodon('TAA')
    True
    >>> isStopCodon('tag')
    True
    >>> isStopCodon('ATC')
    False
    """
    #if the given string is in the list of stop codon, it leads to True.
    if triplet.upper() in ['TAG', 'TGA', 'TAA']:
        return True
    else:
        return False
def reverseComplement(DNAstrand):
    
    """
    >>> reverseComplement('AAGTC')
    'GACTT'
    >>> reverseComplement('agcttcgt')
    'ACGAAGCT'
    >>> reverseComplement('AGTCTTACGCTTA')
    'TAAGCGTAAGACT'
    """
    reversed = ''
    DNAstrand = DNAstrand[::-1].upper() #After changes the given strand reversed,
    for base in DNAstrand: # and then add complement bases to new variant in sequence.
        if base == 'A':
            base = 'T'
        elif base == 'G':
            base = 'C'
        elif base == 'C':
            base = 'G'
        else:
            base = 'A'
        reversed += base
    return reversed

def stopCodons(DNAstrand, frame):
    
    """
    >>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>> stopCodons(seq, +1)
    1
    >>> stopCodons(seq, +2)
    5
    >>> stopCodons(seq, +3)
    2
    >>> stopCodons(seq, -1)
    3
    >>> stopCodons(seq, -2)
    0
    >>> stopCodons(seq, -3)
    1
    """
    count = 0
    if frame < 0: #if the frame is minus, must convert into complement strand.
        DNAstrand = reverseComplement(DNAstrand)
    DNAstrand = DNAstrand[abs(frame)-1:] #if the absolute value of frame is n, skip n bases. 
    while len(DNAstrand) > 2: # read 3 characters together for codon.
        triplet = DNAstrand[:3]
        DNAstrand = DNAstrand[3:] # cut codon out from DNAstrand
        if isStopCodon(triplet): # if the cut codon is stop codon, count it.
            count += 1
    return count

def codons(DNAstrand, frame):
    
    """
    >>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
    >>> codons(seq, +1)
    'TTT-ACT-ATA-GTG-ATA-GCC-GGT-AAC-ATA-GCT-CCT-AGA-ATA-AAG-GCA-ACG-CAA-TAC-CCC-TAG-G'
    >>> codons(seq, +2)
    'T-TTA-CTA-TAG-TGA-TAG-CCG-GTA-ACA-TAG-CTC-CTA-GAA-TAA-AGG-CAA-CGC-AAT-ACC-CCT-AGG'
    >>> codons(seq, +3)
    'TT-TAC-TAT-AGT-GAT-AGC-CGG-TAA-CAT-AGC-TCC-TAG-AAT-AAA-GGC-AAC-GCA-ATA-CCC-CTA-GG'
    >>> codons(seq, -1)
    'CCT-AGG-GGT-ATT-GCG-TTG-CCT-TTA-TTC-TAG-GAG-CTA-TGT-TAC-CGG-CTA-TCA-CTA-TAG-TAA-A'
    >>> codons(seq, -2)
    'C-CTA-GGG-GTA-TTG-CGT-TGC-CTT-TAT-TCT-AGG-AGC-TAT-GTT-ACC-GGC-TAT-CAC-TAT-AGT-AAA'
    >>> codons(seq, -3)
    'CC-TAG-GGG-TAT-TGC-GTT-GCC-TTT-ATT-CTA-GGA-GCT-ATG-TTA-CCG-GCT-ATC-ACT-ATA-GTA-AA'
    """
    order = abs(frame) # starting point
    if frame < 0: # minus value means the complement strand
        DNAstrand = reverseComplement(DNAstrand)
    while len(DNAstrand) >= order: #Until the order value overcomes length of DNA strand,
        DNAstrand = DNAstrand[:order-1] + '-' + DNAstrand[order-1:] # add a '-' tag between each codon
        order += 4 # order should be increased 4(a codon(3) and a tag(1))
    return DNAstrand.strip('-') #erase unneeded tags

if __name__ == '__main__':
    import doctest
    doctest.testmod()