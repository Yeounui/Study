'''
Created on 2016. 10. 3.

@author: Oh, Seungchan (0160323277)
'''
#definition and initialization of variables
startpoint=int(input())
step=int(input())
length=int(input())
verse=  ''
line = ' '
word = ''

# a process to make a line of organized string
while line != '':
    line = input()
    verse += line
subject=verse.replace(' ','').replace(',','').replace('.','').replace('!','').replace('?','').replace(';','').replace(':','').replace('-','')

#initial location of hide letter
sequence=startpoint-1

# a process to find hide letter
for letter in range(0, length):
    word+=subject[sequence]
    sequence += step
    # if the sequence go over length of the organized string, adds some question marks.
    if sequence >= len(subject) or sequence < -1:
        word += (length-1-letter)*'?'
        break

print(word)