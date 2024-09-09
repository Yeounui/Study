'''
Created on 2017. 3. 23.

@author: Seungchan Oh
@student_number: 01603277
'''
class DrunkenAnt:
    def __init__(self, targettxt):
        #Definition
        catalyst = str()
        savepath = list()
        #Read line by line
        opentxt = open(targettxt, 'r')
        readtxt = opentxt.readline()
        #until readtxt finish
        while readtxt:
        #Each letter in line is checked and included into catalyst
            for letter in readtxt.rstrip():
                if letter in ('^', '<', '>', 'v'):
                    catalyst += letter
        #Catalyst is a part of savelist
            savepath.append(list(catalyst))
            readtxt = opentxt.readline()
            catalyst = ''
        self.savepath = savepath
        self.location = (len(savepath)-1, 0)
    
    def position(self):
        return self.location
    
    def __repr__(self):
        result = ''
        # add space between space and combine into result
        for line in self.savepath:
            string = ' '.join(line) + '\n'
            result += string
        return result.rstrip()
    
    def __str__(self):
        result = ''
        xaxis = -1
        for line in self.savepath:
            xaxis += 1
            string = ' ' + '  '.join(line) + ' '
            #Express location
            if xaxis == self.location[0]:
                string = string[:3*self.location[1]]+ '['+string[3*self.location[1]+1]+']'+(string[3*(self.location[1]+1):])
            result += string + '\n'
        return result.rstrip('\n')
    
    def step(self):
    #definition
        point_x = self.location[1]
        point_y = self.location[0]
    #move on
        if self.savepath[point_y][point_x] == '>': #when I am on certain direction sign
            self.savepath[point_y][point_x] = 'v' #change direction sign
            point_x += 1 # move the orbit
        elif self.savepath[point_y][point_x] == '<':
            self.savepath[point_y][point_x] = '^'
            point_x -= 1
        elif self.savepath[point_y][point_x] == '^':
            self.savepath[point_y][point_x] = '>'
            point_y -= 1
        else:
            self.savepath[point_y][point_x] = '<'
            point_y += 1
    #correction without direction sign
        gridlength = len(self.savepath)-1
        if not 0 <= point_x <= gridlength or not 0 <= point_y <= gridlength: # conditions
            if not 0 <= point_x <= gridlength: 
                if point_x < 0: 
                    point_x += 1 #correction for orbit value
                elif point_x > gridlength:
                    point_x -= 1
            elif not 0 <= point_y <= gridlength:
                if point_y < 0:
                    point_y += 1
                elif point_y > gridlength:
                    point_y -= 1
        self.location = (point_y, point_x)
        return self.location
    
    
    def steps(self):
    #definition
        (end_y, end_x) = self.location
        result = [self.location]
    # expressing series of steps
        while (end_y, end_x) != (0, len(self.savepath)-1):
            (end_y, end_x) = self.step() #move on
            result.append((end_y, end_x)) #appending steps left
        return result
    
ant = DrunkenAnt('square.txt')
print(ant.position())
print(ant)
print(ant.step())
print(ant)
print(ant.steps())
print(ant.position())
print(ant)