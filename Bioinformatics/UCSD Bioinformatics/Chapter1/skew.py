def skew(strand):
    score = 0
    skewList = ['0',]
    for i in strand:
        if i == "C":
            score -= 1
        elif i =="G":
            score += 1
        else:
            pass
        skewList.append(str(score))
    
    return ' '.join(skewList)

def skewMinimum(strand):
    score = 0
    minPosList = []
    dMinusPlus = False
    minVal = 0
    for i, j in enumerate(strand):
        if j == "C":
            score -= 1
            if score <= minVal:
                if score < minVal:
                    minVal = score
                    minPosList.clear()
                else:
                    dMinusPlus = True
        else:
            if j =="G":
                score += 1
                if dMinusPlus is True:
                    minPosList.append(i)
                dMinusPlus = False
            
    return minPosList

if __name__ == "__main__":
    strand = 'GCATACACTTCCCAGTAGGTACTG'
    print(skew(strand))
    print(skewMinimum(strand))