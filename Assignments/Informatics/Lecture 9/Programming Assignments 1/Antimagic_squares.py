'''
Created on 2016. 11. 14.

@author: korea
'''
def numbers(group):
    result = set()
    for line in group:
        result.update(line)
    return result

def sums(group):
    element1 = 0
    element2 = 0
    element3 = 0
    element4 = 0
    result = set()
    for oneorbit in range(len(group)):
        for twoorbit in range(len(group)):
            element1 += group[oneorbit][twoorbit]
            element2 += group[twoorbit][oneorbit]
        result.add(element1)
        result.add(element2)
        element1 = 0
        element2 = 0
    for orbit in range(len(group)):
        element3 += group[orbit][orbit]
        element4 += group[orbit][len(group)-orbit-1]
    result.add(element3)
    result.add(element4)
    element3 = 0
    element4 = 0
    return result
    
def magic(group):
    result = list()
    for queue in group:
        result += queue
    if len(result) != len(numbers(group)):
        return False
    else:
        if len(sums(group)) == 1:
            return True
        else:
            return False

def hetero(group):
    result = list()
    for queue in group:
        result += queue
    if len(result) != len(numbers(group)):
        return False
    else:
        if len(sums(group)) == (len(group)+1)*2:
            return True
        else:
            return False

def antimagic(group):
    result = list()
    largest = None
    for queue in group:
        result += queue
    target = sums(group)
    for queue in target:
        if largest == None:
            largest = queue
            smallest = queue
        else:
            if queue > largest:
                largest = queue
            if queue < smallest:
                smallest = queue
            
    if len(result) != len(numbers(group)):
        return False
    else:
        if len(target) == largest-smallest+1:
            if len(target) == 1:
                return False
            else:
                return True
        else:
            return False
    
        
group = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(numbers(group))
print(sums(group))
