'''
Created on 2016. 10. 11.

@author: Seungchan Oh
@student_number: 01603277
'''
def pangram(sentence):
    # Definition
    precede = set(sentence.lower())
    remove = set()
    # collecting non alphabet letters
    for element in precede:
        if not element.isalpha():
            remove.add(element)
    # eliminating non alphabet letters from precede
    precede= precede - remove
    # checking all alphabet inside
    if len(precede) == 26:
        return True
    else:
        return False

def window(sentence):
    # definition
    result = ''
    for length in range(26, len(sentence)+1): # deciding length
        for locus in range(0, len(sentence)-25): # deciding startpoint
            domain = sentence[locus:locus+length]
            # checking whether the partial sentence is pangram or not
            if pangram(domain):
                return domain