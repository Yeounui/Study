'''
Created on 2016. 9. 14.

@author: korea
'''

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

u = ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/((x2-x1)**2+(y2-y1)**2)
xn = x1+u*(x2-x1)
yn = y1+u*(y2-y1)

d = ((xn-x3)**2+(yn-y3)**2)**(1/2)

print('nadir: ({}, {})'.format(xn, yn))
print('distance: {} nautical miles'.format(d))

if 0<=d<12 :
    statement = 'territorial waters'
elif 12<=d<24 :
    statement = 'contiguous zone'
elif 24<=d<200:
    statement = 'exclusive economic zone'
else :
    statement = 'international waters'

print('zone: {}'.format(statement))