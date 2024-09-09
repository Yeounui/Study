# Seungchan Oh Bokyung Jin

givenset = {'GTATTG', 'GATT', 'AATTGC', 'ATTGAT', 'TGCGT', 'TTGA'}
shortest_superstring = 'AATTGCGTATTGATT'

def greedy_shortest_superstring(givenset):
    # definition
    givenlist = list(givenset)
    string = givenlist.pop(0) # saving superstring in it

    while len(givenlist) > 0:

        maximum_overlap = -1
        # Analyze all the string, and then, among them, choose a string which has maximal overlap.
        print(givenlist)
        for sequence in givenlist:

            #deciding what is shorter and longer.
            if len(string) >= len(sequence):
                strand_A = string
                strand_B = sequence
            else:
                strand_A = sequence
                strand_B = string

            index = 0

            while index < len(strand_A) + len(strand_B)-1:
                # No.1 When a short string is overlapped on the head of long string
                if index < len(strand_B)-1:
                    if strand_A[:index+1] == strand_B[-1-index:]: # And then, we compare overall overlap
                        overlap = len(strand_B[-1-index:])
                        if maximum_overlap < overlap: # if overlap is bigger than maximum_overlap, it becomes maximum overlap.
                            maximum_overlap = overlap
                            sequence_saving = sequence # saving for removing element in list
                            prestring = strand_B[:-1-index] + strand_A # saving for string; a string which has maximum overlap has the fittest sequence.

                # No.2 When a short string is a part of long string
                elif index < len(strand_A):
                    if strand_A[index-len(strand_B)+1:index+1] == strand_B: # And then, we compare overall overlap
                        overlap = len(strand_B)
                        if maximum_overlap < overlap:
                            maximum_overlap = overlap
                            sequence_saving = sequence
                            prestring = strand_A

                # No.3. When a short string is overlapped on the tail of long string
                else:
                    if len(strand_B[:index - len(strand_A)]) > maximum_overlap:
                        if strand_A[-(len(strand_A) - index):] == strand_B[:index - len(strand_A)]: # And then, we compare overall overlap
                            overlap = len(strand_B[:index-len(strand_A)])
                            if maximum_overlap < overlap:
                                maximum_overlap = overlap
                                sequence_saving = sequence
                                prestring = strand_A + strand_B[index-len(strand_A):]

                # index increase
                index += 1
                print(index, sequence)

        # remove the fittest sequence from list
        print(strand_A, sequence_saving, maximum_overlap, prestring)
        print(givenlist)
        givenlist.remove(sequence_saving)

        # intermediate to original
        string = prestring

    string += 'T'
    return string

print(greedy_shortest_superstring(givenset))