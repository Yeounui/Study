'''
Created on 2018. 6. 30.

@author: korea
'''
import math

def inHouse(xpoint, ypoint, inch = True):
    if inch is False:
        xpoint = xpoint/0.0254
        ypoint = ypoint/0.0254
    global distance
    distance = (xpoint**2+ypoint**2)**(1/2)
    if distance/12 < 6 + 3/(2*math.pi):
        return True
    else:
        return False
    
def validPositions(stonelist, inch = True):
    rcount = 0
    ycount = 0
    for step in range(len(stonelist)):
        for poststep in range(step+1, len(stonelist)):
            stonebetween = ((stonelist[step][0]-stonelist[poststep][0])**2 + (stonelist[step][1]-stonelist[poststep][1])**2)**(1/2)
            if inch is False:
                stonebetween = stonebetween/0.0254
            if stonebetween < 36/math.pi:
                return False
        if stonelist[step][-1] == 'R':
            rcount += 1
        else:
            ycount += 1
    if rcount > 8 or ycount > 8:
        return False
    return True

def score(stonelist, inch = True):
    closestone = str()
    stonedistance = int()
    assert validPositions(stonelist, inch), 'invalid stone positions'
    for stoneposition in stonelist:
        if inHouse(stoneposition[0], stoneposition[1], inch) is True:
            



print(inHouse(70.0, 0.0))
print(inHouse(70.0, 0.0, False))
print(inHouse(78.0, 0.0))
print(validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')]))
print(validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')]))
print(validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')]))
print(score([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')]))
print(score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')]))
print(score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')]))
print(score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'Y'), (1.0668, 0.9398, 'R')], False))
print(score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'Y')], inch=False))
print(score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'R')], False))