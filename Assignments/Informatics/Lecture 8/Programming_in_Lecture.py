'''
Created on 2016. 10. 27.

@author: korea
'''
def keeper(name, quest='Holy Grail', color='Blue'):
    print('My name is {}'.format(name))
    print('To seek the {}.'.format(quest))
    print('{}.'.format(color))

keeper('A')
keeper('A', 'B')
keeper('A', 'B', 'C')
#default parameter value

keeper('Sir Galahad', color = 'Blue. No yellow')
#change default value

def perimeter(radius):
    from math import pi
    return 2* pi* radius

#main program
radius = 2.87
print(perimeter(radius))

def perimeter(radius):
    return 2 * 3.14 * radius
def parimeter(radius):
    from math import pi
    return 2 * pi * radius

print(perimeter(2.87))
contour = perimeter
print(contour(2.87))

from math import pi
def area(radius):
    return pi * radius ** 2
def compute(function, value):
    return function(value)

print(compute(perimeter, 2.87))
functions = [perimeter, area]
for function in functions:
    print(function(2.87))
    
def perimeter(radius):
    """ Calculates perimeter of circle with given radius."""
    return 2 * radius * pi

dir(perimeter)

print(perimeter.__name__)  
print(perimeter.__doc__) #docstring

perimeter(radius)

"""Working with circles."""
from math import pi
def perimeter(radius):
    """Perimeter of a circle."""
    return 2 * pi * radius
def area(radius):
    """Area of a circle"""
    return pi * radius ** 2
radius = 2.87
import circle
type(circle)
dir(circle)
circle.perimeter(radius)
circle.area(radius)

import circle
circle.__name__
circle.__doc__
help(circle)

import circle
radius = input('radius: ')
ftest = radius
if '.' in radius: #float given?
    ftest = radius.replace('.', '', 1)
if ftest.isdigit():
    radius = float(radius)
    print(circle.perimeter(radius))
    print(circle.area(radius))
    
question = 'ABC'
answer = 'CBA'
import module1
question
module.question