'''
Created on 2016. 10. 25.

@author: korea
'''



def lineup(given):
    organized = list()
    result = list()
    rhat = ''
    bhat = ''
    organized.append(given[0])
    if given[0][1] == 'R':
        rhat = 'R'
    else:
        bhat = 'B'
    for order in range(1, len(given)):
        if rhat == 'R' and bhat == '':
            organized.append(given[order])
        elif rhat == '' and bhat == 'B':
            organized.insert(0, given[order])
        else:
            for queue in range(0, len(organized)):
                if organized[queue][1] == 'B':
                    organized.insert(queue, given[order])
                    break
        if given[order][1] == 'R':
            rhat = 'R'
        else:
            bhat = 'B'
    
    for order in range(0, len(organized)):
        result.append(organized[order][0])
        
    return result

print(lineup([('Alice', 'R'), ('Bob', 'B'), ('Claire', 'R'), ('Dave', 'R'), ('Elsa', 'B')]))