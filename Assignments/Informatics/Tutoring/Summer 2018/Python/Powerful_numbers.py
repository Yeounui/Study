'''
Created on 2018. 6. 30.

@author: korea
'''
givennumber = input()
for powernumber in range(1, len(givennumber)+3):
    sumnumber = 0
    for digit in givennumber:
        sumnumber += int(digit)**powernumber
    if sumnumber >= int(givennumber):
        break
        
if sumnumber == int(givennumber):
    blank1 = ''
    blank2 = ' of order ' + str(powernumber)
else:
    blank1 = 'not '
    blank2 = ''
print('{} is {}a powerful number{}'.format(givennumber, blank1, blank2))