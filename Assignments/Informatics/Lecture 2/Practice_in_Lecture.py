'''
Created on 2016. 9. 8.

@author: korea
'''
from pip._vendor.pyparsing import StringStart

print(4)
type('Hello, World!') # strings
type('17') # It looks a integer, but it actually is a string
type(17) # integers
type(32) # floats
print("Bruce's beard")
print('Bruce')
print(1,000,000)
print(1000000)
welcome = 'Hello, World!'
print(welcome)
message = "What's up, Doc?"
n = 17
pi = 3.14159 # == is for equality test, please name meaningful for not to be confused

import math
y=2
z=7
x= math.sqrt(y**2 + z**2) #we should type 'import math' first to use math.sqrt

a = 3 # a becomes 3
a = 'spam' #changes into spam
a = 1.23 #and changes into 1.23
b = 4
print(id(a), id(b))
b = a #Try to change into a = b
print(id(a), id(b))

#avoid using names with only uppercase letters
print(1)
x = 2
print (x)

print(83 / 10)
print(83 // 10)
print(83 % 10)
print(int('32'))
print(int(-2.3))
print(float(32))
print(str(32)) # change numbers into strings

fruit ='banana'
baked_good = ' nut bread'
print(fruit + baked_good)

n = input('Please, enter your name: ')
print(n)

