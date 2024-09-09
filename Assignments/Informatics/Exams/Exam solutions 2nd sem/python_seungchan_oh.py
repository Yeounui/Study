'''
Created on 2017. 6. 16.

@author: korea
'''
class Diana:
    def __init__(self, giventxt):
        result = ''
        opentxt = open(giventxt, 'r')
        readtxt = opentxt.readline()
        while readtxt:
            readtxt = readtxt.replace('\n', ' ')
            result += readtxt
            readtxt = opentxt.readline()
        self.otptxt = result

    def index(self, targetpad):
        assert targetpad in self.otptxt, 'invalid prefix'
        order1 = len(targetpad.replace(' ', ''))
        location = self.otptxt.find(targetpad)
        order2 = len(self.otptxt[:location].replace(' ', ''))
        return order1 + order2
        
    def trigraph(self, alpha1, alpha2):
        assert len(alpha1) == len(alpha2), 'one-time pad is too short'
        combinedorder = ord(alpha1.upper()) + ord(alpha2.upper()) - 130
        ordernum = (25-combinedorder) % 26
        resultalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[ordernum]
        return resultalpha
        
    def encode(self, givenstring, nfactor = 10):
        result = ''
        target1 = givenstring[:nfactor+nfactor//5-1]
        target2 = givenstring[nfactor+ nfactor//5:].replace(' ', '')
        startnum = self.index(target1)
        target11 = self.otptxt.replace(' ', '')[startnum:startnum+len(target2)]
        for ordernum in range(len(target11)):
            result += self.trigraph(target11[ordernum], target2[ordernum])
        return result
    
    def decode(self, givencode, nfactor = 10):
        result = ''
        prestart = givencode[:nfactor+ nfactor//5-1]
        subjectcode = givencode[nfactor+ nfactor//5:].replace(' ', '')
        startnum = self.index(prestart)
        target = self.otptxt.replace(' ', '')[startnum:startnum+len(subjectcode)]
        for order in range(len(subjectcode)):
            result += self.trigraph(subjectcode.replace(' ', '')[order], target[order])
        return result

diana=Diana('otp.txt')
print(diana.otptxt)
print(diana.index('UKVTF WZHOK'))
print(diana.index('CMMXT VYTJI RRQGU'))
'print(diana.index(''ABCDE FGHIJ''))'
print(diana.trigraph('Q', 'K'))
print(diana.trigraph('t', 'f'))

print(diana.encode('UKVTF WZHOK attack at dawn'))
print(diana.encode('CMMXT VYTJI RRQGU meet at ten tonight', 15))
"print(diana.encode('ABCDE FGHIJ zero dark thirty'))"
"print(diana.encode('VAXPM IPIXU zero dark thirty'))"

print(diana.decode('UKVTF WZHOK TSPDZ TVNRI BY'))
print(diana.decode('CMMXT VYTJI RRQGU SVYRN YRNPM VSULD U', 15))
"print(diana.decode('ABCDE FGHIJ zero dark thirty'))"
"print(diana.decode('VAXPM IPIXU zero dark thirty'))"