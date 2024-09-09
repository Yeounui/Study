def profit(rate, actions):
    """
    >>> profit([5, 11, 4, 2, 8, 10, 7, 4, 3, 6], 'BS-B-S--BS')
    17
    >>> profit((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11), '-B-S-BS-BSBS')
    31
    >>> profit([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10], '-B-S--B-SB--S')
    16
    >>> profit((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10), '-BSB----SBS')
    14
    >>> profit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], '----------')
    0
    >>> profit((10, 4, 2, 4, 8, 12), 'B---SS')
    Traceback (most recent call last):
    AssertionError: invalid actions
    """
    assert isinstance(actions, str) and\
           (len(actions) == len(rate)), 'invalid actions'

    sum = 0
    coin = False
    for day, behavior in enumerate(actions):
        if behavior == 'B':
            assert coin is False, 'invalid actions'
            sum -= rate[day]
            coin = True
        elif behavior == 'S':
            assert coin is True, 'invalid actions'
            sum += rate[day]
            coin = False
        else:
            assert behavior == '-', 'invalid actions'
        assert not (day == len(actions) - 1 and coin is True), 'invalid actions'
    return sum

def optimal_actions(rate):
    """
    >>> optimal_actions([5, 11, 4, 2, 8, 10, 7, 4, 3, 6])
    'BS-B-S--BS'
    >>> optimal_actions((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11))
    '-B-S-BS-BSBS'
    >>> optimal_actions([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10])
    '--B-S-B-SB--S'
    >>> optimal_actions((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10))
    '-BSB----SBS'
    >>> optimal_actions([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    '----------'
    >>> optimal_actions((10, 4, 2, 4, 8, 12))
    '--B--S'
    """
    day = 0
    actions = ''
    buyDayList, sellDayList = [], []
    lowestDay, highestDay = -1, -1
    while day < len(rate):
        if lowestDay != -1 and rate[lowestDay] < rate[day]:
            if highestDay == -1 or rate[day] >= rate[highestDay]:
                highestDay = day
                if day == len(rate) -1:
                    buyDayList.append(lowestDay)
                    sellDayList.append(highestDay)
            else:
                buyDayList.append(lowestDay)
                sellDayList.append(highestDay)
                lowestDay = day
                highestDay = -1
        else:
            if highestDay == -1:
                lowestDay = day
            else:
                buyDayList.append(lowestDay)
                sellDayList.append(highestDay)
                lowestDay = day
                highestDay = -1

        day += 1

    for day in range(len(rate)):
        if day in buyDayList:
            actions += 'B'
        elif day in sellDayList:
            actions += 'S'
        else:
            actions += '-'

    return actions

def maximal_profit(rate):
    """
    >>> maximal_profit([5, 11, 4, 2, 8, 10, 7, 4, 3, 6])
    17
    >>> maximal_profit((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11))
    31
    >>> maximal_profit([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10])
    16
    >>> maximal_profit((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10))
    14
    >>> maximal_profit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    0
    >>> maximal_profit((10, 4, 2, 4, 8, 12))
    10
    """
    actions = optimal_actions(rate)
    return profit(rate, actions)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


