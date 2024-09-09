def _BoyerMooreHorspool(text, pattern):
    # Generate a dictionary for jump.
    jumpDict = dict()
    for keyBase in ["A", "G", "C", "T"]:
        jumpDict[keyBase] = len(pattern)
        for step, baseP in enumerate(pattern[-2::-1]):
            if keyBase == baseP:
                jumpDict[keyBase] = step + 1
                break

    print(jumpDict, pattern)

    #Search the match
    matchList = []
    currentEndT = len(pattern) - 1

    while currentEndT <= len(text):
        currentMatchP = len(pattern) - 1
        currentMatchT = int(currentEndT)
        while currentMatchP >= 0:
            if text[currentMatchT] != pattern[currentMatchP]:
                currentEndT += jumpDict[text[currentMatchT]]
                break
            currentMatchP -= 1
            currentMatchT -= 1
        if currentMatchP == -1:
            matchList.append(currentEndT - len(pattern) + 1)
    return matchList