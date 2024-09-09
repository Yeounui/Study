'''
Created on 2016. 9. 22.

@author: korea
'''
#print() statement: visualize
from lib2to3.fixer_util import String
bruce = 5
print(bruce, end=' ') #end makes results print on the same line.
bruce = 7
print(bruce)

#assignment operator(=)
#expression on the right-hand side is evaluated first
#the result is then assigned to name on left-hand side.
#new value of the variable may depend on the old value.

x = 0
x = x + 1
print(x)
# Only 'y = y + 1' couldn't be, because y isn't defined.

#repetitive statement(loop)
# while- if it is true, some statements are executed, if not, these statements are passed.
n=10
while n > 0: #evaluates by boolean expression-true or flase
    print(n)
    n= n-1
print('Blastoff!')

counter= 0
while True: #this is always true
    counter = counter+1 # is equal to 'counter += 1'
    # print(counter) # this will print counter until out of memory. use terminate current console button in Eclipse which is red.
    
n = int(input('Enter a number: '))
m = n # remember value of n
count = 0 # initialize counter
while m:
    count = count + 1
    m = m // 10
print(n,' has' , count, 'digits.')

n = int(input('Enter a number: '))
m = n # remember value of n
count = 0 # initialize counter
while m :
    digit = m % 10 # lookup last digit
    if digit % 2:
        count = count + 1
    m = m // 10 # remove last digit
print (n, 'has', count, 'odd digits.')

# +=, -=, *=, /=, //= and %=

#print table of powers
print(1, end=' ')
print(1 ** 2, end=' ')
print(1 ** 3)
print(1, 1 ** 2, 1 ** 3)

print(1, end='/t')
print(1 ** 2, end='/t')
print(1 ** 3)
print(1, '/t', 1**2, '/t', 1**3)
print(1, 1 ** 2, 1 ** 3, sep='/t')

n = 1
while n<= 10: #you can convert 10 to 1000
    print(1, 1 ** 2, 1 ** 3, sep='/t')
    n += 1

# 10*10 multiplication table
n = 1
while n<= 10 :
    m = 1
    while m <= 10:
        print(n*m, end='/t')
        m += 1
    print()
    n += 1

s= 's'+'p'+'a'+'m' #string
l= [2, 4, 6, 8, 10] # list
t= ('b', 'a', 'n', 'a') #tuple
v= {'b', 'a', 'n', 'a'} #set
v 

# iterator-transform
word = 'spam'
iterator = iter(word)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
#more of this comes out an Error

word = 'spam'
for letter in word:
    print(letter)
    
list(range(10))
list(range(3, 10))
list(range(3, 10, 2)) # 3rd value is for plus the value to prior number
list(range(10, 0, -1))

for n in range(1, 11) :
    for m in range(1, 4):
        print(n**m, end='/t')
    print()
    
import random
number = random.randint(1,10)

mySum = 0
for i in range(1, n+1):
    mySum += i**2
#sigma i**2 expression

#Fn = Fn-1 + Fn-1
f0, f1 = 0, 1
for i in range(n-1):
    f0, f1 = f1, f0 +f1
    
