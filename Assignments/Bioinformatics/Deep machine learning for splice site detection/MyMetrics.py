'''
Created on Nov 14, 2018

@author: DELL
'''
import MyInputReader as mir

def recallscore(predictions, testY):
    
    #Number of true positives, false positives, true negatives, false negatives
    TP = 0            
    FP = 0                      
    TN = 0                    
    FN = 0
    
    for pos in range(0,len(testY)):
        
        #First check if there is actually a splice site or not
        if testY[pos] == 1:
            if predictions[pos][1] < 0.5:
                FN += 1
            else:
                TP += 1 
        else:
            if predictions[pos][1] < 0.5:
                TN += 1
            else:
                FP += 1
    
    print('The number of true positives are: ' + str(TP))
    print('The number of false positives are: ' + str(FP))
    print('The number of true negatives are: ' + str(TN))
    print('The number of false negatives are: ' + str(FN))
    
    recall = TP/(TP + FN)
    return recall

 
def precisionscore(predictions, testY):
    
    #Number of true positives, false positives, true negatives, false negatives
    TP = 0            
    FP = 0                      
    TN = 0                    
    FN = 0
    
    for pos in range(0,len(testY)):
        
        #First check if there is actually a splice site or not
        if testY[pos] == 1:
            if predictions[pos][1] < 0.5:
                FN += 1
            else:
                TP += 1 
        else:
            if predictions[pos][1] < 0.5:
                TN += 1
            else:
                FP += 1
    
    precision = TP/(TP + FP)
    return precision
    
def f1score(recall, precision):
    
    f1 = (2 * (precision * recall))/(precision + recall)
    
    return 'This is our F1, harmonic mean, score: ' + str(f1)