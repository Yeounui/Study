'''
Created on 2017. 3. 11.

@author: korea
'''
import datetime

class Stardate:
    def __init__(self, day = datetime.date.today()):
        assert type(day) == datetime.date
        self.day = day
        self.trigger = 0
    
    def __repr__(self):
        return 'Stardate(datetime.date({}, {}, {}))'.format(self.day.year, self.day.month, self.day.day)
    
    def __str__(self):
        if self.trigger == 0: # new
            monthday = self.day.timetuple().tm_yday - 1
            #print(monthday)
            yearday = ((self.day- self.day.replace(year = self.day.year-1)) + datetime.date.min).toordinal()-1
            #print(yearday)
            #print((monthday+2)/yearday)
            arranged = int(monthday/yearday*100)
            return'{}.{:02d}'.format(self.day.year, arranged)
        else: # old
            if self.day.year > 1999:
                additionalyear = int(str(self.day.year)[:2]) - 19
                partyear = int(str(self.day.year)[2:])
            else:
                additionalyear = str()
                partyear = int(str(self.day.year)[2:])
            return '{}{:02d}{:02d}.{:02d}'.format(additionalyear, partyear, self.day.month, self.day.day)

    def switch(self):
        if self.trigger == 0:
            self.trigger = 1
        else:
            self.trigger = 0
'''           
date = Stardate(datetime.date(1955, 9, 2))
print(repr(date))
print(date.trigger)
print(str(date))
print(date)
date.switch()
print(date)
date.switch()
print(date)
'''
stardate = Stardate(datetime.date(2015, 7, 6))
stardate.switch()
print(stardate)
stardate.switch()
print(stardate)