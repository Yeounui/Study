# Find the Hamming distance (= dH, the number of different corresponding symbols) between two strings with equal length.
def hammingDistance(s1, s2):
    """
    >>> hammingDistance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
    7

    >>> from Bio import SeqIO
    >>> hammingDistance(*SeqIO.parse('data.fna', 'fasta'))
    31
    """

    # Input type: (i) string in text file / else, (ii) string
    from Bio import SeqRecord
    if isinstance(s1, SeqRecord.SeqRecord):
        s1 = s1.seq
        s2 = s2.seq

    len1, len2 = len(s1), len(s2)
    assert len1 == len2, 'strings must have equal length'

    dH = 0
    for i in range(len1):
        if s1[i] != s2[i]:  # corresponding symbols are differ
            dH += 1

    return dH

if __name__ == '__main__':
    import doctest

    doctest.testmod()