'''
Created on 2016. 9. 13.

@author: korea
'''

i=1
sum=0

while i<10:
    sum+=i*int(input())
    i+=1

print(sum%10)