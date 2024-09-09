'''
Created on 2016. 9. 23.

@author: Oh, Seungchan (0160323277)
'''
#definations
m=int(input())
n=int(input())

#initialization
primary_number=2
divisor=2

while primary_number**2 <= n:
    # initialization of the loop
    divisor=2
    primary_number+=1
    
    # if the divisor subtracts the primary number without any remainder, primary number increases.
    # If not, the divisor increases and checks again.
    while divisor != primary_number:
        if primary_number % divisor == 0:
            break
        else:
            divisor+=1
    # the square of the primary number exists only one from n to m.
    #Therefore, if the value are checked by all possible divisors and bigger than m, it is an answer. 
    if primary_number == divisor and m <= primary_number**2:
        break
print('There are {} Martians having {} fingers each.'.format(primary_number, primary_number))