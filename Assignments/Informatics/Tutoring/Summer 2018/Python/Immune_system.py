class Organism:
    def __init__(self, textfile):
        opentxt = open(textfile, 'r')
        self.resistantlist = list(opentxt.read().split('\n'))
        opentxt.close()
        self.textfile = textfile
        self.intermediateset = set()
    def isResistant(self, virus):
        if str(virus) in self.resistantlist:
            return True
        else:
            if virus not in self.intermediateset:
                self.intermediateset.add(virus)
                return False
            else:
                self.intermediateset.remove(virus)
                self.resistantlist.append(str(virus))
                addtxt = open(self.textfile, 'a')
                addtxt.write('\n'+str(virus))
                addtxt.close()
                return False          
    def mutation(self, virus):
        if virus in self.intermediateset:
            self.intermediateset.remove(virus)
        if str(virus) in self.resistantlist:
            self.resistantlist.remove(str(virus))
            correctedtxt = '\n'.join(self.resistantlist)
            writetxt = open(self.textfile, 'w')
            writetxt.write(correctedtxt)
            writetxt.close()
        

organism = Organism('immune_system.txt')
print(organism.isResistant(1))
print(organism.isResistant(88))
print(organism.isResistant(virus=99))
print(organism.isResistant(2))
print(organism.isResistant(virus=99))
print(organism.isResistant(virus=99))
print(organism.isResistant(virus=99))
organism.mutation(virus=1)
print(organism.isResistant(virus=1))
print(organism.isResistant(virus=1))
print(organism.isResistant(virus=1))
organism.mutation(virus=99)
print(organism.isResistant(virus=99))
print(organism.isResistant(virus=99))
print(organism.isResistant(virus=99))