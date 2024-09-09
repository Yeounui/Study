'''
Created on 2017. 3. 18.

@author: Seungchan Oh
@student_number: 01603277
'''
class MadLibs:
    def __init__(self):
        #define dictionary for incoming words 
        self.vocabulary = dict()
        
    def learn(self, Type, words):
        # unify group of words to list of lowercase words
        if (type(words) is set) or (type(words) is tuple) or (type(words) is list):
            words = [x.lower() for x in words]
        # In case of that type is already in dictionary, word or group of words is added in dictionary
        if Type in self.vocabulary.keys():
            if type(words) == str:
                self.vocabulary[Type].add(words.lower())
            else:
                self.vocabulary[Type].update(words)
        # if the type doesn't exist in, append word or group of words with type
        else:
            if type(words) == str:
                self.vocabulary[Type] = set([words.lower()])
            else:
                self.vocabulary[Type] = set(words)
    
    def suggest(self, condition):
        # check whether the word in condition is in dictionary or not
        assert condition.lower() in self.vocabulary.keys(), 'unknown category'
        import random
        # randomly choose a word
        target = random.choice(list(self.vocabulary[condition.lower()]))
        # As the condition indicates, the word is transformed. 
        if condition.isupper():
            return target.upper()
        elif condition[0].isupper():
            return target[0].upper() + target[1:]
        else:
            return target
        
    def fill(self, sentence):
        # blanks start with '_', so until they are clearly replaced  
        while '_' in sentence:
        # space between initlocation and endlocation should be replaced and filled with word 
            initlocation = sentence.find('_')
            endlocation = sentence[initlocation+1:].find('_') + initlocation + 1
        # key value is included in condition, therefore we utilize it to get the proper formed word
            putin = self.suggest(sentence[initlocation+1:endlocation])
        # replace a condition to a word
            sentence = sentence.replace(sentence[initlocation:endlocation+1], putin)
        return sentence
    
madlib = MadLibs()
madlib.learn('name', 'God')
madlib.learn('thing', 'war')
madlib.learn('citizens', 'Americans')
madlib.learn('discipline', 'geography')
#print(madlib.vocabulary)
print(madlib.fill('_Name_ created _thing_ so that _CITIZENS_ would learn _discipline_.'))

madlib.learn('name', ('Mercator', 'Caesar'))
madlib.learn('thing', ['maps', 'coordinates'])
madlib.learn('citizens', {'Belgians', 'Martians', 'Germans'})
madlib.learn('discipline', 'navigation')
madlib.learn('discipline', 'colonisation')
#print(madlib.vocabulary)

#print(madlib.suggest('name'))
#print(madlib.suggest('NAME'))
#print(madlib.suggest('Name'))