from reverseComplement import reverseComplement
from frequentWords import maxMap
from frequentWordsWithMismatches import generateVarSet

def frequencyTableWithMismatches(text, k, d):
    freqMap = dict()
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        varSet = set([pattern, reverseComplement(pattern)])
        varSet = generateVarSet(varSet, d)
        while varSet:
            element = varSet.pop()
            if element not in freqMap.keys():
                freqMap[element] = 1
            else:
                freqMap[element] += 1
    return freqMap

def FrequentWordsWithMismatchesPlusReverse(text, k, d):
    frequentPatterns = list()
    freqMap = frequencyTableWithMismatches(text, k, d)

    max = maxMap(freqMap)
    print(max)
    for key in freqMap.keys():
        if (freqMap[key] == max):
            frequentPatterns.append(key)
    return frequentPatterns

if __name__ == "__main__":
    text = "CCAACTCTCCACTAGTAGTACTCCAAGTACTTCACTTCACTACTACTCTAGTCTACTCTACTACTTCCTTCTCCTACTACTTCACTTCCTCTTCCTAGTTCAGTTCAGTACTAGTAGTCCAACTAGTACTCTCTCTTCCCATCACTCCAAGTTCCCATCAGTACTCTCCATCAGTAGTACTCCAAGTACTACTACTACTAGTCTCCACCACCACCACCACCACCATCAGTTCAGTAGTCCAAGTAGT"
    k, d = 6, 2
    print(FrequentWordsWithMismatchesPlusReverse(text, k, d))