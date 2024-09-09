'''
Created on 2016. 11. 12.

@author: Seungchan Oh
@student_number: 01603277
'''
def board(prices, screens = 1):
    # Error decision
    assert len(prices) % screens == 0, 'invalid board'
    # Definition
    result = list()
    prices = list(prices)
    # grouping by separating prices
    for queue in range(len(prices)//screens):
       separated = prices[:screens]
       prices = prices[screens:]
       result.append(separated)
    return result

def price(pattern, steps, prices, screens = 1, start = 0):
    #definition
    decided = board(prices, screens)
    trigger1 = 0
    trigger2 = 0
    # fitting start value into proper value
    if start >= len(decided):
        start = start % len(decided)
    #definition for startpoint
    startpoint= decided[start][trigger2]
    # stepping the board
    for sequence in range(steps):
        start += pattern[trigger1]
        trigger1 += 1
        trigger2 += 1
        # initialization according to boardmarks
        if trigger1 == len(pattern):
            trigger1 = 0
        if trigger2 == screens:
            trigger2 = 0
        if start >= len(decided):
            start = start % len(decided)
        # change of current point
        startpoint = decided[start][trigger2]
    return startpoint