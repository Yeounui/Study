'''
Created on 2016. 9. 23.

@author: korea
'''
b=int(input())
p=int(input())
w=int(input())
n=int(input())

initnum=b//p
change=0
left=0
total=initnum

while initnum>=w :
    change = initnum//w*n
    left= initnum%w
    total+=change
    initnum=change+left
    
print(total)