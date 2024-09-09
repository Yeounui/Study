'''
Created on 2017. 8. 16.

@author: korea
'''
def purple(givenlist):
    redcover = list()
    bluecover = list()
    marked = 0
    for atuple in givenlist:
        if atuple[-1] == 'R':
            redcover.append(atuple[:-1])
        else:
            bluecover.append(atuple[:-1])
    for redsquare in redcover:
        redrowlist = [x for x in range(redsquare[0], redsquare[0]+redsquare[2])]
        redcolumnlist = [x for x in range(redsquare[1], redsquare[1]+redsquare[3])]
        for bluesquare in bluecover:
            bluerowlist = [x for x in range(bluesquare[0], bluesquare[0]+bluesquare[2])]
            bluecolumnlist = [x for x in range(bluesquare[1], bluesquare[1]+bluesquare[3])]
            bluerowlist1 = list(bluerowlist)
            bluecolumnlist1 = list(bluecolumnlist)
            for rednumber in redrowlist:
                if rednumber in bluerowlist:
                    bluerowlist.remove(rednumber)
            rowlist = len(bluerowlist1) - len(bluerowlist)
            for rednumber in redcolumnlist:
                if rednumber in bluecolumnlist:
                    bluecolumnlist.remove(rednumber)
            columnlist = len(bluecolumnlist1) - len(bluecolumnlist)
            marked += (rowlist)*(columnlist)
    return marked

def cellophane(givenname):
    opentext = open(givenname, 'r')
    readtext = opentext.readline()
    appendlist = list()
    while readtext:
        readtext = readtext[0] + ' ' +readtext[1:]
        readtuple = tuple(readtext.split(' '))
        readtuple = (int(readtuple[1]), int(readtuple[2]), int(readtuple[3]), int(readtuple[4]), readtuple[0])
        appendlist.append(readtuple)
        readtext = opentext.readline()
    print(appendlist)
    return purple(appendlist)

print(purple([(0, 0, 5, 5, 'R'), (10, 0, 5, 5, 'R'), (3, 2, 9, 2, 'B')]))
print(cellophane('cellophane.txt'))