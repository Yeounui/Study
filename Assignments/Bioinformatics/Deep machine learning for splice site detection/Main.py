'''
Created on Nov 7, 2018

@author: Bo-kyung Jin (01603251) and Seungchan Oh (01603277)
Group 11
'''
import MyInputReader as mir
import Mynetwork as mn
import NetworkModel as nm
import MyMetrics as mm

#This is for the pre-procecssing of the training set
trainX, trainY = mir.inputreader('inputs/train.pos', 'inputs/train.neg')
validX, validY = mir.inputreader('inputs/valid.pos', 'inputs/valid.neg')


#Question 6 
#Note that when creating a model it can be create_network_a or create_network_b, it depends on which type of neural network we want to use.
model = mn.create_network_c()

model.printDetails()
result = model.train(trainX, trainY, validX, validY, 30)


#Question 7 
testX, testY = mir.inputreader('inputs/test.pos', 'inputs/test.neg')
resulttypes = model.generatePredictions(testX)

recallz = mm.recallscore(resulttypes,testY)
print('This is the recall score: ' + str(recallz))
precisionz = mm.precisionscore(resulttypes,testY)
print('This is the precision score: ' + str(precisionz))
f1z = mm.f1score(recallz, precisionz)
print(f1z)