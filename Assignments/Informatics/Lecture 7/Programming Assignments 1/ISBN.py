'''
Created on 2016. 10. 25.

@author: korea
'''
def isISBN(code):
    value = '1234567890'
    multiply = 1
    calculated = 0
    initorder = 0
    domain = []
    ISBN = ''
    
    if len(code) != 13 or code != str(code):
        return False
    
    for number in code[:-1]:
        if not number in value and number != '-':
            return False
    
    for order in range(0, 13):
         if code(order) == '-':
             domain.append(code[initorder:order])
             initorder = order + 1
    if len(domain[0]) != 1 or len(domain[1]) != 4 or len(domain[2]) != 4:
        return False
    
    domain.append(code[-1])
    
    for order in range(0, 3):
        ISBN += domain[order]
    order = 1
    determinent = 0
    for letter in ISBN[:-1]:
        determinent += order*int(letter)
    determinent %= 11
    
    if ISBN[-1] == 'X':
        Last = 10
    else:
        Last = int(ISBN[-1])
    
    if Last == determinent:
        return True
    else:
        return False
    
    print(isISBN('997-150-210-0'))