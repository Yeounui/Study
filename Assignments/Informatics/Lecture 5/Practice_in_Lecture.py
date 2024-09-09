'''
Created on 2016. 9. 29.

@author: korea
'''
element='helium' #string is made of characters.
element.upper() #HELIUM

letter = element[1]
print(letter) #e / 2=l
print(type(letter)) #<class 'str'>

element = 'helium'
element[1] #e
element[0] #h computer starts from 0
element[2 + 3] #m

element = 'helium'
len(element) #6

length = len(element)
# last = element[length] #it causes problem, because length is 6 so it doesn't have any character.
print(element[length-1]) #m 6-1
element[-1] #m muileh
ord('A') # 65 / in ASCII code A is 1000001(2)
chr(65) # A
bin(65) #0bl000001 #0b means it's a binary number
oct(65) #0o101(65) #8
hex(65) #0x41 #6

counter = 0
ascii_code_for_a = ord('a')
while counter < 26: #for counter in range(26)
    print(chr(ascii_code_for_a + counter))
    counter += 1

element = 'helium'
pos = 0
while pos < len(element) :
    letter = element[pos]
    print(pos, letter)
    pos += 1
    
for pos in range(len(element)):
    print(pos, element[pos])
    
for letter in element:
    print(letter)
    
for pos, letter in enumerate(element):
    print(pos, letter)
    
prefix, suffix = 'lo', 'er'
letters = 'nsvw'
for infix in letters:
    print(prefix + infix + suffix)
    
#slice
element='helium'
element[0:3] #'hel'
element[1:5] #'eliu'
element[-3:6] #'ium'
element[:3] #'hel'
element[-3:] #'ium'
element2 = element[:]
element2 #'helium'

'nonflagellated'[4:14:3] #'lead'=nonf'l'ag'e'll'a'te'd'
'deoxyribonucleoprotein'[9::4]#'neon'
'imprisioning'[::3] #iron
'theoriodont'[::4] #tin

'a' == 'a' #t
'a' <= 'b' #t
'cesium'>= 'cerium' #t
'1' <= '9' #t
'appleberry' > 'apple' #t

'a' < 'Z' #f / Capital letter matters.
9 < 10 #t
'9' < '10' #f
'gold' < 'Silver' #f
'gold'.lower() < 'Silver'.lower() #t

#in
'p' in 'apple' #t
'i' in 'apple' #f
'ap' in 'apple' #t
'pa' in 'apple' #f

word = input() #'i','i**2','i**3','i**5','i**10','i**20', PYTHON WITHOUT VOWELS
vowels = 'aeiou'
word_without_vowels = ''
for letter in word:
    if letter.lower() not in vowels:
        word_without_vowels += letter
        print(word_without_vowels)


name = 'dawin'
#name[0] ='D'
name = 'D' + name[1:]
name #'Darwin'

#object.method() is a basic format of String.
element = 'chlorine'
element.upper() #'CHLORINE'
element.capitalize() #'Chlorine'
element.replace('c', 'C') #'Chlorine'

element = 'helium'
element.upper() #'HELIUM'
element.replace('el','afn') #'hafnium'

print('***' + element.upper().center(10) + '***') # center gives some space

#dir(element) #help(element) # help(str.find)

i = 1
print('{:<4s}{:<5s}{:<6s}{:<8s}{:<13s}{:<15s}'.format('i','i**2','i**3','i**5','i**10','i**20'))
while i <= 10 :
    print('{:<4d}{:<5d}{:<6d}{:<8d}{:<13d}{:<15d}'.format(i,i**2,i**3,i**5,i**10,i**20))
    i+=1