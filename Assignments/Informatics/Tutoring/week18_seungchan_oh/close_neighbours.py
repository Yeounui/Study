'''
Created on 2017. 3. 8.

@author: Seungchan Oh
@student_number: 01603277
'''
def capitals(giventxt):
    # Definition
    citydict = dict()
    # Read text line by line
    opentxt = open(giventxt, 'r')
    readtxt = opentxt.readline()
    readtxt = readtxt.strip('\n')
    # divide to 2 words: key and value
    while readtxt:
       restrictsite = readtxt.index(',')
       dictvalue = readtxt[:restrictsite]
       dictkey = readtxt[-2:]
    # Putting to dictionary
       citydict[dictkey] = dictvalue
       readtxt = opentxt.readline()
       readtxt = readtxt.strip('\n')
    opentxt.close()
    return citydict

def coordinates(giventxt):
    # Definition
    coordinatedict = dict()
    count = 0
    order = 2
    # Read text
    opentxt = open(giventxt, 'r')
    readtxt = opentxt.readline()
    readtxt = readtxt.strip('\n')
    from ast import literal_eval
    # Define order and count to separate sentence
    while readtxt:
        while count != 2:
            order += 1
            if readtxt[order] == ',':
                count += 1
    # extract key and value and put it in
        dictkey = readtxt[:order]
        dictvalue = literal_eval(readtxt[order+1:])
        coordinatedict[dictkey] = dictvalue
        readtxt = opentxt.readline()
        readtxt = readtxt.strip()
        count = 0
        order = 2
    opentxt.close()
    return coordinatedict
    
def greatCircleDistance(pointA, pointB):
    import math
    b1 = math.radians(pointA[0])
    b2 = math.radians(pointB[0])
    l1 = math.radians(pointA[1])
    l2 = math.radians(pointB[1])
    #figure out radius
    distance = 6371*math.acos((math.sin(b1)*math.sin(b2) + math.cos(b1)*math.cos(b2)*math.cos(l1-l2)))
    return distance

def closeNeighbours(targetcity, capital, coordinate):
    # Definition
    resultset = set()
    targetpoint = coordinate[targetcity]
    state = targetcity[-2:]
    capitalcity = capital[state]
    # forming element with defined value
    capitaladdress = capitalcity + ',' + state
    # Definition
    capitalpoint = coordinate[capitaladdress]
    measurement = greatCircleDistance(targetpoint, capitalpoint)
    # find out cities in distance
    for acapital in capital.keys():
        acity = capital[acapital] + ',' + acapital
        distance = greatCircleDistance(targetpoint, coordinate[acity])
        if measurement > distance:
            resultset.add(acity)
    return resultset
    
capital = capitals('capitals.txt')
print(capital)
coordinate = coordinates('cities.txt')
print(coordinate)
print(closeNeighbours('Dalhart,TX', capital, coordinate))
