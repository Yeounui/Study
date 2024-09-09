def rotateLeft(givennumber):
    givennumber = str(givennumber)
    givennumber = givennumber[1:] + givennumber[0]
    return int(givennumber)

def rotateRight(givennumber):
    givennumber = str(givennumber)
    givennumber = givennumber[-1] + givennumber[:-1]
    return int(givennumber)

def parasitic(givennumber):
    for parasiticnum in range(1,10):
        comparednum = parasiticnum * givennumber
        if comparednum == rotateRight(givennumber):
            return parasiticnum
    return 0

def corkscrew(parasiticdigit, startdigit):
    resultnum = parasiticdigit * startdigit
    count = 1
    leftnum = 0
    targetnum = 0
    while rotateRight(targetnum) != resultnum:
        leftnum = str(resultnum)[-count:]
        count += 1
        targetnum = int(leftnum + str(startdigit))
        resultnum = parasiticdigit * targetnum
    return targetnum
    
print(rotateLeft(10526315784736842))
print(rotateRight(179487))
print(parasitic(179487))
print(parasitic(1234))
print(parasitic(105263157894736842))
print(corkscrew(4, 7))
print(corkscrew(5, 7))
print(corkscrew(2, 2))