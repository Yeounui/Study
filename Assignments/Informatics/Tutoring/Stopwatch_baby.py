'''
Created on 2018. 1. 11.

@author: korea
'''
birthdate = [0, 0, 2000]
newdate = [input(), input(), input()]
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
resultlist = []

for location in range(0, 3):
    watchdate = newdate[location]
    if watchdate in months:
        watchdate = months.index(watchdate) + 1
    resultdate = int(watchdate) - birthdate[location]
    resultlist.append(str(resultdate))

if resultlist[1] == '12':
    resultlist[1] = '0'
    resultlist[2] = str(int(resultlist[2]) + 1)       

if resultlist[0] == '1':
    resultlist[0] = '1 day'
else:
    resultlist[0] = resultlist[0] + ' days'
    
if resultlist[1] == '1':
    resultlist[1] = '1 month'
else:
    resultlist[1] = resultlist[1] + ' months'
    
if resultlist[2] == '1':
    resultlist[2] = '1 year'
else:
    resultlist[2] = resultlist[2] +' years' 

print('Stopwatch babies are {}, {} and {} old on {} {} {}.'.format(resultlist[0], resultlist[1], resultlist[2], newdate[0], newdate[1], newdate[2]))
    