'''
Created on 2016. 10. 3.

@author: korea
'''
para=input()
n=1

for n in range(1, len(para)):
    x1=int(para[0:n])
    x2=int(para[n:])
    if (x1 + x2)**2 == int(para):
        print('torn')
        break
    else:
        if n == len(para)-1:
            print('not torn')