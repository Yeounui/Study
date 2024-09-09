'''
Created on 2018. 1. 18.

@author: korea
'''
def isStopCodon(codon):
    return bool(codon.upper() in {'TAA', 'TAG', 'TGA'})

def reverseComplement(aStrand):
    complementStrand = str()
    for base in aStrand[::-1].upper():
        if base == 'A':
            complementStrand += 'T'
        elif base == 'G':
            complementStrand += 'C'
        elif base == 'C':
            complementStrand += 'G'
        else:
            complementStrand += 'A'
    return complementStrand

def stopCodons(seq, frame):
    Codon = str()
    count = 0
    if int(frame) < 0:
        seq = reverseComplement(seq)
    for base in seq[abs(int(frame))-1:]:
        Codon += base
        if len(Codon) == 3:
            if isStopCodon(Codon):
                count += 1
            Codon = str()
    return count

def codons(seq, frame):
    count = 0
    if int(frame) < 0:
        seq = reverseComplement(seq)
    while count < len(seq):
        if count % 4 == 0:
            seq = seq[:count+abs(int(frame))-1] + '-' + seq[count+abs(int(frame))-1:]
            count += 1
        count += 1
    return seq.strip('-')

print(isStopCodon("GAA"))
print(reverseComplement('AGTCTTACGCTTA'))    
seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
print(stopCodons(seq, +2))
print(codons(seq, -1))