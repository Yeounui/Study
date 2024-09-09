'''
Created on 2017. 3. 11.

@author: korea
'''
class WordSquare:
    def __init__(self, length, target):
        assert length*(length+1)/2 == len(target), 'invalid square' 
        self.length = length
        self.target = target
        storage = list()
        order3 = 0
        for order1 in range(length):
            for order2 in range(order1+1):
                storage.append((order1, order2, target[order3].upper()))
                order3 += 1
        self.storage = storage
        
    def letter(self, xaxis, yaxis):
        assert self.length-1 >= xaxis and self.length-1 >= yaxis, 'invalid index' 
        for info in self.storage:
            if (info[0] == xaxis and info[1] == yaxis) or (info[0] == yaxis and info[1] == xaxis):
                return info[2]
    
    def word(self, axis):
        assert self.length-1 >= axis, 'invalid index'
        result = ''
        carrier = list()
        for info in self.storage:
            if info[0] == axis or info[1] == axis:
                carrier.append(info)
        for order in range(self.length):
            for info in carrier:
                if info[1] == order or info[0] == order:
                    result += info[2]
                    carrier.remove(info)
                    break
        return result
    
    def __repr__(self):
        result = ''
        for order in range(self.length):
            result += self.word(order) + '\n'
        result = result.rstrip('\n')
        return result
    
    def valid(self, giventxt):
        trigger = 0
        measurement = list()
        for line in range(self.length):
            measurement.append(self.word(line))
        opentxt = open(giventxt, 'r')
        readtxt = opentxt.readline().strip('\n')
        while readtxt:
            for apart in measurement:
                if readtxt == apart.lower():
                    trigger += 1
            readtxt = opentxt.readline().strip('\n')
        if trigger == self.length:
            return True
        else:
            return False
         
square = WordSquare(3, 'bicten')
print(square.storage)
print(square.letter(1, 0))
print(square.letter(1, 1))
print(square.letter(1, 2))
print(square.word(1))
print(square)
print(square.valid('words.txt'))
square = WordSquare(4, 'ABCDEFGHIJ')
print(square.valid('words.txt'))
square = WordSquare(9, 'ACRHEXANABLINOLADDLEHSERINETINITIATOASCENDERS')
print(square.valid('words.txt'))