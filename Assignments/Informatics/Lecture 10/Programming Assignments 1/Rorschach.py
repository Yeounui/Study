'''
Created on 2017. 3. 5.

@author: korea
'''
def rorschach(ptrntxt, target = None):
    initread = open(ptrntxt, 'r')
    carrier2 = str()
    line = initread.readline()
    while line:
        carrier1 = line.replace('\n', '')
        carrier2 += carrier1 + carrier1[::-1] + '\n'
        line = initread.readline()
    initread.close()
    carrier2 = carrier2.rstrip()
    if target is None:
        print(carrier2)
    else:
        initwrite = open(target, 'w')    
        initwrite.write(carrier2)
        initwrite.close()
    
        
rorschach('C:/Users/korea/Documents/rorschach1.txt')