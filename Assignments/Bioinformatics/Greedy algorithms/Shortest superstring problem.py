# Find the length of the longest prefix of q that matches a suffix of p (= overlap).
def overlap(p, q):
    """
    >>> overlap('AATGGATGGAT', 'GGATTCTTGA')
    4
    """
    overlap_len = 0  # no match found

    # Compare the prefix of q and suffix of p, with length i
    for i in range(1, min(len(p), len(q)) + 1): # Iterate from one to minimal length of one of two
        if p[-(i):] == q[:i]:    # match found # Compare one from the end, other from the head respectively
            overlap_len = i

    return overlap_len    # overlap of p with q


    ########################################################################################################
    # # 2nd method: using Horspool algorithm (less efficient)
    # # compare the patterns only at the position where the first letter of q appears among p

    # # (1) find the position of p where the first letter of q appears
    # position = []
    # for pos, letter in enumerate(p):
    #     if letter == q[0]:
    #         position.append(len(p) - pos)  # distance from the rightmost letter

    # # (2) Compare the prefix of q and suffix of p, with length i
    # overlap_len = 0
    # for i in reversed(position):    # reverse to find the longest length
    #     if p[-(i):] == q[:i]:
    #         overlap_len = i
    # return overlap_len    # overlap of p with q
    ########################################################################################################


# Superstring S contains all given strings as substrings, such that the length of S is as small as possible.
# Find a superstring obtained by the greedy approach.
def greedySSP(string_set):
    """
    >>> greedySSP({'AAT', 'TTAAAA'})
    'TTAAAAT'
    """

    # repeatedly merging a pair of substrings with maximum overlap, until one string remains.
    while len(string_set) > 1:
        # find all possible pair of substrings and their overlap.
        pair_list = []
        pair_list += [[p, q] for p in string_set for q in string_set if p != q] #Iterate all possible cases to compare without same case
        for i, pair in enumerate(pair_list):
            pair_list[i].append(overlap(*pair))  # in nested list: [p, q, overlap]

        # choose the pair with maximum overlap.
        max_pair = 'Z'  # lexicographically largest p (for 1st comparison)
        for pairs in pair_list:
            if pairs[2] == max(pair_list, key=lambda x: x[2])[2]:
                # If two or more pairs have the maximum overlap, choose the pair with the lexicographically smallest p.
                max_pair = pairs if max_pair[0] > pairs[0] else max_pair # A if [condition] else B

        p, q, max_overlap = max_pair
        string_set -= {p, q}                # remove p, q from given set
        overlapped = p + q[max_overlap:]    # merge p with q
        string_set.add(overlapped)          # add merged substring

    return list(string_set)[0]  # obtained superstring

if __name__ == '__main__':
    import doctest
    doctest.testmod()