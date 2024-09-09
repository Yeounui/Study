'''
Created on 2016. 9. 14.

@author: korea
'''
days = int(input())
month = input()
years = int(input())

if month == 'january':
    nummonth = 1
elif month == 'february':
    nummonth = 2
elif month == 'march':
    nummonth = 3
elif month == 'april':
    nummonth = 4
elif month == 'may':
    nummonth = 5
elif month == 'june':
    nummonth = 6
elif month == 'july':
    nummonth = 7
elif month == 'august':
    nummonth = 8
elif month == 'september':
    nummonth = 9
elif month == 'october':
    nummonth = 10
elif month == 'november':
    nummonth = 11
else:
    nummonth = 0

if days == 1 :
    Expday = '1 day'
else :
    Expday = '{} days' .format(days)
    
if nummonth == 1 :
    Expmonth = '1 month'
else :
    Expmonth = '{} months' .format(nummonth)

if years == 2001 :
    Expyear = '1 year'
else :
    Expyear = '{} years' .format(years-2000)
    
if month == 'december' :
    if years == 2000 :
        Expyear = '1 year'
    else :
        Expyear = '{} years' .format(years-1999)
else:
    pass
    
print('Stopwatch babies are {}, {} and {} old on {} {} {}.'.format(Expday, Expmonth, Expyear, days, month, years))