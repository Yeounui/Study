'''
Created on 2016. 9. 23.

@author: korea
'''

f0=0
f1=1
m0=1
m1=0
t0=f0+m0
t1=f1+m1

generation = 2
G = int(input())

if G == 0:
    f2 = f0
    m2 = m0
    t2 = t0
elif G == 1:
    f2 = f1
    m2 = m1
    t2 = t1   
else:
    while generation<=G:
        f2=f0+f1
        m2=m0+m1
        t2=t0+t1
    
        generation+=1
    
        f0=f1
        f1=f2
        m0=m1
        m1=m2
        t0=t1
        t1=t2

print('number of female bees: {}' .format(f2))
print('number of male bees: {}' .format(m2))
print('total number of bees: {}' .format(t2))