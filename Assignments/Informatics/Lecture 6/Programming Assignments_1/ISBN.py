'''
Created on 2016. 10. 11.

@author: korea
'''

def isISBN(ISBN):
    
    alphabet = 'ABCDEFGHIGKLMNOPQRSTUWVXYZ'
    order = 1
    queue = 0
    
    if ISBN != str(ISBN):
        result = False
        return result
    if len(ISBN) != 10:
        result = False
        return result
    for number in ISBN[:-1]:
        if number in alphabet:
            result = False
            return result
        else:
            queue += order*int(number)
            order += 1
    
    if ISBN[-1] in alphabet:
        if ISBN[-1] == 'X':
            x10 = 10
        else:
            result = False
            return result
    else:
        x10 = int(ISBN[-1])
    
    result = (x10 == queue % 11)
    return result