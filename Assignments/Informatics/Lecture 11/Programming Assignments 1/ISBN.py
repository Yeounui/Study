'''
Created on 2017. 3. 11.

@author: korea
'''
class ISBN13:
    def __init__(self, isbncode, countrygroup = 1):
        assert type(isbncode) == int, 'ISBN-13 code is an integer argument.'
        assert 1 <= countrygroup <= 5, 'Make sure this number is in between 1 and 5.'
        self.isbn = isbncode
        self.country = countrygroup
        
    def __str__(self):
        strisbncode = str(self.isbn)
        return '{}-{}-{}-{}'.format(strisbncode[:3], strisbncode[3], strisbncode[4:12], strisbncode[12])
    
    def __repr__(self):
        return 'ISBN13({}, {})'.format(self.isbn, self.country)
    
    def isValid(self):
        firstsum = 0
        secondsum = 0
        for firstnumber in str(self.isbn)[:12:2]:
            firstsum += int(firstnumber)
        for secondnumber in str(self.isbn)[1:12:2]:
            secondsum += int(secondnumber)
        value = (10 - (firstsum + 3*secondsum) % 10) % 10
        if int(str(self.isbn)[12]) == value:
            return True
        else:
            return False
        
    def asISBN10(self):
        sum = 0
        isbncode = str(self.isbn)[3:13]
        for order in range(1, 10):
            sum += order * int(isbncode[order-1])
        value = sum % 11
        return '{}-{}-{}'.format(isbncode[0], isbncode[1:9], value)
