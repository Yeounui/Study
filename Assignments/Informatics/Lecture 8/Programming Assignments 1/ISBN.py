'''
Created on 2016. 11. 2.

@author: korea
'''
def ISBN13(code):
    oddnum = 0
    evenum = 0

    for digit in code[0: 12: 2]:
        oddnum += int(digit)
    for digit in code[1: 12: 2]:
        evenum += int(digit)
    calculated = (10-(oddnum + 3*evenum)%10)%10
    given = int(code[-1])
    if given  == calculated:
        return True
    else:
        return False
    
def ISBN10(code):
    given = None
    calculated = 0
    for order in range(1, 10):
        calculated += order*int(code[order-1])
    calculated %= 11
    given = code[-1]
    if code[-1] == 'X':
        given = 10
    if int(given) == calculated:
        return True
    else:
        return False

def isISBN(code, check = True):
    if check:
        if len(code) == 13:
            return ISBN13(code)
        else:
            return False
    else:
        if len(code) == 10:
            return ISBN10(code)
        else:
            return False
    
def areISBN(code, check = None):
    result = list()
    for queue in code:
        if type(queue) != str:
            result.append(False)
        else:
            if len(queue) == 13:
                if check:
                    result.append(ISBN13(queue))
                elif check == False:
                    result.append(False)
                else:
                    result.append(ISBN13(queue))
            elif len(queue) == 10:
                if check:
                    result.append(False)
                elif check == False:
                    result.append(ISBN10(queue))
                else:
                    result.append(ISBN10(queue))
            else:
                result.append(False)
    
    return result

print(isISBN('9789027439642', False))
print(areISBN(['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146'], False))