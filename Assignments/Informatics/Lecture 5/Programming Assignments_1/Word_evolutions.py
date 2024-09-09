'''
Created on 2016. 10. 3.

@author: korea
'''
givenvo=input()
initdec=input()
immedlet=str()
result=''

initlet=givenvo[0]
initnum=ord(givenvo[0])
while initnum != ord(initdec):
    initnum+=1
    if initnum == 91:
        initnum = 65
    immedlet+=chr(initnum)
result=givenvo[0] + immedlet.lower() + initdec
bridge=len(result[1:])

initlet=givenvo[1]
for initlet in givenvo:
    immedlet = ''
    initnum = ord(initlet)
    for level in range(0,bridge-1):
        initnum+=1
        if initnum == 91:
            initnum = 65
        immedlet+=chr(initnum)
    result=initlet + (immedlet[0:-1]).lower() + chr(ord(immedlet[-1]))
    print(result)