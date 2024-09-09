'''
Created on 2016. 10. 11.

@author: korea
'''
consonants = 'bcdfghjklmnpqrstwvxyzBCDFGHJKLMNPQRSTWVXYZ'
vowels = 'aeiouAEIOU'

def encode(name):
    encodename = ''
    concentrated = ''
    for letter in name:
        if letter in consonants:
            concentrated += letter
        elif letter in vowels:
            if concentrated == '':
                encodename += letter
            else:
                encodename += concentrated + 'o' + concentrated.lower() + letter
                concentrated = ''
        else:
            if concentrated == '':
                encodename += letter
            else:
                encodename += concentrated + 'o' + concentrated.lower() + letter
                concentrated = ''
    if concentrated != '':
        encodename += concentrated + 'o' + concentrated.lower()
    return encodename

def decode(code):
    concentrated = 0
    concentrating = 0
    initsize = 0
    word = ''
    while concentrating < len(code):
        if code[concentrating] in consonants:
            concentrated += 1
            concentrating += 1
        elif code[concentrating] in vowels:
            if concentrating + concentrated + 1 == len(code):
                if initsize == concentrating:
                    word += code[initsize]
                else:    
                    word += code[initsize:concentrating]
                break
            elif concentrated == 0:
                word += code[concentrating]
                initsize = concentrating + 1
                concentrating += 1
            else:
                word += code[initsize:concentrating] + code[concentrating + concentrated + 1]
                initsize = concentrating + concentrated + 2
                concentrating += concentrated + 2
                concentrated = 0
        else:
            word += code[concentrating]
            concentrating += 1
            initsize += 1

    return word