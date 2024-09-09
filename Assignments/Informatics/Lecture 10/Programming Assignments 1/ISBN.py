'''
Created on 2017. 3. 2.

@author: korea
'''
def displayBookInfo(code):
    sum1 = 0
    sum2 = 0
    text = ''
    for letter in str(code)[0:12:2]:
        sum1 += int(letter)
    for letter in str(code)[1:12:2]:
        sum2 += int(letter)
    determin = (10 - (sum1 + 3*sum2) % 10) % 10
    if determin == int(str(code)[12]):
        from urllib.request import urlopen
        url = urlopen('http://isbndb.com/api/books.xml?access_key=ZFD8L2Z5&index1=isbn&value1=' + str(code))
        for urlline in url:
            line = urlline.decode('utf-8')
            if '<Title>' in line:
                initnum = line.index('>')+1
                endnum = line[1:].index('<')+1
                text += ('Title: '+ line[initnum:endnum] + '\n')
            elif '<AuthorsText>' in line:
                initnum = line.index('>')+1
                endnum = line[1:].index('<')+1
                text += ('Authors: '+ line[initnum:endnum].rstrip(', ') + '\n')
            elif '<PublisherText' in line:
                initnum = line.index('>')+1
                endnum = line[1:].index('<')+1
                text += ('Publisher: '+ line[initnum:endnum])
        print(text)   
    else:
        print('Wrong ISBN-13 code')
    
displayBookInfo('9780547125329')
displayBookInfo('9780321714725')