'''
Created on 2017. 3. 2.

@author: korea
'''
def massTable(location):
    table = dict()
    reading = open(location, 'r')
    for line in reading:
        value = float(line[1:].lstrip())
        table[line[0]] = value
    reading.close()
    return table

def proteinMass(code, table, peptide = False):
    result = 0
    for letter in code:
        result += table[letter]
    if peptide == False:
        result += 18.01056
    return result