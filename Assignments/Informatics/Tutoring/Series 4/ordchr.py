Aord = ord('A')
Achr = chr(Aord)
achr = chr(Aord+32) # upper -> lower
print(Achr)
print(achr)

#Upper alphabet: 65-90
#Lower alphabet: 97-122

# Usage: When it is necessary to deal with alphabetical order.

alphabet_ord = ord('A')-1
alphabet_list = list()
while alphabet_ord != ord('z'):
    alphabet_ord+= 1
    alphabet_list.append(chr(alphabet_ord))

    if alphabet_ord is ord("Z"):
        alphabet_ord += 6 # Lower after upper

print(alphabet_list)