'''
Created on 2016. 11. 10.

@author: korea
'''
def fitness(word1, word2):
    assert len(word1) == len(word2), 'strings must have equal length'
    result = 0
    for sequence in range(0, len(word1)):
        if word1[sequence] == word2[sequence]:
            result += 1       
    return result

def mutation(word, mutations = 1):
    assert len(word) >= mutations >= 0, 'invalid number of mutations' 
    loci = list()
    import random
    alphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'V', 'X', 'Y', 'Z']
    loci = random.sample(range(0, len(word)), mutations)
    for locus in loci:
        alphabet.remove(word[locus])
        changed = random.choice(alphabet)
        alphabet.append(word[locus])
        word = word[:locus] + changed +word[locus+1:]
    return word

def crossover(word1, word2, point = -1):
    import random
    if point == -1:
       point = random.randrange(1, len(word1))
       print(point)
       print(type(point))
    assert len(word1) == len(word2), 'strings must have equal length'
    assert len(word1) > point > 0, 'invalid crossover point'
    word3 = word1[:point] + word2[point:]
    word4 = word2[:point] + word1[point:]
    return (word3, word4)
print(fitness('WEASEL', 'WETSEL'))
print(mutation('WEASEL'))
print(crossover('WEASEL', 'DONKEY'))