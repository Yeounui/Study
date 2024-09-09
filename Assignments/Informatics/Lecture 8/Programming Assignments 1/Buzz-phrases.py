'''
Created on 2016. 11. 8.

@author: korea
'''
#import random
#random.choice(list, 3)

#random.randint(1,5)

def buzzphrase1(candidated):
    import random
    result = str()
    for queue in candidated:
        result += random.choice(queue) + ' '
    result = result.rstrip()
    return result

def buzzphrase2(*candidated):
    return buzzphrase1(candidated) # if use *candidated instead of candidated, the files of value are unpacked.
    
buzz1 = ('integrated', 'total', 'systematized', 'parallel', 'functional', 'responsive', 'optional7', 'synchronized', 'compatible', 'balanced')
buzz2 = ('management', 'organizational', 'monitored', 'reciprocal', 'digital', 'logistical6', 'transitional', 'incremental', 'third-generation', 'policy')
buzz3 = ('options', 'flexibility', 'capability', 'mobility', 'programming', 'concept', 'time-phase', 'projection', 'hardware', 'contingency')
print(buzzphrase2(buzz1, buzz2, buzz3))


#somefunction(1,2,3,4,5)
#def somefunction(a,b,*c):
#    a -> 1
#    b -> 2
#    c -> (3,4,5)