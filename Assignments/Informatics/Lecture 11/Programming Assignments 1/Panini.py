class Panini:
    def __init__(self, givenlist):
        detect = 0
        orderlist = list()
        if type(givenlist) == int:
            givenlist = [givenlist]
        else:
            assert type(givenlist) == tuple or type(givenlist) == list or type(givenlist) == set, 'invalid stickers'
            for element in givenlist:
                assert type(element) == int, 'invalid stickers'
            givenlist = list(givenlist)
        givenlist1 = givenlist.copy()
        for element in givenlist1:
            while givenlist.count(element) != 1:
                givenlist.remove(element)
        while len(givenlist) != 0:
            if detect in givenlist:
                order = givenlist.index(detect)
                orderlist.append(givenlist[order])
                givenlist.remove(detect)
            detect += 1
        self.list = orderlist
    
    def __repr__(self):
        result = ''
        if len(self.list) == 0:
            return result
        compared = self.list[0]
        initstorage = self.list[0]
        laststorage = None
        while self.list[-1] != laststorage:
            if compared in self.list:
                if initstorage != None:
                    compared += 1
                else:
                    initstorage = compared
                
            elif compared not in self.list:
                laststorage = compared - 1
                if initstorage == laststorage:
                    result += '{}, '.format(initstorage)
                elif type(initstorage) == int and type(laststorage) == int:
                    result += '{}-{}, '.format(initstorage, laststorage)
                initstorage = None
                compared += 1
        return result.rstrip(', ')

    def __add__(self, other):
        selflist = self.list.copy()
        for element in other.list:
            if element in self.list:
                selflist.remove(element)
        return Panini(selflist + other.list)
    
    def __sub__(self, other):
        selflist = self.list.copy()
        for element in other.list:
            if element in self.list:
                selflist.remove(element)
        return Panini(selflist)

print(Panini((20, 35, 23, 34, 35, 2, 23, 18, 27, 10, 5, 2, 14)))
collection1 = Panini([1, 3, 4, 5, 6, 7, 9, 10, 11, 17, 19, 20])
print(collection1)
collection2 = Panini(8)
print(collection2)
collection3 = collection1 + collection2
print(collection3)
collection4 = collection1 - Panini((5, 8))
print(collection4)
print(collection1)
print(collection1 - Panini({1, 2, 3, 4}) + Panini(list(range(10, 19))))
Panini([1, 2, 3.14])
Panini('spam')