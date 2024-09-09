'''
Created on 2016. 9. 23.

@author: korea
'''
x=input()
n=1
total=0

while x != 'stop':
    while n <= 9:
        total+=n*int(x)
        n+=1
        x=input()
    ISBN=total%11
    if ISBN == int(x):
        print('OK')
    else:
        print('WRONG')
    n=1
    total=0
    x=input()