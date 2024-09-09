'''
Created on 2016. 10. 11.

@author: korea
'''
def encodeLetter(alphabet, number, language):
    language = language.lower()
    alphabet = alphabet.lower()
    result = language.find(alphabet) + 1 + number
    return result

def encodeWord(word, number, language):
    result =''
    for letter in word:
       result += str(encodeLetter(letter, number, language))
    result=int(result)
    return result