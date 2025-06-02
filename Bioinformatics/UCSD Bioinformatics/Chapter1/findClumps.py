def enrollPattern(freqMap, clumpList, pattern, t):
    if pattern not in freqMap.keys():
            freqMap[pattern] = 1
    else:
        freqMap[pattern] += 1
        if ((freqMap[pattern] >= t) and
            (pattern not in clumpList)):
            clumpList.append(pattern)
        else:
            pass

def findClumps(text, k, L, t):
    freqMap = dict()
    clumpList = list()
    for i in range(L-k+1):
        pattern = text[i:i+k]
        enrollPattern(freqMap, clumpList, pattern, t)
    
    for i in range(len(text) - L + 1):
        patternNew = text[i+L-k+1:i+L+1]
        freqMap[text[i:i+k]] -= 1
        enrollPattern(freqMap, clumpList, patternNew, t)
    return len(clumpList)

targettxt = './Study/Bioinformatics/UCSD Bioinformatics/Chapter1/E_coli.txt'
opentxt = open(targettxt, 'r')
readtxt = opentxt.read()
print(findClumps(readtxt, 9, 500, 3))