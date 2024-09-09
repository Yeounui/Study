'''
Created on 2016. 11. 14.

@author: Seungchan Oh
@student_number: 01603277
'''
def lettervalue(word):
    # Error condition when the length of letterstring is not odd number or No alphabet letter are involved
    assert len(word)%2 == 1 and word.isalpha() and len(set(word)) == len(word), 'invalid letterstring'
    # Definition
    result = dict()
    n = -((len(word)-1)//2)
    # Providing values to letter in word
    for letter in word.upper():
        result[letter] = n
        n += 1
    return result

def wordvalue(word, letterstring):
    #Definition
    compared = lettervalue(letterstring)
    value = 0
    #combining each value of a letter
    for letter in word.upper():
        assert letter in compared, 'missing letters'
        value += compared[letter]
    return value

def alignment(wordlist, letterstring):
    #Definition
    compared = list()
    for word in wordlist:
        try:
            compared.append(wordvalue(word, letterstring))
        except:
            pass
    # compare length of dict and wordlist
    if compared == [element for element in range(len(wordlist))]:
        return True
    else:
        return False
    
def arrange1(planets, letterstring):
    #Definition
    orbitdict = dict()
    result = list()
    trigger = 0
    compared1 = 0
    compared2 = 0
    ordernum = 0
    #constructing dictionary 'orbitdict'
    for planet in planets:
        orbitdict[planet] = wordvalue(planet, letterstring)
    # making the arranged list 'result'
    result.append(planets[0])
    for planet in planets[1:]: # comparing dictionary value between planets' elements and result's elements 
        for queue in result:
            
            
            if orbitdict[planet] < orbitdict[queue]: # stop increasing ordernum when value of element in result is higher than result
                result.insert(ordernum, planet) # And then insert element of planets
                ordernum = 0 #initializing ordernum
                break
            
            elif orbitdict[planet] == orbitdict[queue]: # compare alphabetical order when the values are same
                while len(planet) > trigger and len(queue) > trigger:
                    compared1 += ord(planet[trigger].lower()) #each of alphabet letter converted to number by ord()
                    compared2 += ord(queue[trigger].lower())
                    trigger += 1 #needed for going to the next letter
                    if compared1 != compared2:    # inserting part engages when the numbers are different.
                        if compared1 > compared2:
                            result.insert(ordernum + 1, planet)
                        elif compared1 < compared2:
                            result.insert(ordernum, planet)
                        # initialization for next order
                        compared1 = 0
                        compared2 = 0
                        ordernum = 0
                        trigger = 0
                        break # break out from while loop
                break #break out from for in result loop

            else: #deciding order in result
                ordernum += 1
                
        if ordernum != 0: # insert for a first or a last ordered element
            if orbitdict[result[0]] > orbitdict[planet]:
                result.insert(0, planet)
            else:
                result.append(planet)
            ordernum = 0
    #converting result to planets
    for order in range(len(planets)):
        planets[order] = result[order]
        
def arrange2(planets, letterstring):
    adaptation = arrange1(planets, letterstring) # mutability
    return tuple(planets)