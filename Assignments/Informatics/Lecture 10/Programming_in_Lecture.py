'''
Created on 2017. 2. 28.

@author: korea
'''
'''
reader = open('haiku.txt', 'r') # reader for file object, r for reading
data = reader.read() #reads entire content of file into a string and copy to data
reader.close() # disconnect
len(data) # report the number of characters


#chunk a long text for memory lackage
reader = open('haiku.txt', 'r')
data = reader.read(64)
while data:
    print(len(data))
    data = reader.read(64)
#64, 64, 64, 64, 30
len(data)
#0
reader.close()

#read a text per a line
reader = open('haiku.txt', 'r')
bytes, lines = 0, 0
line = reader.readline()
while line:
    lines += 1
    bytes += len(line)
    line = reader.readline()
reader.close()
print('average: {}'.format(bytes / lines))


#readlines() is for all lines in file as list of strings
#file object is an iterable object
reader = open('haiku.txt', 'r')
content = reader.readlines()
reader.close()
bytes, lines = 0, 0
for line in content:
    lines += 1
    bytes += len(line)
print('average: {}'.format(bytes / lines))
'''
#UNIX(Mac OS) and MS Windows use different conventions to represent the end of a line in text files.
#Unix '\n'
#Windows '\r'


writer = open('elements.txt', 'w')
writer.write('elements')
writer.writelines(['He', 'Ne', 'Ar', 'Kr'])
writer.close()
#elementsHeNeArKr

#Python only writes what we tell it to end-of-line characters must be written explicitely: '\n'
#and we did not tell it to write any end of line characters
writer = open('elements.txt', 'w')
writer.write('elements\n')
writer.writelines(['He\n', 'Ne\n', 'Ar\n', 'Kr\n'])
writer.close()

writer = open('elements.txt', 'w')
print('elements', file = writer)
for gas in ['He', 'Ne', 'Ar', 'Kr']:
    print(gas, file=writer)
writer.close()

reader = open('haiku.txt', 'r')
data = reader.read()
reader.close()
writer = open('copy.txt', 'w')
writer.write(data)
writer.close()
#Not terabyte files

reader= open('haiku.txt', 'r')
writer = open('copy.txt', 'w')
for line in reader:
    writer.write(line)
reader.close()
writer.close()
#No binary files

#for an exact copy of the original file, use rstrip(), print which is automatically adds a newline when writing output such as
# print(line, file=writer, end='')
