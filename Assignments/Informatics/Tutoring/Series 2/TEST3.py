# Isomorse 2016

def morsecodes(giventxt):
    keydict = dict()
    with open(giventxt,'r') as opentxt:
        readtxt = opentxt.readlines()
        for line in readtxt:
            alphabet = line[0]
            morse = line[1:].strip()
            keydict[alphabet] = morse
    return keydict

    """
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
    """

def pattern(word, codes, complement=False, mirror=False):

    encoded = ''
    for letter in word:
        encoded += codes[letter]

    postcomplement = ''
    if complement:
        for letter in encoded:
            if letter == '.':
                postcomplement += '-'
            else:
                postcomplement += '.'
    else:
        postcomplement = encoded

    if mirror:
        postmirror = postcomplement[::-1]
    else:
        postmirror = postcomplement

    return postmirror

    """
    encoded_string = str()
    for letter in word:
        encoded_string += codes[letter]

    complement_adjusted = str()
    if complement:
        for encoded_letter in encoded_string:
            if encoded_letter == '.':
                encoded_letter = '-'
            else:
                encoded_letter = '.'
            complement_adjusted += encoded_letter
    else:
        complement_adjusted = encoded_string
    if mirror:
        complement_adjusted = complement_adjusted[::-1]
    return complement_adjusted
    """
    
def isomorse(word1, word2, codes, complement=False, mirror=False):
    encoded1 = pattern(word1, codes)
    encoded2 = pattern(word2, codes, complement, mirror)
    return bool(encoded1 == encoded2)

def groups(wordtxt, morsetxt):
    resultdict = dict()
    inputset = set()

    refer_dict = morsecodes(morsetxt)

    with open(wordtxt, 'r') as opentxt:
        word_list = opentxt.readlines()
    for word1 in word_list:
        inputset.add(word1) # value set
        for word2 in word_list:
            if word1 != word2:
                if isomorse(word1, word2, codes):
                    inputset.add(word2)
        resultdict[pattern(word1, codes)] = inputset
        inputset = set()
    return resultdict

    """
    morsedict = dict()
    candidated = list()
    inputset = set()

    codes = morsecodes(morsetxt)

    with open(wordtxt, 'r') as opentxt:
        readtxt = opentxt.readline()
        while readtxt:
            candidated.append(readtxt.strip())
            readtxt = opentxt.readline()

    for word1 in candidated:
        inputset.add(word1)
        for word2 in candidated:
            if word1 != word2:
                if isomorse(word1, word2, codes):
                    inputset.add(word2)
        morsedict[pattern(word1, codes)] = inputset
        inputset = set()
    return morsedict
    """