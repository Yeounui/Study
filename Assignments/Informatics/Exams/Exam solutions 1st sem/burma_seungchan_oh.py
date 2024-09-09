'''
Created on 2016. 11. 31.

@author: Seungchan Oh
@number: 01603277
'''
def color(genotype):
    """
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    """
    #definition
    phenotype = list()
    Cgene = genotype[0:2] # divided in two parts
    Dgene = genotype[2:4]
    # figure out phenotype, if dominant allele exists, the dominant characteristic will come out.
    if 'C' in Cgene:
        phenotype.append('C')
    else:
        phenotype.append('c')
    
    if 'D' in Dgene:
        phenotype.append('D')
    else:
        phenotype.append('d')
    # resulting combination of phenotypes   
    if ['C', 'D'] == phenotype:
        return 'seal'
    elif ['C', 'd'] == phenotype:
        return 'blue'
    elif ['c', 'D'] == phenotype:
        return 'chocolate'
    else:
        return 'lilac'
    
def combinations(genotype):
    """
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    """
    #definition
    result = list()
    # append genotypes as the given format
    result.append(genotype[::2])
    result.append(genotype[::3])
    result.append(genotype[1:3])
    result.append(genotype[1::2])
    
    return result

def punnett(mate1, mate2, pprint = False):
    """
    >>> print(punnett('CcDd', 'CcDd'))
    [['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
    >>> print(punnett('CcDd', 'CcDd', pprint=True))
    CCDD CCDd CcDD CcDd
    CCdD CCdd CcdD Ccdd
    cCDD cCDd ccDD ccDd
    cCdD cCdd ccdD ccdd
    >>> print(punnett('cCDd', 'CcdD', pprint=True))
    cCDd cCDD ccDd ccDD
    cCdd cCdD ccdd ccdD
    CCDd CCDD CcDd CcDD
    CCdd CCdD Ccdd CcdD
    """
    #definition
    result = list()
    line = list()
    combimate1 = combinations(mate1)
    combimate2 = combinations(mate2)
    finalresult = str()
    # making a line in punett square
    for ngene1 in combimate1:
        for ngene2 in combimate2:
            line.append(ngene1[0] + ngene2[0] + ngene1[1] + ngene2[1])
        result.append(line)
        line = list()
    # if pprint is true, the result comes out as a expression of the punett square.
    if pprint:
        for line in result:
            linestring = ' '.join(line) # combining elements in line
            finalresult += linestring + '\n'
        return finalresult.rstrip() #for eliminating the last left enter by '\n'
    
    else:
        return result
    
def colorDistribution(mate1, mate2):
    """
    >>> colorDistribution('CcDd', 'CcDd')
    {'blue': 3, 'seal': 9, 'lilac': 1, 'chocolate': 3}
    >>> colorDistribution('cCDD', 'cCDD')
    {'seal': 12, 'chocolate': 4}
    >>> colorDistribution('ccDD', 'ccDD')
    {'chocolate': 16}
    >>> colorDistribution('ccdd', 'CcDd')
    {'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
    """
    #definition of dict
    countpheno = dict()
    countpheno['blue'] = 0
    countpheno['seal'] = 0
    countpheno['lilac'] = 0
    countpheno['chocolate'] = 0
    # definition of target
    descendant = punnett(mate1, mate2)
    # counting dict values
    for line in descendant:
        for genotype in line:
            phenotype = color(genotype)
            if phenotype == 'seal':
                countpheno['seal'] += 1
            elif phenotype == 'blue':
                countpheno['blue'] += 1
            elif phenotype == 'chocolate':
                countpheno['chocolate'] += 1
            else:
                countpheno['lilac'] += 1
    # elminating zero-valued keys
    for element in ['seal', 'blue', 'chocolate', 'lilac']:
        if countpheno[element] == 0:
            del countpheno[element]
    
    return countpheno

if __name__ == '__main__':
    import doctest
    doctest.testmod()