# find a subsequence of the DNA string that corresponds with the given indices.
def subsequence(dna, indices):
    """
    >>> subsequence('ACGTACGTGACG',(3, 8, 10))
    'GTA'

    >>> from Bio import SeqIO
    >>> subsequence((7, 12, 21, 32),)
    'TGAC'
    """

    # for the given DNA string that formed as a Seq/SeqRecord object
    if not isinstance(dna, str):
        dna = dna.seq

    sub = ''.join([dna[index - 1] for index in indices])    # find nucleotide corresponds with the given index

    for i, index in enumerate(indices):
        assert dna[index - 1] == sub[i], 'invalid indices'    # indices are not matched with subsequence

    return sub


# find one collection of indices of s in which the symbols of t appear as a subsequence of s.
# If multiple indices exist, the function may return any one.
def indices(s, t):
    """
    >>> indices('ACGTACGTGACG', 'GTA')
    (3, 8, 10)

    >>> from Bio import SeqIO
    >>> indices(*SeqIO.parse('data02.fna', 'fasta'))
    (7, 11, 21, 32)
    """

    # for the given DNA string that formed as a Seq/SeqRecord object
    if not isinstance(s, str):
        s = s.seq

    index_list = []
    i = 0
    for nucleotide in t:
        index_list.append(s.find(nucleotide, i) + 1)   # find index of each nucleotide
        i = s.find(nucleotide, i) + 1   # starting point for next search

        ########################################################################################################
        # # 2nd method: use last element of indices list as starting point
        # if len(index_list) == 0:
        #     index_list.append(s.find(nucleotide) + 1)
        # else:
        #     index_list.append(s.find(nucleotide, index_list[-1]) + 1)
        ########################################################################################################

    assert len(index_list) == len(t), 'invalid subsequence'    # no such indices exist

    return tuple(index_list)


if __name__ == '__main__':
    import doctest

    doctest.testmod()