# Write a longest common subsequence (LSC) of two DNA strings in FASTA format to the file.
def lcs(input_file, output_file):
    """
    >>> lcs('data01_LCS.fna','output01.fna')
    >>> print(open('output01.fna').read().rstrip())
    >seq01
    AACTTG
    """

    # Read the sequence of two DNA strings from FASTA file
    from Bio import SeqIO
    sequences = SeqIO.parse(input_file, 'fasta')
    seq1 = next(sequences).seq
    seq2 = next(sequences).seq
    len1, len2 = len(seq1), len(seq2)

    # Constructing a Dynamic Programming (DP) table of size [len1 + 1] * [len2 + 1]
    DPTable = [[0] * (len2 + 1) for _ in range((len1 + 1))]
    for r in range(1, len1 + 1):
        for c in range(1, len2 + 1):
            if seq1[r - 1] == seq2[c - 1]:  # Match: Move diagonally towards bottom right
                DPTable[r][c] = max(DPTable[r - 1][c], DPTable[r][c - 1], DPTable[r - 1][c - 1] + 1)
            else:  # Mismatch: Move downwards or towards right
                DPTable[r][c] = max(DPTable[r - 1][c], DPTable[r][c - 1])

    # Reconstructing the LCS from DP Table
    Mylcs = ''
    while (len1 > 0 and len2 > 0):
        if DPTable[len1][len2] == DPTable[len1 - 1][len2]:
            len1 -= 1   # Deletion: Move upwards
        elif DPTable[len1][len2] == DPTable[len1][len2 - 1]:
            len2 -= 1   # Insertion: Move towards left
        else:
            Mylcs += seq1[len1 - 1] # Match: Move diagonally towards top left
            len1 -= 1
            len2 -= 1

    # Write the LCS to a FASTA format file
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord

    lcs_FASTA = SeqRecord(Seq(Mylcs[::-1]), id='seq01', description='')
    SeqIO.write(lcs_FASTA, output_file, 'fasta')


if __name__ == '__main__':
    import doctest
    doctest.testmod()