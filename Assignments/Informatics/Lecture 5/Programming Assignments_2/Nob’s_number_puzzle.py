'''
Created on 2016. 10. 3.

@author: Oh, Seungchan (0160323277)
'''
#definations and initializations
firnum = input()
secnum = input()
space=''
trigger = 1


while trigger == 1:
    # a basic format of the value in the loop
    prline = space + firnum.center(4) + secnum.center(4)
    print(prline.rstrip(' ')) #rstrip is for eliminating right certain letters.
    #intialization for first number for calculation
    result=0
    queue=firnum
    #first part of calculation for first number
    while queue != firnum[-1]:
        result += int(queue[0])
        queue = queue[1:]
    result = result + int(queue)
    #intialization for second number for calculation
    queue=secnum
    #second part of calculation for second number
    while queue != secnum[-1]:
        result += int(queue[0])
        queue = queue[1:]
    result = result + int(queue)
    #change of numbers of each line from result and input
    firnum = str(result)
    secnum = input()
    #initialization of result
    result = 0
    #give some space to each line
    space += '  '
    # an expression of the last line
    if secnum == '-1':
        trigger = 0
        print(space + firnum.center(4).rstrip(' '))
        
        #the last line doesn't come out in eclipse.