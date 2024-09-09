'''
Created on 2016. 9. 14.

@author: korea
'''
Age =  int(input())
Level = int(input())

if Age<=6:
    if Level<=29:
        print('CF is very unlikely')
    elif 30<=Level<=59:
        print('CF is possible')
    else:
        print('CF is likely')
else:
    if Level<=39:
        print('CF is very unlikely')
    elif 40<=Level<=59:
        print('CF is possible')
    else:
        print('CF is likely')