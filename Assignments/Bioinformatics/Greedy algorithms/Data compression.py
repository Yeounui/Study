# ZIP compress strings as bit strings, and decompress bit strings into strings according to the Huffman coding scheme.
class ZIP:
    """
    >>> zip = ZIP('codes.txt')

    >>> zip.symbol2bitstring('i')
    '1000'
    >>> zip.symbol2bitstring('e')
    '000'
    >>> zip.symbol2bitstring('T')
    Traceback (most recent call last):
    AssertionError: unknown symbol "T"

    >>> zip.bitstring2symbol('1000')
    'i'
    >>> zip.bitstring2symbol('000')
    'e'
    >>> zip.bitstring2symbol('01')
    Traceback (most recent call last):
    AssertionError: invalid bitstring

    >>> zip.compress('internet')
    '1000001001100001100000100000110'
    >>> len(zip.compress('internet'))
    31
    >>> zip.compress('internet explorer')
    '1000001001100001100000100000110111000100101001111001001101100000011000'
    >>> zip.compress('mozilla firefox')
    Traceback (most recent call last):
    AssertionError: unknown symbol "z"

    >>> zip.decompress('1000001001100001100000100000110')
    'internet'
    >>> zip.decompress('1000001001100001100000100000110111000100101001111001001101100000011000')
    'internet explorer'
    >>> zip.decompress('10000010011000011000001000001101')
    Traceback (most recent call last):
    AssertionError: invalid bitstring
    >>> zip.decompress('10000010011000011000000000110')
    Traceback (most recent call last):
    AssertionError: invalid bitstring
    """

    def __init__(self, textfile):
        # read text file and make a dictionary (key= symbol, value= bit string)
        codeTable = {}
        with open(textfile) as openfile:
            for line in openfile:
                sym, bit = line.rstrip().split('\t')
                codeTable[sym] = bit

        self.cT = codeTable

    # Compress symbol --> bit string
    def symbol2bitstring(self, sym2com):
        assert sym2com in self.cT, 'unknown symbol "{}"'.format(sym2com)  # given symbol does not occur in the file
        return self.cT[sym2com]

    # Decompress bit string --> symbol
    def bitstring2symbol(self, bit2decom):
        assert bit2decom in self.cT.values(), 'invalid bitstring'    # given bit string does not occur in the file
        return list(self.cT.keys())[list(self.cT.values()).index(bit2decom)]


    ########################################################################################################
    # # 2nd method: by switching keys and values (less efficient - need more steps to switch the dictionary)
    # def bitstring2symbol(self, bit2decom):
    #     reversed_cT = {self.cT[sym]: sym for sym in self.cT}    # switch keys and values
    #     assert bit2decom in reversed_cT, 'invalid bitstring'    # given bit string does not occur in the file
    #     return reversed_cT[bit2decom]
    ########################################################################################################


    # Compress string of symbols --> bit string
    def compress(self, str2com):
        compressed = ''
        for sym in str2com:
            # find the bit string representations of symbols
            compressed += self.symbol2bitstring(sym)
        return compressed

    # Decompress bit string --> original string
    def decompress(self, str2decom):
        decompressed = ''
        # repeat until there is no bit string left to decompress
        while str2decom:
            # find the symbol whose corresponding bit string is a prefix of the given bit string
            occur = 0
            for sym, bit in self.cT.items():
                if str2decom.startswith(bit): # check whether prefix is bit.
                    occur += 1
                    decompressed += sym
                    str2decom = str2decom[len(bit):]    # remove the corresponding prefix
                    break
            assert occur, 'invalid bitstring'  # given bit string does not occur in the file
        return decompressed


if __name__ == '__main__':
    import doctest
    doctest.testmod()