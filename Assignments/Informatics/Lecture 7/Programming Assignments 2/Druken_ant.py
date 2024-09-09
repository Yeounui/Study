'''
Created on 2016. 11. 8.

@author: Seungchan Oh
@student_number: 01603277
'''
def grid(string, direction):
    #Error decision
    assert string**2 == len(direction), 'invalid arguments'
    # deciding grid length
    if len(direction) == string**2:
        result = list()
        line = list()
        # separating string and making list
        for linenum in range(0, string):
            line=list(direction[string*linenum:string*(linenum+1)])
            result.append(line)
        return result

def text(grid):
    result = ''
    #textilization
    for line in grid:
        string = (' '.join(line)) # give a space
        result += string + '\n' #give a line
    return result.rstrip()

def step(square, orbit):
    #definition
    point_x = orbit[1]
    point_y = orbit[0]
    #move on
    if square[point_y][point_x] == '>': #when I am on certain direction sign
        square[point_y][point_x] = 'v' #change direction sign
        point_x += 1 # move the orbit
    elif square[point_y][point_x] == '<':
        square[point_y][point_x] = '^'
        point_x -= 1
    elif square[point_y][point_x] == '^':
        square[point_y][point_x] = '>'
        point_y -= 1
    else:
        square[point_y][point_x] = '<'
        point_y += 1
    #correction without direction sign
    if not 0 <= point_x <= len(square)-1 or not 0 <= point_y <= len(square)-1: # conditions
        if not 0 <= point_x <= len(square)-1: 
            if point_x < 0: 
                point_x += 1 # correction for orbit value
            elif point_x > len(square)-1:
                point_x -= 1
        elif not 0 <= point_y <= len(square)-1:
            if point_y < 0:
                point_y += 1
            elif point_y > len(square)-1:
                point_y -= 1
    return (point_y, point_x)

def steps(square):
    #definition
    point_y = len(square)-1
    point_x = 0
    result = [(len(square)-1, 0)]
    # expressing series of steps
    while (point_y, point_x) != (0, len(square)-1):
       (point_y, point_x) = step(square, (point_y, point_x)) #move on
       result.append((point_y, point_x)) # appending steps left
    return result
square=square = [['^', 'v', '>', '^', '>'], ['<', '>', 'v', '<', '>'], ['>', '<', '>', '^', '<'], ['<', '^', 'v', '>', '>'], ['<', 'v', '<', '^', 'v']]
print(step(square, (0, 1)))
print(text(square))
print(steps(square))