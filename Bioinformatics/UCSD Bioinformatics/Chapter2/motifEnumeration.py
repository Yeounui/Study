# importing sys
import sys

# adding Chapter1 to the system path
sys.path.insert(0, './Study/Bioinformatics/UCSD Bioinformatics/Chapter1')
from frequentWordsWithMismatches import generateVarSet
from hammingDistance import countApproxPattern

def motifEnumeration(dna, k, d):
    dnaList = dna.split(' ')
    patterns = set()
    for i in range(len(dnaList[0]) -k +1):
        varSet = generateVarSet(set([dnaList[0][i:i+k],]), d)
        for varPattern in list(varSet):
            allincluded = True
            for j in dnaList[1:]:
                if countApproxPattern(j, varPattern, d) == 0:
                    allincluded = False
            if allincluded:
                patterns.add(varPattern)
                    
    return patterns

dna = "CCCTCACAATTCCGATCTCTGGCGG CCCTATAAGCTGTAGCTTTCCATAT GCTTGCCCTTCATGCCACAACTATC AAACGCTCGCTTGTTTGCTCCCCTA CCCTTGACAACTCCTCGTGCTCGGA TAAAGGCTAAGGAGCCCATTCCCTT"
k = 5
d = 1
print(motifEnumeration(dna, k, d))