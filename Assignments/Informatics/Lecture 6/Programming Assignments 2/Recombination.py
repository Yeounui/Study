'''
Created on 2016. 10. 11.

@author: Seungchan Oh
@student_number: 01603277
'''
def recombination(word1, word2, result1):
    # Error decision
    assert len(word1) == len(word2) == len(result1) , 'words must have equal length'
    # definition
    prechange = list()
    result2 = ''
    # saving order
    for digit in range(len(word1)):
        # Error decision
        assert result1[digit] == word1[digit] or result1[digit] == word2[digit], 'invalid recombination'
        # saving the digit value
        if result1[digit] == word1[digit]:
            prechange.append(digit)
    # filling out letters
    for digit in range(len(word1)):
        if not digit in prechange:
            result2 += word1[digit]
        else:
            result2 += word2[digit]
    return result2

def chimeras(word1, word2, mark):
    #Error decision
    assert len(word1) == len(word2), 'words must have equal length'
    #definition
    save = list()
    initnum = ''
    terminum = ''
    trigger = 0
    result1 = word1
    result2 = word2
    termlist = list()
    initlist = list()
    # figure out cutting point
    for queue in mark:
        # separating number from mark
        if queue.isalnum():
            if trigger == 0:
                initnum += queue
            else:
                terminum += queue
            # putting to lists meaning startpoint and endpoint
            if queue == mark[-1]:
                if trigger == 0:
                    initlist.append(int(initnum)) # when changing digits are not aline
                    termlist.append(None)
                else:
                    initlist.append(int(initnum)) # when changing digits are aline
                    termlist.append(int(terminum))
        # expressing changing digits are aline.
        elif queue == '-':
            trigger = 1
        else:
            # endpoint by ';'
            if trigger == 0:
                initlist.append(int(initnum))
                termlist.append(None)
            else:
                initlist.append(int(initnum))
                termlist.append(int(terminum))
                trigger = 0
                terminum = ''
            initnum = ''
    # constructing results
    for sequence in range(len(initlist)):
        initnum = initlist[sequence]
        terminum = termlist[sequence]
        # sequence which appends letter from initlist and termlist
        if terminum == None:
            result1 = result1[:int(initnum)-1] + word2[int(initnum)-1] + result1[int(initnum):]
            result2 = result2[:int(initnum)-1] + word1[int(initnum)-1] + result2[int(initnum):]
        else:
            result1 = result1[:int(initnum)-1] + word2[int(initnum)-1:int(terminum)] + result1[int(terminum):]
            result2 = result2[:int(initnum)-1] + word1[int(initnum)-1:int(terminum)] + result2[int(terminum):]
    return (result1, result2)

print(recombination('oleins', 'arcade', 'oreads'))
print(chimeras('burgul', 'aeneas', '2-3;5'))