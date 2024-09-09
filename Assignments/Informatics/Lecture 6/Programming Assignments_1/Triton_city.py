'''
Created on 2016. 10. 11.

@author: korea
'''
def factorial(target):
   
    queue = 1
    result = 1
    
    if target == 0:
        result = 1
    else:
        while queue <= target:
            result *= queue
            queue += 1
    return result

def binomialCoefficient(target, order):
    if 0 <= order <= target:
        result = int(factorial(target) / (factorial(order) * factorial(target-order)))
    else:
        result = 0
    return result

def triangularNumber(target):
    result = binomialCoefficient(target+1, 2)
    return result

def tetrahedralNumber(target):
    result = binomialCoefficient(target+2, 3)
    return result