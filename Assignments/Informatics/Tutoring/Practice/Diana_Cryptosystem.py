'''
Created on 2017. 8. 14.

@author: korea
'''
class Diana:
    def __init__(self, textfile):
        padcopy = ''
        opentext = open(textfile, 'r')
        readtext = opentext.readline()
        while readtext:
            padcopy += readtext.replace('\n', ' ')
            readtext = opentext.readline()
        for aletter in padcopy:
            if not aletter.isalpha():
                padcopy = padcopy.replace(aletter, '')
        padcopy = padcopy.upper()
        self.padcopy = padcopy
    
    def index(self, targetstr):
        targetstr = targetstr.upper()
        for aletter in targetstr:
            if not aletter.isalpha():
                targetstr = targetstr.replace(aletter, '')
        padcopy = self.padcopy.replace(' ', '')
        assert targetstr in padcopy, 'invalid prefix'
        prelocus = padcopy.find(targetstr)
        return prelocus+len(targetstr)
    
    def trigraph(self, letter1, letter2):
        p1p2 = ord(letter1.upper()) + ord(letter2.upper()) - 130
        return chr((25 - p1p2)%26 + 65)
    
    def encode(self, mixedstr, locus=10):
        encoded = ''
        for aletter in mixedstr:
            if not aletter.isalpha():
                mixedstr = mixedstr.replace(aletter, '')
        prepadlocus = mixedstr[:locus]
        padlocus = self.index(prepadlocus.upper())
        strand2 = mixedstr[locus:]
        prestrand1 = self.padcopy[padlocus:]
        assert len(prestrand1) >= len(strand2), 'one-time pad is too short'
        strand1 = prestrand1[:len(strand2)]
        comparedlist = list(zip(list(strand1), list(strand2)))
        for aletter in comparedlist:
            encoded += self.trigraph(*aletter)
        return encoded
    
    def decode(self, mixedstr, locus=10):
        return self.encode(mixedstr, locus)

diana = Diana('otp.txt')
#print(Diana('otp.txt').padcopy)
#print(diana.index('UKVTF WZHOK'))
#print(diana.index('ABCDE FGHIJ'))
#print(diana.trigraph('Q', 'K'))
#print(diana.encode('UKVTF WZHOK attack at dawn'))
#print(diana.encode('CMMXT VYTJI RRQGU meet at ten tonight', 15))
#print(diana.encode('ABCDE FGHIJ zero dark thirty'))
#print(diana.decode('UKVTF WZHOK TSPDZ TVNRI BY'))
#print(diana.decode('CMMXT VYTJI RRQGU SVYRN YRNPM VSULD U', 15))
#print(diana.index('EZI*EG^PUK'))
diana2 = Diana('otp2.txt')
print(diana2.padcopy)
print(diana2.index('CY)|SXD'))