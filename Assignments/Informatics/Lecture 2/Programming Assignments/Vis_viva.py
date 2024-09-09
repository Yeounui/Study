'''
Created on 2016. 9. 13.

@author: korea
'''
import math

r = float(input())
v = float(input())
u = 398600.4418*10**9 #m**3s**-2

a = (u*r)/(2*u - r*v**2)
t = 2 * math.pi * (a**3/u)**(1/2)

day = t//(24*60*60)
hour = (t - (24*60*60)*day) // (60*60)
minute =(t - day*(24*60*60) - hour*(60 * 60)) // 60

print('major axis: ' + str(a) + ' meters')
print('period: ' + str(t) + ' seconds')
print('period: ' + str(int(day)) + ' days, ' + str(int(hour)) +' hours and ' + str(int(minute)) + ' minutes')