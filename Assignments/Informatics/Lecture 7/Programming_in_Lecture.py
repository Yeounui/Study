'''
Created on 2016. 10. 13.

@author: korea
'''
#list: mutable(elements can be changed in place) sequence of objects
gases = ['He', 'Ne', 'Ar', 'Kr']
print(gases) #['He', 'Ne', 'Ar', 'Kr']
# elements and order is two important things in list.
print(gases[0], gases[-1]) #He Kr
gases[0] = 'Xe'
gases[-1] = 'Rn'
print(gases) #['Xe', 'Ne', 'Ar', 'Rn']

helium = ['He', 'Helium', 2, 4.00260]
gases = [['He', 2], ['Ne', 10], ['Ar', 18]]

gases= [] # is similar as 0 in number, '' in string.
# the empty list is False in a boolean expression
# the opposite holds true for True
if gases:
    print('There are gasese in the list.')
else:
    print('There are no gases in the list.')

gases = ['He', 'Ne', 'Ar', 'Kr']
def revervesed(list):
    return list[::-1]
#>>>reversed(gases)
#['Kr', 'Ar', 'Ne', 'He']

#string methods return a new string: immutable
#list methods modify an existing list: mutable
metals = ['gold', 'iron', 'lead', 'gold']
metals.append('tin') #['gold', 'iron', 'lead', 'gold', 'tin']
metals.count('gold') #2
#.pop coming out last elements
metals = ['gold', 'iron', 'lead', 'gold']
#metals.index('sulfur') # error
metals.sort() #metals = ['gold', 'gold', 'iron', 'lead']
#metals = metals.reverse() # Error, just put metals.reverse()
#print(metals) #None

gases = ['He', 'Ne', 'Ar', 'Kr']
print(gases[0])
print(gases[-1])
#print(gases[4]) is an index error
print(gases[9 - 8])
#print(gases[1.0]] should be integer.
gases = [['He', 2], ['Ne', 10], ['Ar', 18]]
print(gases[1]) #['Ne', 10]
print(gases[1][0]) #Ne

gases = ['He', 'Ne', 'Ar', 'Kr']
gases.append('Kr')
gases.append('Xe')
gases.append('Rn')
gases.append('Uuo')
print(gases)

gases[1:3] #['He', 'Ne']
gases[:4] #['H', 'He', 'Ne', 'Ar']
gases[4:] #['Kr', 'Xe', 'Rn']
gases[:] #['H', 'He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
gases[::2] #['H', 'Ne', 'Kr', 'Rn']

len(gases) #8

for i in range(len(gases)):
    print(gases[i])

numbers = [1, 2, 3, 4, 5]
for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2
print(numbers)

for index, numer in enumerate(numbers):
    numbers[index] = number ** 2
print(number)

lanthanides = ['Ce', 'Pr', 'Nd']
actinides = ['Th', 'Pa', 'U']
all = lanthanides + actinides
print(all)
print(lanthanides * 3)

#actinides + 'NP' is an error.
actinides + ['NP']

water = 'H2O'
water_split = list(water) #['H', '2', 'O']
print(''.join(water_split))
print('-'.join(water_split))

list(range(1, 5))
list(range(10))
list(range(1, 10, 2))
list(range(20, 4, -5))
list(range(10, 20, -5))

element = 'cesium'
element = list(element)
element[2] = 'r'
print(element)
''.join(element)

element = list(element)
element[1] = 'h'
element[3, 6] = ['o', 'm', 'e']
print(element)
''.join(element)
element[4:4] = ['m', 'o', 's', 'o']
print(element)
''.join(element)

element = list('ytterbium')
element[:2] = []
print(element)
element[:1] = []
print(element)
element = list('ytterbium')
del element[:2]
print(element)
del element[:1]
print(element)

gases = ('He', 'Ne', 'Ar', 'Kr')
print(gases)
print(gases[0], gases[-1])
print(gases[3:2])
print(gases[2:3])

gases = 'He', 'Ne', 'Ar'
print(gases)
(gas1, gas2, gas3) = gases
print(gas1, gas2)
gas1, gas2, gas3 = gases

gas1, gas2 = 'He', 'Ne'
gas1, gas2 = gas2, gas1



a = 'plutonium' * 100
b = 'plutonium' * 100
a == b # True
a is b # False
id(a), id(b)

a = 'plutonium' * 100
b = a
a == b #True
a is b #True
id(a), id(b)