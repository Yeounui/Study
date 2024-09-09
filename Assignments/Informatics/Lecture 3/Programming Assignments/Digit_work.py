'''
Created on 2016. 9. 14.

@author: korea
'''
x = int(input())
y = int(input())

if (x<=5 and y<=5) or (x==10 or y==10) : #why '(x or y)==10' couldn't be? Answer: it's impossible.
    print(str(x) + ' x ' + str(y) + ' = ' + str(x*y))
elif (6 <= x <= 9 and 6 <= y <= 9) :
    print(str(x) + ' x ' + str(y) + ' = 10 x (' + str(x-5) + ' + ' + str(y-5) + ') + (' + str(10-x) + ' x ' + str(10-y) + ') = ' + str(x*y))
elif (11 <= x <= 15 and 11 <= y <= 15) :
    print(str(x) + ' x ' + str(y) + ' = 100 + 10 x (' + str(x-10) + ' + ' + str(y-10)+ ') + (' + str(x-10) + ' x ' + str(y-10)+ ') = ' + str(x*y))
else :
    print(str(x) + ' x ' + str(y) + ' = 100 + 10 x (' + str(x-10) + ' + ' + str(y-10)+ ') + (' + str(x-10) + ' x ' + str(y-10)+ ') = ' + str(x*y))