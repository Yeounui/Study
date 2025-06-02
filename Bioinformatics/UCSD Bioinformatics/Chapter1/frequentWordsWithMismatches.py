from frequentWords import maxMap

def generateVarSet(givenSet, d):
    if d == 0:
        return givenSet
    
    givenList = list(givenSet)
    for element in givenList:
        j = 0
        while j < len(element):
            givenSet.add(element[:j] + 'A' + element[j + 1:])
            givenSet.add(element[:j] + 'G' + element[j + 1:])
            givenSet.add(element[:j] + 'C' + element[j + 1:])
            givenSet.add(element[:j] + 'T' + element[j + 1:])
            j += 1
    
    if d > 1:
        givenSet = generateVarSet(givenSet, d-1)
        
    return givenSet
        
        

def frequencyTableWithMismatches(text, k, d):
    freqMap = dict()
    for i in range(len(text)-k+1):
        varSet = set([text[i:i+k],])
        varSet = generateVarSet(varSet, d)
        while varSet:
            element = varSet.pop()
            if element not in freqMap.keys():
                freqMap[element] = 1
            else:
                freqMap[element] += 1
            
    return freqMap

def FrequentWordsWithMismatches(text, k, d):
    frequentPatterns = list()
    freqMap = frequencyTableWithMismatches(text, k, d)
    max = maxMap(freqMap)
    for key in freqMap.keys():
        if (freqMap[key] == max):
            frequentPatterns.append(key)
    return ' '.join(frequentPatterns)



if __name__ == "__main__":
    Text = 'AACAGCAGCGTACGCAGTAAACAACAGCCGCACGCAGTAAACTCTTGTACGCAAGCTCTTAACCGCATCTTAGCCGCAAGCAACTCTTTCTTAACTCTTAGCAACAACGTAAACAACAACCGCAGTAAACAACAGCGTAAACAACGTAAACGTAAGCCGCAGTACGCATCTTAACAGCAGCAGCTCTTCGCAAGCCGCACGCAAACTCTTAACTCTTAACCGCACGCAAACCGCAAGCGTAGTAAGCAACAGCGTAAGCAGCAGCAGCCGCATCTTCGCAAGCAACCGCAAGCCGCAGTACGCATCTTCGCAAGCGTAGTATCTTTCTTCGCAGTAAACGTATCTTTCTT'
    k = 7
    d = 3
    print(FrequentWordsWithMismatches(Text, k, d))