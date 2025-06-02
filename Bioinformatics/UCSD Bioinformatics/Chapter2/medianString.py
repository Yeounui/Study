# importing sys
import sys

# adding Chapter1 to the system path
sys.path.insert(0, './Study/Bioinformatics/UCSD Bioinformatics/Chapter1')
from frequentWordsWithMismatches import generateVarSet
from hammingDistance import hammingDistance

def distanceBetweenPatternAndStrings(pattern, dnaList):
    k = len(pattern)
    dist = 0
    for txt in dnaList:
        hammingDist = k + 1
        for i in range(len(txt)-k+1):
            candidDist = hammingDistance(pattern, txt[i:i+k])
            if hammingDist > candidDist:
                hammingDist = candidDist
        dist += hammingDist
    return dist

def medianString(k, dna):
    dnaList = dna.split(' ')
    distance = k * len(dnaList)
    median = str()
    kmerList = list(generateVarSet({'A'*k,}, k))
    for p in kmerList:
        distPS = distanceBetweenPatternAndStrings(p, dnaList)
        if distance > distPS:
            distance = distPS
            median = p
    return median
        

k = 6
dna = "CCCAGCTCGGAATGTGCTAAGTCGGGCCCCACCGATGCTAAT TGTGCTTGAGGACTGGATAGTGGCGGAGGTGATAACTAGATC GGATACAAATCGAGGGTGTAATATTGTACTATAACGAGTCTC AGACACCTATAATGTGCTACTGCAAAAAGTGTCGGTTCGCCT GCTGGTCTCGTTGCTTGGTGAGCGTGTGCTGGCAAAGTGACC TCTCGCTGTCCTGGCCGATTGACACTACTTAGAATTGATAAC TAGCGAGTTACGAGCAGGAGTACTCCTTCATGTTCTTCTCGG CAGGCGTACAACTGTTCTGCACTAGGTCTCCAAATCACGACC GTATCTGCGACCTGCCAAGTGCTATGGCGGTGCAATTGTGCT GATATTACATAATGTTCTTCCCCTATCTATGACAGTTTTAGG"
print(medianString(k, dna))