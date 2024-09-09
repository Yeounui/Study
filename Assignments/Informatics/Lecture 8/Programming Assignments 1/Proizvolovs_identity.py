'''
Created on 2016. 11. 9.

@author: korea
'''
def split(number, different = True):
    total = list()
    sequence = 0
    assert number%2 == 0 and number > 0, 'invalid length'
    import random
    template = list(range(1, number+1))
    random.shuffle(template)
    part1 = template[:(number//2)]
    if different:
        part2 = template[(number//2):]
    else:
        random.shuffle(template)
        part2 = template[:number//2]
    total.append(tuple(part1))
    total.append(tuple(part2))
    total = tuple(total)
    return total

def add(*given):
    result = 0
    part1s= list()
    part2s= list()
    assert len(given[0]) == len(given[1]), 'groups must have equal length'
    part1 = list(given[0])
    part2 = list(given[1])
    for queue in range(1, len(given[0])*2+1):
        if queue in part1:
            order = part1.count(queue)
            for number in range(order):
                part1s.append(queue)
        if queue in part2:
            order = part2.count(queue)
            for number in range(order):
                part2s.insert(0, queue)
    for queue in range(0, len(given[0])):
        result += abs(part1s[queue]-part2s[queue])
    return result

print(split(8))
print()