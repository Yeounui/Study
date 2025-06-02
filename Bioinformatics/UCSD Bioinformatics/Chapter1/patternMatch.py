def transformToScore(digit):
    if (digit == "A"):
        return 1
    elif (digit == "C"):
        return 2
    elif (digit == "G"):
        return 3
    else:
        return 4
            
def strandHash(strand):
    hash = 0
    for i in strand:
        hash += transformToScore(i)
    hash %= 5
    return hash

def patternMatch(pattern, genome):
    matchPosList = list()
    patternhash = strandHash(pattern)
    patternlen = len(pattern)
    candidatehash = strandHash(genome[:patternlen-1])
    for i in range(len(genome)-patternlen+1):
        candidatehash += transformToScore(genome[i+patternlen-1])
        candidatehash %= 5
        if ((candidatehash == patternhash) and 
            (pattern == genome[i:i+patternlen])):
            matchPosList.append(str(i))
        candidatehash -= transformToScore(genome[i])
    return ' '.join(matchPosList)

targettxt = './Study/Bioinformatics/UCSD Bioinformatics/Chapter1/Vibrio_cholerae.txt'
opentxt = open(targettxt, 'r')
readtxt = opentxt.read()
input3 = "CTTGATCAT"

print(patternMatch(input3, readtxt))