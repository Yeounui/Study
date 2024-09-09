'''
Created on 2017. 3. 6.

@author: Seungchan Oh
@student_number: 01603277
'''
def width(givenlist):
    # Definition
    givenlist = list(givenlist)
    largestpoint = givenlist[0][0]
    largestorder = 0
    # compare which one is bigger
    for order in range(len(givenlist)):
        candidated = givenlist[order][0]
        if largestpoint < candidated:
            largestpoint = candidated
            largestorder = order
    # the biggest number of location 0 in partial list determines length of sentence
    length = largestpoint + givenlist[largestorder][1]
    return length
    
def line(tuplegroup, length = None):
    # Definition
    transformed = str()
    tuplegroup = list(tuplegroup)
    candidated = [tuplegroup[0]]
    # Compare number in sequence with numbers in organizing list. 
    for tuple2 in tuplegroup[1:]:
        for tuple1 in candidated:
            if tuple1 < tuple2:
                candidated.insert(candidated.index(tuple1), tuple2)
                break
    # add number to last location in list unless command insert works. 
        if tuple2 not in candidated:
            candidated.append(tuple2)
    # reversed list is more prone to find order of numbers.
    tuplegroup = candidated[::-1]
    
    for parttuple in tuplegroup:
    # Definition
        startpoint = parttuple[0]
        markpoints = parttuple[1]
        lastletter = len(transformed)
    #append spaces until the mark starts
        while len(transformed) != int(startpoint):
            transformed += ' '
    #append sharps to interval between startpoint and markpoint
        while len(transformed) !=  startpoint + markpoints:
            transformed += '#'
    # fill until defined end of string
    if length is not None:
        while len(transformed) != length:
            transformed += ' '
    return transformed
    
def nonogram(given, made):
    # opening text and definition
    opentxt = open(given, 'r')
    readtxt = opentxt.readline()
    saveonpy = list()
    picture = ''
    from ast import literal_eval
    # convert string to format list and append to savelist 
    while readtxt:
        readtxt = readtxt.replace(';', ',')
        readtxt = literal_eval(readtxt)
        if type(readtxt[0]) == int:
            readtxt = tuple([readtxt])
        saveonpy.append(readtxt)
        readtxt = opentxt.readline()
    opentxt.close()
    # Define largest string to fill space
    largestlength = width(saveonpy[0])
    # Define length of line
    for line1 in saveonpy[1:]:
        target = width(line1)
        if target > largestlength:
            largestlength = target
    # forming each line
    for line2 in saveonpy:
        picture += (line(list(line2), largestlength) + '\n')
    picture = picture.rstrip('\n')
    # putting in text
    opentxt = open(made, 'w')
    writetxt = opentxt.write(picture)
    opentxt.close()

nonogram('stupid.puzzle.txt', 'stupid.solution.txt')