'''
Created on Nov 7, 2018

@author: Bo-kyung Jin (01603251) and Seungchan Oh (01603277)
Group 11
'''
from NetworkModel import NetworkModel
#A regular neural network, with an input layer, two fully-connected layers with each 50 neurons, and an output layer.
#Note that no convolutional or pooling layers should be added here.
def create_network_a():
    
    #Create the model
    model = NetworkModel()
    
    model.addInputLayer()
    model.addFullyConnectedLayer(50)
    model.addFullyConnectedLayer(50)
    model.addOutputLayer()
    
    return model


#The basic convolutional neural network that was shown in the slides (slide number 18)
def create_network_b():
   
   #Create the model
    model = NetworkModel()
    model.addInputLayer()
    
    model.addConvLayer(10,7)
    model.addMaxPoolLayer(5)
    model.addConvLayer(20,5)
    model.addMaxPoolLayer(5)
    model.addFullyConnectedLayer(15)
    model.addOutputLayer()
    
    return model
    
    
#Your own convolutional neural network. For this topology, you can start from the basic network (b) and add more layers, filters, neurons, etc. 
#With your own network, try to improve the validation cost of the basic network as much as possible. Further comparisons (using other metrics) will be made in Section 7.
def create_network_c():
    
    #Create the model
    model = NetworkModel()
    model.addInputLayer()
    
    model.addConvLayer(200,7)
    model.addMaxPoolLayer(5)
    model.addConvLayer(400,5)
    model.addMaxPoolLayer(5)
    model.addFullyConnectedLayer(15)
    model.addOutputLayer()
    
    return model