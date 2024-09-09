class Square:
    def __init__(self, templatestr='ABCDEFGHIKLMLOPQRSTUVWXYZ'): 
        pretemplate = 'ABCDEFGHIKLMLOPQRSTUVWXYZ'
        if templatestr != 'ABCDEFGHIKLMLOPQRSTUVWXYZ':
            for aletter in templatestr:
                if aletter in templatestr:
                    pretemplate = pretemplate.replace(aletter, '') # remove,
            pretemplate = templatestr+pretemplate #and append
        self.templatestr = pretemplate 
        
    def __str__(self):
        #definition
        order1 = 5
        template = self.templatestr
        #append 'additional characters between alphabets'
        while len(template) > order1:
            template = template[:order1] + '!' + template[order1:]
            order1 += 6
        template.split()
        template = '@'.join(template)
        template = template.replace('@!@', '\n').replace('@', ' ') #and replace them into space 
        return template      # change according to your needs

    def letter(self, yorbit, xorbit):
        assert  0 <= xorbit <= 4 and 0 <= yorbit <= 4, 'invalid position'
        recent = xorbit + 5*yorbit
        result = self.templatestr[recent].upper() #Using string we can find orbit of a letter.  a orbit possiblity: 0,1,2,3,4
        return result             # change according to your needs


    def position(self, aletter):
        assert aletter in self.templatestr, 'invalid letter'
        for recenty in range(0, 5):
            for recentx in range(0, 5):
                if self.letter(recenty, recentx) == aletter: #By using previous function, find out location
                    return (recenty, recentx) # change according to your needs
    
        """
    >>> square = Square()
    >>> print(square)
    A B C D E
    F G H I K
    L M N O P
    Q R S T U
    V W X Y Z

    >>> square.letter(3, 2)
    'S'
    >>> square.letter(7, 1)
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> square.position('A')
    (0, 0)
    >>> square.position('?')
    Traceback (most recent call last):
    AssertionError: invalid letter
    
    >>> square = Square('EXAMPLE')
    >>> print(square)
    E X A M P
    L B C D F
    G H I K N
    O Q R S T
    U V W Y Z

    >>> square.letter(3, 2)
    'R'
    >>> square.position('A')
    (0, 2)

    >>> square = Square('keyword')
    >>> print(square)
    K E Y W O
    R D A B C
    F G H I L
    M N P Q S
    T U V X Z
    """
    
class FourSquare:

    def __init__(self):

        test = Square()     # change according to your needs

    def encode(self):

        return('Encoded')   # change according to your needs

    def decode(self):

        return('Decoded')   # change according to your needs
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()