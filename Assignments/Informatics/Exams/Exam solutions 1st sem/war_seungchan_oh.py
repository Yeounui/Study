'''
Created on 2016. 11. 31.

@author: Seungchan Oh
@number: 01603277
'''
def reverseComplement(codes):
    
    """
    >>> reverseComplement('GATATC')
    'GATATC'
    >>> reverseComplement('GCATGC')
    'GCATGC'
    >>> reverseComplement('AGCTTC')
    'GAAGCT'
    """
    # definition
    saved = ''
    # counter-complementary base saving
    for base in codes:
        if base == 'A':
            saved += 'T'
        elif base == 'T':
            saved += 'A'
        elif base == 'C':
            saved += 'G'
        else:
            saved += 'C'
    # need to reverse        
    return saved[::-1]
    
def reversePalindrome(codes):
    
    """
    >>> reversePalindrome('GATATC')
    True
    >>> reversePalindrome('GCATGC')
    True
    >>> reversePalindrome('AGCTTC')
    False
    """
    # whether codes is identical with the result of the function.
    if codes == reverseComplement(codes):
        return True
    else:
        return False
    
def restrictionSites(codes, minLength = 4, maxLength = 12):
    
    """
    >>> restrictionSites('TCAATGCATGCGGGTCTATATGCAT')
    [(4, 'ATGCAT'), (5, 'TGCA'), (6, 'GCATGC'), (7, 'CATG'), (17, 'TATA'), (18, 'ATAT'), (20, 'ATGCAT'), (21, 'TGCA')]
    >>> restrictionSites('AAGTCATAGCTATCGATCAGATCAC', minLength=5)
    [(6, 'ATAGCTAT'), (7, 'TAGCTA'), (12, 'ATCGAT')]
    >>> restrictionSites('ATATTCAGTCATCGATCAGCTAGCA', maxLength=5)
    [(1, 'ATAT'), (12, 'TCGA'), (14, 'GATC'), (18, 'AGCT'), (20, 'CTAG')]
    """
    # definition
    result = list()
    # length definition
    for order in range(len(codes)):
        for length in range(minLength, maxLength+1):
            queue = codes[order:order+length] #target to check
            # for eliminating queue of no use
            if order+length > len(codes):
                break
            # if the part is a spalindromic recognition site, append it to result
            if reversePalindrome(queue):
                result.append((order+1, queue))
    
    return result
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()