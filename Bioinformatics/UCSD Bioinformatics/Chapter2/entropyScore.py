from numpy import log2

def entropyScore(text):
    textList = text.split(' ')
    textNum = len(textList)
    
    scoreList = list()
    for i in range(len(textList[0])):
        scoreSum = 0
        collectList = [0, 0, 0, 0] # A, T, C, G
        for text in textList:
            if text[i] == 'A':
                collectList[0] += 1
            elif text[i] == 'T':
                collectList[1] += 1
            elif text[i] == 'C':
                collectList[2] += 1
            elif text[i] == 'G':
                collectList[3] += 1
            else:
                return 1
        
        for j in collectList:
            if j != 0:
                floatJ = j / textNum
                scoreSum -= (floatJ) * log2(floatJ)
            
        scoreList.append(scoreSum)
    
    print(scoreList)    
    sum = 0
    for k in scoreList:
        sum += k
    return sum

text = "TCGGGGGTTTTT CCGGTGACTTAC ACGGGGATTTTC TTGGGGACTTTT AAGGGGACTTCC TTGGGGACTTCC TCGGGGATTCAT TCGGGGATTCCT TAGGGGAACTAC TCGGGTATAACC"
print(entropyScore(text))