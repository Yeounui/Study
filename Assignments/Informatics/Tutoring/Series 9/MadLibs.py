class MadLibs:
    def __init__(self):
        self.vocabulary = dict()

    def learn(self, Type, words):
        if (type(words) is set) or (type(words) is tuple) or (type(words) is list):
            words = [x.lower() for x in words]
            if Type in self.vocabulary.keys():
                if type(words) == str:
                    self.vocabulary[Type].add(words.lower())
                else:
                    self.vocabulary[Type].update(words)
            else:
                if type(words) == str:
                    self.vocabulary[Type] = set([words.lower()])
                else:
                    self.vocabulary[Type] = set(words)

    def suggest(self, condition):
        assert condition.lower() in self.vocabulary.keys(), 'unknown category'
        import random
        target = random.choice(list(self.vocabulary[condition.lower()]))
        if condition.isupper():
            return target.upper()
        elif condition[0].isupper():
            return target[0].upper() + target[1:]
        else:
            return target

    def fill(self, sentence):
        while '_' in sentence:
            initlocation = sentence.find('_')
            endlocation = sentence[initlocation + 1:].find('_') + initlocation + 1
            putin = self.suggest(sentence[initlocation + 1:endlocation])
            sentence = sentence.replace(sentence[initlocation:endlocation + 1], putin)
        return sentence