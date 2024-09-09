'''
Created on 2016. 10. 25.

@author: korea
'''
def consecutive(line):
    minimum = 0
    maximum = 0
    trigger = 0
    for number in line:
        if line.count(number) != 1:
            return False
        if minimum > number or minimum == 0:
            minimum = number
        if maximum < number or maximum == 0:
            maximum = number
        
    for queue in range(minimum, maximum+1): #
        if queue not in line:
            return False
        if queue == maximum:
            return True

def goldilocks(line):
    minimum = 0
    maximum = 0
    trigger = 0
    cation = 0
    for number in line:
        if line.count(number) != 1:
            return None
        if minimum > number or minimum == 0:
            minimum = number
        if maximum < number or maximum == 0:
            maximum = number
    for queue in range(minimum, maximum + 1):
        if queue not in line:
            cation += 1
            if cation == 2:
                return None
            result = queue
    if cation == 1:
        return result
    
def move1(line):
    addnum = goldilocks(line)
    change = list(line)
    if addnum != None:
        change.append(addnum)
    return change

def move2(line):
    if consecutive(line):
        return None
    else:
        if not goldilocks(line):
            return None
        else: 
            line.append(goldilocks(line)) #the latest value remains
            return 
shells = [16, 13, 18, 17, 15, 14, 20]
move2(shells)
print(shells)