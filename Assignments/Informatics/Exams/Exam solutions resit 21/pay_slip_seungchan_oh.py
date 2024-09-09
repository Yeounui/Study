'''
Created on 2017. 8. 18.

@author: Seungchan Oh 01603277
'''
#definition
worker = int(input())
prenum = worker
sum = 0
order = 0
task = input()

while task != 'stop': #Until 'stop',
    worker += int(task) # Workers add their salary to the previous whisper.
    sum += worker - prenum # A salary of a worker is the result: recent whisper - previous whisper.
    prenum = worker
    order += 1 #numbering workers
    task = input()
    print('worker #{} whispers ${}'.format(order, worker)) #print lines
average = sum / order # for the average salary
print('average salary: ${:.2f}'.format(average)) # print last line after stop received