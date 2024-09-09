DNA = 'deoxy riboNucleic Acid'
#DNA[0] = 'D'
#DNA[9] = 'N'
#DNA[-4] = 'A'
#print(DNA)

DNA = DNA.capitalize()
print(DNA)
print(DNA.title())
print(DNA.swapcase())
print(DNA.lower())
print(DNA.upper())

print(len(DNA))
DNA_center = DNA.center(32)
print(DNA_center)
print(DNA.ljust(32))
print(DNA.rjust(32))

print('423'.zfill(5))

print(DNA_center.strip())
print(DNA_center.lstrip())
print(DNA_center.rstrip())

print(DNA.startswith('Deoxy'))
print(DNA.endswith('acid'))


ex = 'eibnhtaxaxaeobmgovpaxabnupg'
print(ex.count('axa'))

print(ex.find('axa')) # failure -1
print(ex.rfind('axa'))

print(ex.index('axa')) # failure error
print(ex.rindex('axa'))

print(ex.split('ax')) #join
print(ex.rsplit('ax'))

quote = "I wish to finish this tutoring program.\nbut I am still teaching now."
quote_words = quote.split()
print("!!!")
print(" ".join(quote_words))
print(quote_words)
print(quote.splitlines())
quote = quote.replace(' ', '\t')
quote = quote.replace('wish', 'love')
print(quote)
print(quote.expandtabs(8))


"""
isalnum
isalpha
isdecimal
isdigit
islower
isnumeric
isprintable
isspace
istitle
"""