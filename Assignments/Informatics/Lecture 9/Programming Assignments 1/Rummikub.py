'''
Created on 2016. 11. 14.

@author: korea
'''
def group(given):
    setgiven = set(given)
    dictgiven = {}
    for queue in setgiven:
        dictgiven[queue] = given.count(queue)
    return dictgiven

def play(meld, rack):
    result = None
    for queue in meld:
        if queue in rack:
            if meld[queue] > rack[queue]:
                result = False
        else:
            result = False
    if result == None:
        result = True
        for queue in meld:
            if meld[queue] == rack[queue]:
                del rack[queue]
            else:
                rack[queue] = rack[queue] - meld[queue]
    return result
        
print(group(['9Y', '7R', '9Y', '7R', '9Y', '7R', '9Y']))

meld = group(['13B', '13Z', '13Y'])
rack = group(['1Y', '7Y', '8Y', '12Y', '12B', '13B', '13B', '13Z', '13Y', '2Z', '3Z', '4Z', '11Z', '11Z', '4R', '5R'])
print(play(meld, rack))
