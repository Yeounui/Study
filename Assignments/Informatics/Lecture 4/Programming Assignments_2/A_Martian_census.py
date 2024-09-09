'''
Created on 2016. 9. 23.

@author: Oh, Seungchan (0160323277)
'''
#definations
#each variables meet two conditons: 'o <= x <= y <= z <= b' and '4/n = 1/x + 1/y + 1/z'
n=int(input())
o=int(input())
b=int(input())

#initializations
x=o
y=o
z=o

#the roop is for increasing the value of variables one by one. If one variable reaches to 'b',
#one of the other variable increases and the past variable becomes initialized.
#After each variables are determined, the coding checks out whether determined values meet the conditions.
for x in range(o,b+1):
    for y in range(x,b+1):
        for z in range(y,b+1):
            if 4*x*y*z == n*(x*y + y*z + x*z):
                print('4/{} = 1/{} + 1/{} + 1/{}'.format(n, x, y, z))
                continue
            else:
                continue
        
    