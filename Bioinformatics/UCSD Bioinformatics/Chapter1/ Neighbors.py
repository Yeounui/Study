from frequentWordsWithMismatches import generateVarSet

def neighbors(pattern, d):
    givenSet = set([pattern,])
    givenSet = generateVarSet(givenSet, d)
    return givenSet

if __name__ == "__main__":
    pattern = 'TGCAT'
    d = 2
    print(len(neighbors(pattern, d)))