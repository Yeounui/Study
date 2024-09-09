'''
Created on 2018. 1. 4.

@author: korea
'''
target = input()
digit1 = target[0]
digit2 = target[1]
rownumber = 0
while target != None:
    target = input()
    rownumber += 1
    placeholder = target.replace(digit1, '').replace(digit2, '')
    if placeholder != '':
        columnnumber= target.find(placeholder) + 1
        break
print("character '{}' only occurs at row {} and column {}".format(placeholder, rownumber, columnnumber))