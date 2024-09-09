'''
Created on 2017. 3. 5.

@author: korea
'''
def morsecodes(giventxt):
    keydict = dict()
    preread = open(giventxt, 'r')
    line = preread.readline()
    while line:
        lettercarrier = line[0]
        morsecarrier = line[1:].strip('\t').strip()
        keydict[lettercarrier] = morsecarrier
        line = preread.readline()
    preread.close()
    return keydict

def pattern(word, codes, complement= False, mirror= False):
    encoded = str()
    transformed = str()
    for letter in word:
        encoded += codes[letter]
    if complement:
        for encodedletter in encoded:
            if encodedletter == '.':
                encodedletter = '-'
            elif encodedletter == '-':
                encodedletter = '.'
            transformed += encodedletter
    else:
        transformed = encoded
    if mirror:
        transformed = transformed[::-1]
    return transformed

def isomorse(word1, word2, codes, complement= False, mirror= False):
    encoded1 = pattern(word1, codes)
    encoded2 = pattern(word2, codes, complement, mirror)
    if encoded1 == encoded2:
        return True
    else:
        return False
    
def groups(target, giventxt):
    morsedict = dict()
    candidated = list()
    inputset = list()
    codes = morsecodes(giventxt)
    opentarget = open(target, 'r')
    readtarget = opentarget.readline()
    while readtarget:
        candidated.append(readtarget.strip())
        readtarget = opentarget.readline()
    opentarget.close()
    for word1 in candidated:
        inputset.append(word1)
        for word2 in candidated:
            if word1 != word2:
                if isomorse(word1, word2, codes):
                    inputset.append(word2)
        morsedict[pattern(word1, codes)] = set(inputset)
        inputset.clear()
    return morsedict

#codes = morsecodes('C:/Users/korea/Documents/rorschach1.txt')

#print(pattern('TAIPAN', codes))

#print(pattern('TUDOR', codes, True, True))

print(groups('words.txt', 'morse.txt'))