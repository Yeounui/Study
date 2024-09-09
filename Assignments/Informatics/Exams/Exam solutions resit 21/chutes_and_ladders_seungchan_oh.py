'''
Created on 2017. 8. 18.

@author: Seungchan Oh 01603277
'''
def merge(chutedict, ladderdict):
    
    """
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> merge(chutes, ladders)
    {64: -4, 1: 37, 4: 10, 71: 20, 9: 22, 16: -10, 21: 21, 87: -63, 28: 56, 93: -20, 95: -20, 80: 20, 98: -20, 36: 8, 47: -21, 49: -38, 51: 16, 56: -3, 62: -43}
    >>> chutes
    {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders
    {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> merge({23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    """
    assert [x for x in ladderdict.keys() if x in chutedict.keys()] == list(), 'invalid configuration' #check whether starting point of ladder and chute is same.
    #definition
    mergedict = dict()
    premergedict = dict(chutedict)
    premergedict.update(ladderdict) # for editing a dictionary at one time
    for start in premergedict.keys():
        inputvalue = premergedict[start]-start
        if start in chutedict.keys(): # check whether ladder has positive values or not, and whether chute has negative values or not.
            assert inputvalue < 0, 'invalid configuration' # if ladder got a positive, it is an error.
        elif start in ladderdict.keys():
            assert inputvalue > 0, 'invalid configuration' # if chute got a negative, it is an error.
        mergedict[start] = inputvalue # add a fine value to result dictionary.
    return mergedict

def spaces(diegroup, chutedict, ladderdict):
    
    """
    >>> chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> spaces([1, 4, 5], chutes, ladders)
    [38, 42, 26]
    >>> spaces([2, 4, 1, 4, 5, 5, 4, 2], chutes, ladders)
    [2, 6, 7, 11, 6, 11, 15, 17]
    >>> spaces([5] * 16, chutes, ladders)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 100]
    >>> spaces([6] * 14, chutes, ladders)
    [6, 12, 18, 24, 30, 44, 50, 53, 59, 65, 91, 97, 97, 97]
    >>> spaces([4, 2, 5, 6], {23: 32}, {44: 44})
    Traceback (most recent call last):
    AssertionError: invalid configuration
    """
    #definition
    mergedict = merge(chutedict, ladderdict)
    location = 0
    resultlist = list()
    for result in diegroup: # Until sum of dying result overcomes 100, keeps moving according to mergedict.
        if location + result <= 100:
            location += result
        if location in mergedict.keys(): # when a ladder or a chute is involved.
            if location + mergedict[location] <= 100:
                location += mergedict[location]
        resultlist.append(location)
    return resultlist

if __name__ == '__main__':
    import doctest
    doctest.testmod()