'''
Created on 2016. 10. 25.

@author: korea
'''
def vector(aline):
    result = [(0, 0)]
    for base in aline:
        if base == 'A':
            result.append((result[-1][0] - 1, result[-1][1]))
        elif base == 'G':
            result.append((result[-1][0], result[-1][1] - 1))
        elif base == 'C':
            result.append((result[-1][0], result[-1][1] + 1))
        else:
            result.append((result[-1][0] + 1, result[-1][1]))
    return result

def replicatie(aline):
    yvalue = 0
    minimum = 0
    maximum = 0
    maxiorder = 0
    miniorder = 0
    maxicode = ''
    minicode = ''
    for order in range(0, len(aline)):
        base = aline[order]
        if base == 'G':
            yvalue -= 1
        elif base == 'C':
            yvalue += 1
            
        if minimum > yvalue:
            minimum = yvalue
            miniorder = order
            minicode = aline[0:order+1]
        if maximum < yvalue:
            maximum = yvalue
            maxiorder = order
            maxicode = aline[0:order+1]
    
    for base in minicode:
        if base == 'G' or base == 'C':
            miniorder += 1
            break
    for base in maxicode:
        if base == 'G' or base == 'C':
            maxiorder += 1
            break
        
    return (maxiorder, miniorder)
    
def sequentie(orbit):
    code = ''
    for queue in range(0, len(orbit)-1):
        base = (orbit[queue + 1][0] - orbit[queue][0], orbit[queue + 1][1] - orbit[queue][1])
        if base == (-1, 0):
            code += 'A'
        elif base == (0, -1):
            code += 'G'
        elif base == (0, 1):
            code += 'C'
        else:
            code += 'T'       
    return code

print(replicatie('ACTATCAGTTATTAC'))
print(vector('CTGGGGTAA'))
print(sequentie([(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, 2), (1, 2), (1, 1), (2, 1)]))