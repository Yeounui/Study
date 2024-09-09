'''
Created on Nov 18, 2018

@author: DELL
'''

import MyInputReader as mir
import Mynetwork as mn
import NetworkModel as nm
import MyMetrics as mm


'''
1)Read the fasta file, concatenate the multiple lines and then produce one long string.
'''
listoflines = [line.rstrip('\n') for line in open('full_sample.fasta')]

#remove the first element of the list as it is simply the header
listoflines.pop(0)

fullsequence = ''
#Create the long concatenated list
for strand in listoflines:
    fullsequence += strand


'''
2)Extract all donor sites, also the 99 nucleotides before and after_test
'''
#this list gives us the index at which the splice site occurs
poslist = []
#this list gives us all the donor sites as well as 99 nucleotides before and after the possible splice site 
strandlist = []

for pos in range(99,len(fullsequence) - 100):

    #If it is GC then add it to poslist and strandlist
    if fullsequence[pos:pos+2] == 'GT':
        poslist.append(pos)
        #We have to include 99 nucleotides before and after the splice site     
        strandlist.append(fullsequence[pos - 99:pos + 2 + 99])
        

'''
3)Convert all strands in strandlist to one hot encoding so it can be used our model
'''
#this list contains all strands after one hot encoding 
onehotencodedlist = []

for possplicesite in strandlist:
    
    #Reused code from Myinput reader
    encodedstrand = []
    
    for nucleotide in possplicesite:
        if nucleotide == 'A':
            encodedstrand.append([1,0,0,0])
            
        if nucleotide == 'C':
            encodedstrand.append([0,1,0,0])
            
        if nucleotide == 'G':
            encodedstrand.append([0,0,1,0])
            
        if nucleotide == 'T':
            encodedstrand.append([0,0,0,1])
            
    onehotencodedlist.append(encodedstrand)

 
'''
4)Train a new model and 5)Predict the positive probability of each candidate splice site 
'''
    
#This is for the pre-procecssing of the training set
trainX, trainY = mir.inputreader('inputs/train.pos', 'inputs/train.neg')
validX, validY = mir.inputreader('inputs/valid.pos', 'inputs/valid.neg')

#First create a model using our custom neural network    
model = mn.create_network_c()

#print the model details and train the model first
model.printDetails()
result = model.train(trainX, trainY, validX, validY, 20)

resulttypes = model.generatePredictions(onehotencodedlist)

#remember we only want positive probability so it is the second element in each tuple of the list of predictions generated

#this list contains the positive probability of each possible splice site
listofposprobs = []
for posnegpredict in resulttypes:
    listofposprobs.append(posnegpredict[1])


'''
6)Print out your results in a clean output format, where you list the candidate splice site's position, the local context (+/- 10-15 nucleotides) 
and the predicted probability in different columns.
'''
#So the data in lists we need
#1)positions are all listed in poslist
#2)hit with context is listed in strandlist
#3)positive probabilities are listed in listofposprobs

#First thing we do is shorten the splice site from +-99 to +-10
shortenedstrandlist = []
for strand in strandlist:
    shortenedstrandlist.append(strand[99 - 10:99 + 2 + 10])

#hit with context shortened is in shortenedstrandlist

print(' {:^5} | {:^22} | {:^20} '.format('Position', 'Hit (with context)', 'Score (positive probability)'))
#Just to seperate the header and the data
print('-{:-^65}-'.format(''))
for pos in range(0,len(shortenedstrandlist)):
    print(poslist[pos], '      |', shortenedstrandlist[pos], '|', listofposprobs[pos])