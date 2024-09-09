'''
Created on 2016. 10. 3.

@author: korea
'''

para=input()
n=1
total=0

while para != 'stop':
    for letter in para[0:9]:
        total+=n*int(letter)
        n+=1
    ISBN=str(total%11)
    check=para[9]
    if check == 'X':
        check='10'
    if ISBN == check:
        print('OK')
    else:
        print('WRONG')
    n=1
    total=0
    para=input()