'''
Created on 2016. 11. 14.

@author: korea
'''
def letterFrequencies(sentence):
    sentence = sentence.lower()
    dict = {}
    for letter in sentence:
        if letter.isalpha():
            dict[letter] = dict.get(letter, 0) + 1
    return dict

def letterPositions(sentence):
    subject = sentence.lower()
    preresult = set()
    result = {}
    preadded = 0
    series = letterFrequencies(sentence)
    for letter in series:
        print(letter)
        for sequence in range(series[letter]):
            added = subject.find(letter)
            preresult.add(added+preadded)
            preadded = preadded + added+1
            subject = subject[added+1:]
        if letter == sentence[0]:
            preresult.add('0')
            preresult.remove(0)
        subject = sentence.lower()
        preadded = 0
        result[letter] = preresult
        preresult = set()
    return result
            
                    
print(letterFrequencies("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's"))
positions = letterPositions("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
print(letterPositions("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's"))             