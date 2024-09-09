'''
Created on 2018. 7. 8.

@author: korea
'''
def processMatches(textfile):
    opentxt = open(textfile, 'r')
    readtxt = opentxt.readline()
    resultlist = list()
    while readtxt:
        if readtxt.find(',') != -1:
            gameresult = readtxt.split(',')
            resultlist.append(gameresult)
        readtxt = opentxt.readline()
    opentxt.close()
    
    countrydict = dict()
    for gameresult in resultlist:
        if not gameresult[0] in countrydict.keys():
            countrydict[gameresult[0]] = [0,0,0,0,0,gameresult[-1].strip()]
        if not gameresult[1] in countrydict.keys():
            countrydict[gameresult[1]] = [0,0,0,0,0,gameresult[-1].strip()]
        comparescore = gameresult[2].split('-')
        if comparescore[0] > comparescore[1]:
            countrydict[gameresult[0]][0] += 1
            countrydict[gameresult[1]][1] += 1
            countrydict[gameresult[0]][3] += int(comparescore[0])
            countrydict[gameresult[0]][4] += int(comparescore[1])
            countrydict[gameresult[1]][4] += int(comparescore[0])
            countrydict[gameresult[1]][3] += int(comparescore[1])
            
        elif comparescore[0] < comparescore[1]:
            countrydict[gameresult[0]][1] += 1
            countrydict[gameresult[1]][0] += 1
            countrydict[gameresult[0]][3] += int(comparescore[0])
            countrydict[gameresult[0]][4] += int(comparescore[1])
            countrydict[gameresult[1]][4] += int(comparescore[0])
            countrydict[gameresult[1]][3] += int(comparescore[1])
        else:
            countrydict[gameresult[0]][2] += 1
            countrydict[gameresult[1]][2] += 1
            countrydict[gameresult[0]][3] += int(comparescore[0])
            countrydict[gameresult[0]][4] += int(comparescore[1])
            countrydict[gameresult[1]][4] += int(comparescore[0])
            countrydict[gameresult[1]][3] += int(comparescore[1])
    
    resultdict = dict()
    for country in countrydict.keys():
        group = countrydict[country].pop(-1)
        if group not in resultdict.keys():
            resultdict[group] = dict()
        resultdict[group][country] = countrydict[country]
    
    return resultdict

def showGroup(resultdict, group, writetext=None):
    groupdict = resultdict[group] # get dictionary of group
    countries = groupdict.keys() # country list in the group
    for country in countries:
        scoreresult = groupdict[country] # get dictionary of a country
        groupdict[country].append(scoreresult[0] + scoreresult[1] + scoreresult[2]) # the number of play
        groupdict[country].append(3*scoreresult[0] + scoreresult[2]) # pts
        groupdict[country].append(scoreresult[3] - scoreresult[4]) # goal difference
    
    for country1 in countries:
        rankingcount = 0 #set & reset
        for country2 in countries: # double for roof for handling two variables
            if country1 != country2: # no need to check the same
                if groupdict[country1][6] == groupdict[country2][6]: # pts comparison if same
                    if groupdict[country1][7] > groupdict[country2][7]: # goal difference comparison
                        rankingcount += 1 # the higher value, the better country
                    elif groupdict[country1][7] == groupdict[country2][7]: # goal difference comparison if same
                        if ord(country1[0]) < ord(country2[0]): # alphabetical order
                            rankingcount += 1
                elif groupdict[country1][6] > groupdict[country2][6]: #pts comparison
                    rankingcount += 1
        groupdict[country1].append(rankingcount) # put rank value into dictionary
    
    formatsheet = '' # set variable for chart
    ranking = len(countries)-1 # set variable for rank in largewise (3, 2, 1, 0)
    while ranking != -1:
        for country in countries:
            if groupdict[country][-1] == ranking:
                formatsheet +=  '|{} |   {} |   {}   {}   {} {} {} {} |   {} |\n'.format(country.rjust(22), groupdict[country][5], groupdict[country][0], groupdict[country][1], groupdict[country][2], str(groupdict[country][3]).rjust(3), str(groupdict[country][4]).rjust(3), str(groupdict[country][7]).rjust(3), groupdict[country][6])
                # put values in the chart
        ranking -= 1 # manage new variable for searching next ranked country
        
    resultstr = '                            GROUP {}                            \n'.format(group)+ '+-----------------------+-----+-------------------------+-----+\n'+'|                       |   P |   W   L   D   F   A   S | Pts |\n'+'+-----------------------+-----+-------------------------+-----+\n'+formatsheet+'+-----------------------+-----+-------------------------+-----+'
    # template
    if writetext == None:
        print(resultstr)
    else:
        opentxt = open(writetext, 'w')
        opentxt.write(resultstr)
        opentxt.close()

stats = processMatches('worldcup2010.txt')
print(stats)
print(stats['A'])
print(stats['B'])
print(stats['F'])
print(showGroup(stats, 'A'))
print(showGroup(stats, 'D'))
showGroup(stats, 'F', 'groupF.txt')