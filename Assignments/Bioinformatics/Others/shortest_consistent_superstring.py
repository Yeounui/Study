positive_sequences = {'GTATTG', 'GATT', 'AATTGC', 'ATTGAT', 'TGCGT', 'TTGA'}
negative_sequences = {'TTAA', 'AAC', 'CGCATA', 'ATAAC', 'ACTAA'}

def shortest_consistent_superstring(positive_seq_set, negative_seq_set):
    positive_seq_list = list(positive_seq_set)
    negative_seq_list = list(negative_seq_set)
    string = positive_seq_list.pop(0)
    prestring = str()

    complementary_seq_list = list()
    for negative_seq in negative_seq_list:
        complementary_seq = str()
        for base in negative_seq:
            if base == 'A':
                complementary_seq += 'T'
            elif base == 'T':
                complementary_seq += 'A'
            elif base == 'C':
                complementary_seq += 'G'
            else:
                complementary_seq += 'C'
        complementary_seq_list.append(complementary_seq)

    print(positive_seq_list)
    print(complementary_seq_list)
    print(string)

    list_using = complementary_seq_list
    while len(positive_seq_list) > 0 and len(complementary_seq_list) > 0:

        maximum_overlap = -1
        for sequence in list_using:
            print(sequence, 'sequence')

            if len(string) >= len(sequence):
                strand_A = string
                strand_B = sequence
            else:
                strand_A = sequence
                strand_B = string

            index = 0
            while index < len(strand_A) + len(strand_B)-1:
                if index < len(strand_B)-1:
                    if strand_A[0] == strand_B[-1-index]:
                        if strand_A[:index+1] == strand_B[-1-index:]:
                            overlap = len(strand_B[-1-index:])
                            print('success!', strand_A, strand_B, index, overlap)
                            if maximum_overlap < overlap:
                                maximum_overlap = overlap
                                sequence_saving = sequence
                                prestring = strand_B[:-1-index] + strand_A

                elif index < len(strand_A):
                    if strand_B[0] == strand_A[index-len(strand_B)+1]:
                        if strand_A[index-len(strand_B)+1:index+1] == strand_B:
                            overlap = len(strand_B)
                            print('success!!', strand_A, strand_B, index, overlap)
                            if maximum_overlap < overlap:
                                maximum_overlap = overlap
                                sequence_saving = sequence
                                prestring = strand_A

                else:
                    if len(strand_B[:index - len(strand_A)]) > maximum_overlap:
                        if strand_A[len(strand_A) - index] == strand_B[0]:
                            if strand_A[len(strand_A) - index:] == strand_B[:index - len(strand_A)]:
                                overlap = len(strand_B[:index-len(strand_A)])
                                print('success!!!', strand_A, strand_B, index, overlap)
                                if maximum_overlap < overlap:
                                    maximum_overlap = overlap
                                    sequence_saving = sequence
                                    prestring = strand_A + strand_B[index-len(strand_A):]

                index += 1

        if list_using == positive_seq_list:
            list_using = complementary_seq_list
            positive_seq_list.remove(sequence_saving)
        else:
            list_using = positive_seq_list
            complementary_seq_list.remove(sequence_saving)
        print(positive_seq_list)
        print(complementary_seq_list)

        string = prestring
        print(string, 'string')

    return string


#superstring is AATTGCGTATTGATT
print(shortest_consistent_superstring(positive_sequences, negative_sequences))