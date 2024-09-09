'''
Created on 2016. 9. 23.

@author: korea
'''
table=int(input())
money=int(input())
times=int(input())
statement=input()

n=1

total=0

while n < table :
    if n % times == 0:
        total+= money* n
        total= total* 2
        print('table #{} (x2): \u20ac{}'.format(n, total))  #\u20ac is euro, \u20A9 is won
    else:
        total+= money* n
        print('table #{}: \u20ac{}'.format(n, total))
    n+=1
if statement == 'stopped':
    if n % times == 0:
        total+= money* n
        total= total* 2
        print('table #{} (x2): \u20ac{}'.format(n, total))
    else:
        total+= money* n
        print('table #{}: \u20ac{}'.format(n, total))
else:
        print('table #{}: \u20ac{}'.format(n, int(total/2)))