'''
Created on 2018. 7. 3.

@author: korea
'''
class Assembler:
    def __init__(self, targettxt):
        opentxt = open(targettxt, 'r')
        readtxt = opentxt.readline()
        
        packetdict = dict()
        packetlist = list()
        
        while readtxt:
            firstindex = readtxt.find('\t')
            packetdict['uniqcode'] = int(readtxt[:firstindex])
            secondindex = readtxt[firstindex+2-1:].find('\t')
            packetdict['index'] = int(readtxt[firstindex+2-1:firstindex+2-1+secondindex])
            thirdindex = readtxt[firstindex+2+secondindex:].find('\t')
            packetdict['number'] = int(readtxt[firstindex+2+secondindex:firstindex+2+secondindex+thirdindex])
            packetdict['text'] = readtxt[firstindex+2+secondindex+thirdindex:].strip()
            
            packetlist.append(packetdict)
            packetdict = dict()
            readtxt = opentxt.readline()
        
        opentxt.close()
        
        self.packetlist = packetlist

    def isComplete(self, givenuniqcode):
        switch = 0
        compareset = set()
        global countset
        countset = {adict['index'] for adict in self.packetlist if adict['uniqcode'] == givenuniqcode}
        for adict in self.packetlist: 
            if adict['uniqcode'] == givenuniqcode:
                global number
                number = adict['number']
                compareset = set(range(number))
                break
            
        if countset != compareset or countset == set():
            return False
        else:
            return True
                    
    def completeMessages(self):
        innatecode= set(adict['uniqcode'] for adict in self.packetlist)
        return set(code for code in list(innatecode) if self.isComplete(code))
    
    def incompleteMessages(self):
        incompdict = dict()
        innatecode= set(adict['uniqcode'] for adict in self.packetlist)
        for code in list(innatecode):
            if not self.isComplete(code):
                incompdict[code] = len(countset), number
        return incompdict

    def message(self, givenuniqcode):
        assert self.isComplete(givenuniqcode), 'incomplete message'
        indexcount = 0
        resultstr = ''
        chosenpacketlist = [adict for adict in self.packetlist if adict['uniqcode'] == givenuniqcode]    
        while indexcount != number:
            for adict in chosenpacketlist:
                if adict['index'] == indexcount:
                    resultstr += str(adict['index']) + '. ' +adict['text'] +'\n'
            indexcount += 1
        return resultstr.rstrip('\n')



assembler = Assembler('packets_01.txt')
print(assembler.isComplete(6220))
print(assembler.isComplete(5181))
print(assembler.isComplete(1234))
print(assembler.completeMessages())
print(assembler.incompleteMessages())
print(assembler.message(6220))
assembler = Assembler('packets_02.txt')
print(assembler.isComplete(2997))
print(assembler.isComplete(1938))
print(assembler.isComplete(1234))
print(assembler.completeMessages())
print(assembler.incompleteMessages())