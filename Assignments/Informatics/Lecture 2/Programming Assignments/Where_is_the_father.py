'''
Created on 2016. 9. 10.

@author: korea
'''
a = int(input()) #years
b = int(input()) #years
c = int(input()) #times

A = a * 12 #months
B = b * 12 #months

SA = (A + B- B*c) / (c - 1) #months
MA = SA + A #months 

print('The mother is ' + str(int(MA)) + ' months old and her son ' + str(int(SA)) + ' months.')