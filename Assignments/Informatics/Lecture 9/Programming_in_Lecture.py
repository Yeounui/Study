'''
Created on 2016. 11. 14.

@author: korea
'''
from _ctypes import Union

# [expression for variable in iterable]
li =[3, 6, 2, 7]
a = [2* elem for elem in li] # each elements multiply twice.
print(a)

li = [3, 'spam', [4, 5]]
a = [3 * elem for elem in li]
print(a)

li = [('a', 1), ('b', 2), ('c', 7)]
a = [3 * n for (x, n) in li]
print(a)

def subtract(a, b):
    return a - b
li = [(6, 3), (1, 7), (5, 5)]
a = [subtract(y, x) for (x, y) in li]
print(a)

# [expression for variable1 in iterable1[if condition | for variable2 in iterable2]...]
li = [3, 6, 2, 7, 1, 9]
a = [2 * elem for elem in li if elem > 4]
print(a)

a = [p for p in range(2, 100) if not [x for x in range(2, p) if not p % x]]
print(a)

#zip()
firstnames = ['John', 'Terry', 'Eric']
lastnames = ['cleese', 'Giliam', 'Idle']
names = list(zip(firstnames, lastnames))
print(names)
first_names, last_names = (zip(*names))
print(list(first_names))
print(list(last_names))

#Set
tens = set(range(10))
lows = {0, 1, 2, 3, 4}
odds = {1, 3, 5, 7, 9}
# .add(), .remove(), .clear() can be used.
print(lows - odds)
print(lows)
print(odds - lows)
print(lows ^ odds) # symmetric

print(lows.intersection(odds)) #intersection
print(lows & odds)
print(lows.union(odds)) # union
print(lows | odds)
print(lows.issubset(tens)) # subset
print(lows <= tens)
print(lows.issuperset(odds)) # superset
print(lows >= odds)

#dictionary
birthday = {'Newton': 1642, 'Darwin': 1809} 
print(birthday['Darwin'], birthday['Newton'])

birthday = {} #empty dictionaries are written as {}
birthday['Darwin'] = 1809
birthday['Newton'] = 1942
birthday['Newton'] = 1642 # can be replaced.
birthday['Turing'] = 1912
print(birthday)
del birthday['Turing']
print(birthday)

# for key in dictionary
birthday = {'Newton' : 1642, 'Darwin' : 1809, 'Turing' : 1912}
for name in birthday: 
    print(name, birthday[name])


#.clear() // return None, but d is now empty
d = birthday
print(d)
d.clear()
print(d)


#.get() // returns d['x'] if 'x' in d, or 99 if is not
birthday = {'Newton': 1642, 'Darwin': 1809, 'Turing': 1912}
print(birthday)
result = birthday.get('x', 99)
print(result)
result = birthday.get('Darwin', 98)
print(result)

#.keys() // return a list of keys
d = birthday.keys()
print(d)

#.values() // return a list of values
d = birthday.values()
print(d)

#.items() // return a list of (key, value) pairs
d = birthday.items()
print(d)

#.update() // 
seuoh = {'seungchanoh': 1996}
print(birthday)
birthday.update(seuoh)
print(birthday)