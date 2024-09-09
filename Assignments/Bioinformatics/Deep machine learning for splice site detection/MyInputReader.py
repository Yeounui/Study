'''
Created on Nov 7, 2018

@author: Bo-kyung Jin (01603251) and Seungchan Oh (01603277)
Group 11
'''
def inputreader(datafile1,datafile2):
    trainX = []
    trainY = []
    
    #turning text representation into a list of lines
    #datafile1 is positive, datafile2 is negative
    listoflinespositive = [line.rstrip('\n') for line in open(datafile1)]
    
    listoflinesnegative = [line.rstrip('\n') for line in open(datafile2)]
    
    #Calculating trainY first, positives get a weight of one, negatives a weight of zero
    trainY.extend(1 for i in range(len(listoflinespositive)))
    trainY.extend(0 for i in range(len(listoflinesnegative)))
    
    for seq in listoflinespositive:
        trainX.append(onehotencoder(seq))
        
    for seq in listoflinesnegative:
        trainX.append(onehotencoder(seq))
        
    return trainX,trainY
    
def onehotencoder(sequence):
    
    encodedlist = []
    
    for nucleotide in sequence:
        if nucleotide == 'A':
            encodedlist.append([1,0,0,0])
            
        if nucleotide == 'C':
            encodedlist.append([0,1,0,0])
            
        if nucleotide == 'G':
            encodedlist.append([0,0,1,0])
            
        if nucleotide == 'T':
            encodedlist.append([0,0,0,1])
            
    return encodedlist