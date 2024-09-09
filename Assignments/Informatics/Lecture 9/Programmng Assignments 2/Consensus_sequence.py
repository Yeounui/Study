'''
Created on 2016. 11. 14.

@author: Seungchan Oh
@student_number: 01603277
'''
def profile(seqs):
    # Error decision
    for order in range(1, len(seqs)):
        assert len(seqs[0]) == len(seqs[order]), 'sequences should have equal length' 
    #Definition
    result = dict()
    Anumber = 0
    Tnumber = 0
    Cnumber = 0
    Gnumber = 0
    Astorage = list()
    Tstorage = list()
    Cstorage = list()
    Gstorage = list()
    for order in range(len(seqs[0])):
        for seq in seqs:
            if seq[order] == 'A':
                Anumber += 1
            elif seq[order] == 'T':
                Tnumber += 1
            elif seq[order] == 'C':
                Cnumber += 1
            else:
                Gnumber += 1
        #initialization
        Astorage.append(Anumber) 
        Tstorage.append(Tnumber)
        Cstorage.append(Cnumber)
        Gstorage.append(Gnumber)
        Anumber = 0
        Tnumber = 0
        Cnumber = 0
        Gnumber = 0
    # input value into dictionary
    result['A'] = Astorage
    result['T'] = Tstorage
    result['C'] = Cstorage
    result['G'] = Gstorage
    return result

def consensus(profile):
    #definition
    result = ''
    #deciding highest value among bases
    for order in range(len(profile['A'])):
        highestnum = profile['A'][order]
        mark = 'A'
        if highestnum < profile['T'][order]:
            highestnum = profile['T'][order]
            mark = 'T'
        if highestnum < profile['G'][order]:
            highestnum = profile['G'][order]
            mark = 'G'
        if highestnum < profile['C'][order]:
            mark = 'C'
        # deciding 'N'
        for base in 'ATCG':
            if base != mark:
                if profile[base][order] == profile[mark][order]:
                    mark = 'N'
                    break
        # appending mark into result
        result += mark
    return result