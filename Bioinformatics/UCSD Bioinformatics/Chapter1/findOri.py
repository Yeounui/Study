from skew import skewMinimum
from frequentWordsWithMismatchesPlusReverse import FrequentWordsWithMismatchesPlusReverse

# Load genome sequence data.
targettxt = './Study/Bioinformatics/UCSD Bioinformatics/Chapter1/Salmonella_enterica.txt'

genomeData = str()
opentxt = open(targettxt, 'r')
readtxt = opentxt.readline()
while readtxt:
    readtxt = opentxt.readline().strip()
    genomeData += readtxt
opentxt.close()

# Set range of seeking frequent k-mer based on skew score.
L = 500

skewMinList = skewMinimum(genomeData)
potentRangeList = list()
for i in skewMinList:
    potentRangeList.append(genomeData[i-L:i+L])
    
# Find frequent k-mer in chosen range.
k = 9 # k is too short to consider insertion and deletion.
d = 1 # or 2
# When L, d is adjusted like this, 9-mers which is similar to E. coli comes out.
for t in potentRangeList:
    FreqWordList = FrequentWordsWithMismatchesPlusReverse(t, k, d)
    print(FreqWordList)
    
"""
If deamination decreases the amount of cytosine on the forward strand, and increases the amount of thymine on the forward strand and adenine
on the reverse strand, why don't we examine the difference between occurrences of T and C or between A and C? What is special about G and C?

Either of these two alternatives is perfectly reasonable. But computing the skew as the difference between G and C performed the best in practice.

In particular, you may have noticed that the frequency of T on the forward half-strand hardly changed.
Although deamination initially creates a surplus of thymine on the forward half-strand, this surplus may be reduced by follow-up mutations of thymine
into other nucleotides. In fact, deamination is just one of many factors that may contribute to skew. See Frank and Lobry, 1999 for a review of various
mechanisms that contribute to the GC-skew. Tillier and Collins, 2000 even argued that deamination is not the major factor contributing to GC-skew.
The question is whether there is some mechanism that makes GC-skew such a useful tool for identifying the location of ori in some species (like E. coli)
but not others.
"""