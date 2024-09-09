# find the Profile-most probable k-mer in given DNA string
def profilemost_probable_kmer(DNA_file, p_file):
    """
    >>> profilemost_probable_kmer('data11.fna', 'data01.prof')
    'CCGAG'
    >>> profilemost_probable_kmer('data02.fna', 'data02.prof')
    'AGCAGCTT'
    >>> profilemost_probable_kmer('data03.fna', 'data03.prof')
    'AAGCAGAGTTTA'
    """

    # calculate the probability of k-mer being a motif according to Profile
    def Probability(p_matrix, kmer):
        prob = 1
        for i in range(k):
            prob *= float(p_matrix[kmer[i]][i])

        return prob

    from Bio import SeqIO
    DNA = str(SeqIO.read(DNA_file, 'fasta').seq)

    p_matrix = {}
    with open(p_file) as txt:
        for nucleotide, line in zip('ACGT', txt):
            p_matrix[nucleotide] = line.rstrip().split(' ')

    k = len(p_matrix['A'])    # length of k-mer
    maxpos = len(DNA) - k + 1  # maximum value starting position

    # find the k-mer with the highest probability
    PMP_kmer = max([DNA[j:j + k] for j in range(maxpos)], key=lambda x: Probability(p_matrix, x))

    return PMP_kmer

if __name__ == '__main__':
    import doctest
    doctest.testmod()