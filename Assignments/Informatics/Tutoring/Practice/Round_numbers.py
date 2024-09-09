'''
Created on 2017. 8. 11.

@author: korea
'''
firstnum = int(input())
secondnum = int(input())
thirdnum = int(input())
forthnum = int(input())

print('{}-{}-{}-{}'.format(str(firstnum), str(secondnum), str(thirdnum), str(forthnum)))

while not (firstnum == secondnum and firstnum == thirdnum and firstnum == forthnum):
    prefirstnum = abs(firstnum - secondnum)
    presecodnum = abs(secondnum - thirdnum)
    prethirdnum = abs(thirdnum - forthnum)
    preforthnum = abs(forthnum - firstnum)
    
    firstnum = prefirstnum
    secondnum = presecodnum
    thirdnum = prethirdnum
    forthnum = preforthnum
    
    print('{}-{}-{}-{}'.format(str(firstnum), str(secondnum), str(thirdnum), str(forthnum)))