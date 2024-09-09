import doctest
from Bio.Seq import Seq


#### 1

def pattern_count(sequence, pattern):
    #Pattern matching; return occurrences. Brute force Algorithm
    """
    >>> pattern_count('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT')
    3
    >>> pattern_count('CGATATATCCATAG ', 'ATA')
    3

    >>> from Bio import SeqIO
    >>> pattern_count(*SeqIO.parse('data1.fna', 'fasta'))
    294
    """
    count = 0

    # Compatible to SeqRecord
    try:
        sequence = sequence.seq
    except:
        pass

    try:
        pattern = pattern.seq
    except:
        pass

    sequence = str(sequence)
    pattern = str(pattern)

    # Size definition
    sequence_length = len(sequence)
    pattern_length = len(pattern)
    loci_num = sequence_length - pattern_length

    # Following Pseudocode
    for i in range(loci_num + 1):
        potent_kmer = sequence[i: i + pattern_length]
        if potent_kmer == pattern:
            count += 1

    return count


####2

def most_frequent_kmers(sequence, k):
    #Return most frequent pattern in length of k
    """
    >>> most_frequent_kmers('ACAACTATGCATCACTATCGGGAACTATCCT', 5)
    {'ACTAT'}
    >>> most_frequent_kmers('CGATATATCCATAG', 3)
    {'ATA'}

    >>> from Bio import SeqIO
    >>> most_frequent_kmers(*SeqIO.parse('data2.fna', 'fasta'), 4)
    {'CATG', 'GCAT'}
    """

    # Compatible to SeqRecord
    try:
        sequence = sequence.seq
    except:
        pass

    sequence = str(sequence)

    # Size definition
    sequence_length = len(sequence)
    locus_num = sequence_length - k

    # Gather all possible kmers
    potent_kmer_set = set()

    for i in range(locus_num + 1):
        potent_kmer = sequence[i: i + k]
        potent_kmer_set.add(potent_kmer)

    # Comparison between potent most frequent kmers
    most_frequent_set = set()
    max_frequent_num = None

    for j in potent_kmer_set:
        if max_frequent_num is not None:
            potent_frequent_num = pattern_count(sequence, j)

            if potent_frequent_num > max_frequent_num:
                max_frequent_num = potent_frequent_num
                most_frequent_set.clear()
                most_frequent_set.add(j)

            elif potent_frequent_num == max_frequent_num:
                most_frequent_set.add(j)

        else:
            max_frequent_num = pattern_count(sequence, j)
            most_frequent_set.add(j)

    return most_frequent_set


####3

def pattern_occurrences(kmer, sequence):
    # Find indexes of occurrence of kmer in sequence
    """
    >>> pattern_occurrences('ATA', 'CGATATATCCATAG')
    (2, 4, 10)
    >>> pattern_occurrences('ATAT', 'GATATATGCATATACTT')
    (1, 3, 9)

    >>> from Bio import SeqIO
    >>> pattern_occurrences(*SeqIO.parse('data3.fna', 'fasta'))
    (0, 46, 51, 74)
    """
    # Compatible to SeqRecord
    try:
        kmer = kmer.seq
    except:
        pass

    try:
        sequence = sequence.seq
    except:
        pass

    kmer = str(kmer)
    sequence = str(sequence)

    # Size definition
    sequence_length = len(sequence)
    kmer_length = len(kmer)
    locus_num = sequence_length - kmer_length

    loci_list = list()

    # match detection
    for i in range(locus_num + 1):
        potent_kmer = sequence[i: i + kmer_length]
        if potent_kmer == kmer:
            loci_list.append(i)

    return tuple(loci_list)


####3

def minimum_skew(sequence):
    #
    """
    >>> minimum_skew('CATGGGCATCGGCCATACGCC')
    (21,)

    >>> from Bio import SeqIO
    >>> minimum_skew(*SeqIO.parse('data4.fna', 'fasta'))
    (53, 97)
    """

    # Compatible to SeqRecord
    try:
        sequence = sequence.seq
    except:
        pass

    sequence = str(sequence)

    min_skew_list = [0]
    min_skew_value = 0
    skew_value = 0
    for locus, i in enumerate(list(sequence)):
        # Measure current skew value
        if i == 'C':
            skew_value -= 1
        elif i == 'G':
            skew_value += 1

        # Measure min skew value in process
        if min_skew_value > skew_value:
            min_skew_value = skew_value
            min_skew_list = [locus + 1]

        elif min_skew_value == skew_value:
            min_skew_list.append(locus + 1)

    return tuple(min_skew_list)


####3

def clump_finding(sequence, k, length, time):
    """
    >>> clump_finding('CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC', 5, 75, 4)
    {'GAAGA', 'CGACA', 'AATGT'}
    >>> clump_finding('AAAACGTCGAAAAA', 2, 4, 2)
    {'AA'}
    >>> clump_finding('ACGTACGT', 1, 5, 2)
    {'G', 'T', 'C', 'A'}

    >>> from Bio import SeqIO
    >>> clump_finding(*SeqIO.parse('data4.fna', 'fasta'), 11, 566, 18)
    {'AAACCAGGTGG'}
    """
    # Compatible to SeqRecord
    try:
        sequence = sequence.seq
    except:
        pass

    # gather all possible clumps into a set
    possible_clump_set = set()
    for i in range(len(sequence) - k):
        possible_clump_set.add(sequence[i: i + k])

    # Check a possible clump whether the seq patterns appear specific times in certain length of interval.
    clump_set = set()
    for i in possible_clump_set:
        kmer_loci_list = list(pattern_occurrences(i, sequence))
        for j in range(len(kmer_loci_list) - time + 1):
            if kmer_loci_list[j + time - 1] - kmer_loci_list[j] <= length - k:
                clump_set.add(str(i))
                break

    return clump_set
