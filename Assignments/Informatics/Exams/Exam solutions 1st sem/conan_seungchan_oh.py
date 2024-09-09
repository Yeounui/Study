'''
Created on 2016. 11. 31.

@author: Seungchan Oh
@number: 01603277
'''
#definition
daughtertimes = int(input())
daughterconst = int(input())
experimentsec= int(input())
mothernum2= int(input())
trigger = 1
initnum = 1
secondneeded = 0

# calculating cell population from cell divisions in the given seconds
while 0 <= trigger <= experimentsec:
    cellnum = daughtertimes * initnum + daughterconst
    trigger += 1 # seconds in the recent stage
    initnum = cellnum
# for grammar
if cellnum in [0, 1]:
    pluralcell = ''
else:
    pluralcell = 's'  
if experimentsec in [0, 1]:
    pluralsec = ''
else:
    pluralsec = 's'

print('experiment #1: {} cell{} after {} second{}'.format(cellnum, pluralcell, experimentsec, pluralsec))
# cell division happens until the population of cell overcomes the first result.
while mothernum2 < cellnum:
    secondneeded += 1 # counting seconds
    cellnum2 = daughtertimes * mothernum2 + daughterconst
    mothernum2 = cellnum2
# for grammar
if cellnum in [0, 1]:
    pluralcell = ''
else:
    pluralcell = 's'
if secondneeded in [0, 1]:
    pluralsec = ''
else:
    pluralsec = 's'

print('experiment #2: {} cell{} after {} second{}'.format(cellnum2, pluralcell, secondneeded, pluralsec))