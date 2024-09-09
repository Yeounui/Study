'''
Created on 2016. 11. 14.

@author: Seungchan Oh
@student_number: 01603277
'''
from datetime import date, timedelta
#import datetime

def birthday(bornyear, thisyear):
    if bornyear.month == thisyear.month and bornyear.day == thisyear.day:
        return True
    else:
        return False

def sameweekday(compare1, compare2):
    if compare1.weekday() == compare2.weekday() and compare1.day == compare2.day:
        return True
    else:
        return False
    
def hundredday(compare1, compare2):
    leftover = (compare2 - compare1).days % 100
    if leftover == 0:
        return True
    else:
        return False
    
def unbirthday(bornyear, thisyear):
    determinent = birthday(bornyear, thisyear)
    if determinent:
        return False
    else:
        return True

def birthdays(date, birthday = birthday, start = None, end = date.today()):
    #definition
    if start == None:
        start = date
    result = list()
    queue = date
    # going onto one by one and checking condition
    while queue <= end:
        if birthday(date, queue) and queue >= start:
             result.append(queue)
        queue += timedelta(days = 1)
    return tuple(result)